"""
Week 7 quiz Q7-Q9: implement Oja's rule for a single neuron and explore its
convergence behavior, using the course's own c10p1 dataset (100 2D points,
from the Dayan & Abbott textbook exercises).

Discrete update rule (derived in Q5/Q6):
    w_{i+1} = w_i + dt * eta * (v*u - alpha * v**2 * w_i),   v = u . w_i
"""
import pickle
import numpy as np

with open("c10p1.pickle", "rb") as f:
    raw = pickle.load(f)

data = np.asarray(raw["c10p1"] if isinstance(raw, dict) else raw)
print("data shape:", data.shape)


def run_oja(points, eta=1.0, alpha=1.0, dt=0.01, n_iter=100_000, seed=None,
            use_oja=True):
    rng = np.random.default_rng(seed)
    w = rng.normal(size=2)
    n = len(points)
    for i in range(n_iter):
        u = points[i % n]
        v = u @ w
        if use_oja:
            dw = dt * eta * (v * u - alpha * v**2 * w)
        else:
            dw = dt * eta * (v * u)  # pure Hebb rule (no subtractive term)
        w = w + dw
    return w


# --- Q7: zero-mean-centered data, Oja's rule ---------------------------------
mean = data.mean(axis=0)
centered = data - mean
print("\nQ7: mean-centered data, original mean was:", mean)

Q = (centered.T @ centered) / len(centered)
vals, vecs = np.linalg.eig(Q)
print("correlation/covariance matrix eigenvalues:", vals)
print("principal eigenvector:", vecs[:, np.argmax(vals)])
print("expected |w| = 1/sqrt(alpha) =", 1 / np.sqrt(1.0))

for seed in range(5):
    w = run_oja(centered, seed=seed)
    print(f"  seed={seed}: w = {w}, |w| = {np.linalg.norm(w):.4f}")

# --- Q8: same data, but shifted to a nonzero mean ----------------------------
print("\nQ8: data shifted away from zero mean")
for shift in [(3, 3), (-2, 5)]:
    shifted = data + np.array(shift) - mean  # shift relative to original mean
    print(f" shift={shift}, new mean={shifted.mean(axis=0)}")
    for seed in range(3):
        w = run_oja(shifted, seed=seed)
        print(f"  seed={seed}: w = {w}, |w| = {np.linalg.norm(w):.4f}, "
              f"direction angle = {np.degrees(np.arctan2(w[1], w[0])):.1f} deg")
    print(f"  direction toward shifted mean: angle = "
          f"{np.degrees(np.arctan2(shifted.mean(axis=0)[1], shifted.mean(axis=0)[0])):.1f} deg")

# --- Q9: pure Hebb rule (no normalization term) on mean-centered data --------
print("\nQ9: pure Hebb rule (no -alpha*v^2*w term), mean-centered data")
for seed in range(3):
    w = run_oja(centered, seed=seed, n_iter=2000, use_oja=False)
    print(f"  seed={seed}, n_iter=2000:  w = {w}, |w| = {np.linalg.norm(w):.4f}")
for seed in range(3):
    w = run_oja(centered, seed=seed, n_iter=20000, use_oja=False)
    print(f"  seed={seed}, n_iter=20000: w = {w}, |w| = {np.linalg.norm(w):.4f}")
