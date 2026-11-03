"""
Week 4 graded assignment: Information Theory & Neural Coding
Questions 7-9: Poisson neuron models and population coding (cricket cercal system)
"""
import pickle
import numpy as np

# ---- Load data ----
with open('tuning.pickle', 'rb') as f:
    tuning = pickle.load(f)

stim = np.array(tuning['stim'])  # 24 stimulus directions, 0-345 deg in 15 deg steps
neurons = {n: np.array(tuning[n]) for n in ['neuron1', 'neuron2', 'neuron3', 'neuron4']}

print("=== Question 7: Tuning curve shape ===")
tuning_curves = {}
for name, arr in neurons.items():
    mean_rate = arr.mean(axis=0)  # mean over 100 trials, per stimulus
    tuning_curves[name] = mean_rate
    print(f"{name}: min={mean_rate.min():.2f}, max={mean_rate.max():.2f}, "
          f"argmax stim={stim[np.argmax(mean_rate)]}, "
          f"has_zero_region={np.any(mean_rate < 0.5)}")

# Check: does it look like half-wave rectified cosine (i.e., goes to ~0 and stays there
# for stimuli opposite the preferred direction), vs. a full (unrectified) cosine which
# would go negative, vs Gaussian (single narrow peak, ~0 far from peak on BOTH sides
# symmetric), vs linear.
for name, mean_rate in tuning_curves.items():
    print(f"\n{name} full tuning curve (stim, rate):")
    for s, r in zip(stim, mean_rate):
        print(f"  {s:6.1f}: {r:7.3f}")

print("\n=== Question 8: Which neuron is NOT Poisson? ===")
for name, arr in neurons.items():
    # arr is firing RATE (Hz) over 10-second trials -> spike count = rate * 10
    spike_counts = arr * 10.0
    mean_per_stim = spike_counts.mean(axis=0)
    var_per_stim = spike_counts.var(axis=0)
    # Fano factor per stimulus value (only where mean > 0 to avoid div by zero)
    valid = mean_per_stim > 0.5
    fano = var_per_stim[valid] / mean_per_stim[valid]
    print(f"{name}: mean Fano factor (spike counts) = {fano.mean():.3f}, "
          f"std = {fano.std():.3f}, min={fano.min():.3f}, max={fano.max():.3f}")

print("\n=== Question 9: Population vector decoding ===")
with open('pop_coding.pickle', 'rb') as f:
    pop = pickle.load(f)
print("pop_coding keys:", list(pop.keys()))

r_max = {name: tuning_curves[name].max() for name in neurons}
print("r_max per neuron:", r_max)

# population vector: sum over neurons of (r_i / r_max_i) * c_i  (c_i is 2D basis vector)
vec = np.zeros(2)
for i in range(1, 5):
    name = f'neuron{i}'
    r = pop[f'r{i}']
    r = np.array(r).mean()  # average over the 10 trials given for this neuron
    c = np.array(pop[f'c{i}'])
    weight = r / r_max[name]
    vec += weight * c
    print(f"neuron{i}: r_mean={r:.3f}, r_max={r_max[name]:.3f}, weight={weight:.4f}, c={c}")

print("\nSummed vector:", vec)

# Convention: 0 degrees = +y axis (north), 90 degrees = +x axis (east)
# standard atan2(x, y) gives angle from +y axis towards +x axis
angle_rad = np.arctan2(vec[0], vec[1])
angle_deg = np.degrees(angle_rad)
angle_deg_mod = angle_deg % 360
print(f"\nPopulation vector angle: {angle_deg:.2f} deg -> normalized: {angle_deg_mod:.2f} deg")
print(f"Rounded to nearest degree: {round(angle_deg_mod)}")
