# Week 2 Graded Assignment: Spike-Triggered Averages (A Glimpse Into Neural Encoding)

**Course:** University of Washington, Computational Neuroscience (Coursera)
**Recorded:** November 2, 2026
**Source:** Graded Assignment, Module 2, "Spike Triggered Averages: A Glimpse Into Neural Encoding."
**Status:** Worked answer key with supporting code and real computed results. Submission and
score are not confirmed — this document records the work, it is not a submission receipt.

**Dataset:** `c1p8.pickle` — recordings from the H1 motion-sensitive neuron of the blowfly
(*Calliphora vicina*), from the lab of Dr. Robert de Ruyter van Steveninck. 600,000 samples
at 500 Hz (1200 s / 20 min), 53,601 total spikes. Stimulus is the velocity of a pattern of
vertical bars.

**Code:** [quiz2.py](../assignments/week2_spike_triggered_average/quiz2.py),
[compute_sta.py](../assignments/week2_spike_triggered_average/compute_sta.py).
Both were completed, run locally with Python 3.11 / NumPy / Matplotlib, and reproduced the
same numbers across two separate runs. The dataset file (`c1p8.pickle`, ~5.4 MB) is
intentionally not committed (see `.gitignore`) — download it from the assignment page if
re-running.

## Quick Answer Key

| Question | Answer | Basis |
|---|---|---|
| 1 | `y(t) = cos[x(t-θ)]` is **not** linear | Only option where the output is a nonlinear function of the input |
| 2 | The stimuli preceding a spike, averaged over all stimuli that elicited a spike | Standard definition; matches lecture 2.3 |
| 3 | `sampling_period = 2` (ms) | 1000 ms / 500 Hz = 2 ms |
| 4 | `num_timesteps = 150` | 300 ms window / 2 ms per sample = 150 |
| 5 | `num_spikes = 53583` | Computed from data (53,601 total − 18 within the first 300 ms) |
| 6 | The plot that ramps up slowly, peaks sharply ~28 ms before the spike, then drops straight back to baseline (no sustained negative undershoot) | Matches our actual computed STA, see `sta_plot.png` |
| 7 | Differentiation | STA shape is a rise-then-sharp-fall transient, not a flat average or monotonic decay |
| 8 | A positive value followed by a negative value | Mirrors the STA's own shape: large positive buildup followed by a sharp drop |
| 9 | Principal component analysis / covariance analysis | Explicitly the method taught in lecture 2.3 for multi-feature neurons |

## Question 1: Which system is not a linear filter?

Four candidate systems, with `x(t)` the input and `y(t)` the output:

- `y(t) = Σ_{n=0}^∞ aⁿ x(t − nτ)` with `0 < a < 1` — a discrete leaky integrator. Linear:
  each output sample is a weighted sum of past inputs.
- `y(t) = 3x(t) − 5x(t − τ)` — a two-tap FIR filter. Linear.
- `y(t) = cos[x(t − θ)]` — applies `cos(·)` **to the signal itself**, not to time. This
  breaks superposition and scaling (`cos(a+b) ≠ cos(a) + cos(b)`). **Not linear.**
- `y(t) = ∫₀^∞ e^{−τ} x(t − τ) dτ` — a continuous leaky integrator (convolution with an
  exponential kernel). Linear.

**Answer: the cosine system.**

## Question 2: Definition of the spike-triggered average

From lecture 2.3: "For every time there's a spike, we look back in time at the chunk of
stimulus preceding that spike, and grab it ... the spike-triggered average is just the
average of all of these examples." That is: **the stimuli preceding a spike, averaged over
all stimuli that elicited a spike.**

The other options describe different quantities: the set of spike-eliciting stimuli itself
(no averaging), the inter-spike interval (a timing statistic, not a stimulus feature), or an
average-over-time-first-then-collect procedure (backwards from the correct order of
operations).

## Question 3: Sampling period

Sampling rate is 500 Hz → 500 samples per second → `1000 / 500 = 2` ms between samples.

```python
sampling_period = 2  # ms
```

## Question 4: Number of timesteps in a 300 ms window

Window width 300 ms, sampling period 2 ms, and we exclude the sample at exactly −300 ms:

```python
num_timesteps = 300 // 2  # = 150
```

150 is even, matching the question's hint.

## Question 5: Number of spikes (excluding the first 300 ms)

```python
spike_times = rho[num_timesteps:].nonzero()[0] + num_timesteps
num_spikes = len(spike_times)
```

Run against the actual dataset: **`num_spikes = 53583`** (18 of the 53,601 total recorded
spikes occur within the first 300 ms and are correctly excluded).

## Question 6: Matching the STA plot

```python
sta = np.zeros((num_timesteps,))
for t in spike_times:
    sta += stim[t - num_timesteps:t]
sta /= num_spikes
```

Running this against the real data gives a curve that is:

- Near flat / close to zero for most of the window (−300 ms to about −60 ms before the
  spike).
- Rises smoothly starting around −60 ms.
- Peaks sharply at **28 ms before the spike** (value ≈ 29.5).
- Falls steeply right back down to baseline by the time of the spike — **no sustained
  negative undershoot** (the last sample is −0.06, essentially noise-level, not a real
  trough).

See [`sta_plot.png`](../assignments/week2_spike_triggered_average/sta_plot.png) for the
actual rendered curve. On the quiz page, the second answer option (ramp up → sharp peak
near the right edge → sharp drop straight back to baseline, no dip below zero) is the one
that matches — not the option with the biphasic positive-peak-then-negative-trough shape,
and not the flat, rectangular/step, or narrow-spike options.

## Question 7: What operation does this neuron compute?

Options were: no response, running average/sum, differentiation, leaky integration.

A running average or leaky integration would produce a smooth, monotonically decaying (or
flat) kernel — no sharp sign change. What we actually see is a transient: the stimulus
builds up over tens of milliseconds and then changes sharply right as the spike occurs. That
rapid-change sensitivity is the signature of **differentiation** — the neuron is more
responsive to how fast the stimulus is changing than to its absolute level, consistent with
H1 being a motion- (velocity-) sensitive neuron.

## Question 8: Preferred stimulus pattern

Given the STA's own shape — a sustained positive value building up, followed by a sharp
drop — the neuron should respond most strongly to **a positive value followed by a negative
value**, i.e., a stimulus that mirrors the shape of its own STA. This is exactly the
"ramps up, then goes down" example used in lecture 2.3 to illustrate a feature that
triggers firing.

## Question 9: Finding two feature modes

Options: plain STA, splitting spikes into two disjoint sets and averaging separately,
PCA/covariance analysis, or iteratively subtracting the first STA and recomputing.

Lecture 2.3 covers this directly: when a neuron is sensitive to **on** and **off** features
that are roughly mirror images of each other, the plain spike-triggered average can collapse
to near zero (the two modes cancel in the average), hiding the structure. The lecture's own
retinal-ganglion-cell example resolves this with **principal component analysis /
covariance analysis** — projecting spike-triggering stimuli onto the top two principal
components reveals the two modes that a simple average would miss. Splitting spikes into
arbitrary disjoint sets has no principled basis for finding the right two directions, and
iteratively subtracting the first STA and re-averaging does not reliably separate
overlapping/mirror-symmetric modes the way PCA does.

## Reproduction

```powershell
cd assignments/week2_spike_triggered_average
pip install numpy matplotlib
python quiz2.py
```

Expected console output:

```
num_spikes = 53583
sta[:5] = [-0.213 -0.331 -0.291 -0.231 -0.246]
sta[-5:] = [0.287 0.185 0.243 0.129 -0.061]
sta min/max = -0.363 29.473
Saved plot to sta_plot.png
```
