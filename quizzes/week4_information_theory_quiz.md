# Week 4 Graded Assignment: Information Theory & Neural Coding

**Course:** University of Washington, Computational Neuroscience (Coursera)
**Recorded:** November 2, 2026
**Status:** Worked answer key with supporting code and real computed results, ready to copy into Coursera.

## Quick Answer Key

| Question | Answer | Basis |
|---|---|---|
| 1 | **0.4690** bits | Entropy of Bernoulli(p=0.1): H = −0.1·log₂(0.1) − 0.9·log₂(0.9) |
| 2 | **0.0904** bits | Mutual information MI(S,F); computed H(F)=0.4690, noise entropy=0.3786, MI = 0.4690−0.3786 |
| 3 | The pieces that make up the image. | φᵢ = basis functions (the "shapes" being summed) |
| 4 | The difference between the actual image and the representation. | ε = reconstruction error/residual |
| 5 | The level of transparency vs. opacity/influence of each piece. | aᵢ = weighting coefficients on each basis function |
| 6 | The importance of coding efficiency. | λ = sparsity/efficiency tradeoff parameter |
| 7 | Half-wave rectified cosine. | Real tuning curves (see below) peak then clip to exactly 0 over a ~180° range, then resume — a rectified cosine, not Gaussian/linear/unrectified cosine |
| 8 | Neuron 3. | Fano factor ≈1.0 for neurons 1, 2, 4 (Poisson-consistent); neuron 3 averages 6.8 (up to 20) — clearly not Poisson |
| 9 | **112** (degrees) | Population vector decoding of the mystery stimulus from `pop_coding.pickle` |

## Questions 1-2: Entropy and mutual information (worked by hand/computed)

- H(F) for P(F=1)=0.1: **0.4690 bits**
- With P(S=1)=0.1 (flash), P(F=1|flash)=0.5, P(F=1|no flash)=1/18:
  - Overall P(F=1) = 0.5×0.1 + (1/18)×0.9 = 0.1 (same marginal as Q1)
  - Noise entropy = 0.1×H(0.5) + 0.9×H(1/18) = 0.1×1 + 0.9×0.3096 = 0.3786
  - **MI = 0.4690 − 0.3786 = 0.0904 bits**

## Questions 3-6: Sparse coding metaphor (image = Σ aᵢφᵢ + ε, with λ controlling sparsity)

Standard sparse-coding decomposition, matching the Photoshop-layers metaphor in the question:
- **φᵢ (basis functions)** = the reusable shape "stencils" → the pieces that make up the image
- **aᵢ (coefficients)** = how much of each stencil is used → the transparency/opacity of each piece
- **ε (error term)** = how far the reconstruction is from the real image
- **λ** = the penalty weight that trades off accuracy for using fewer active pieces → coding efficiency

## Questions 7-9: Poisson neurons and population coding (cricket cercal system)

**Data:** `tuning.pickle` (4 neurons × 100 trials × 24 stimulus directions, 0–345° in 15° steps)
and `pop_coding.pickle` (responses of the same 4 neurons to one unknown "mystery" stimulus,
plus their 2D basis vectors c1–c4). Code: [analyze.py](../assignments/week4_information_theory/analyze.py).

**Q7 — Tuning curve shape:** Each neuron's mean firing rate vs. stimulus direction rises to a peak,
then falls to **exactly 0 and stays at 0** over roughly half the stimulus range, before rising again —
e.g. neuron 1 peaks at 31.7 Hz at 45°, hits 0 from 135° through 315° (181° span), then climbs
back up. This flat-zero plateau (not a smooth symmetric decay, not negative values, not monotonic)
is the signature of a **half-wave rectified cosine**: `rate = max(0, cos(stimulus − preferred))`.

**Q8 — Which neuron isn't Poisson:** Converting firing rate back to spike counts (rate × 10s) and
computing the Fano factor (variance/mean) per stimulus value:

| Neuron | Mean Fano factor | Range |
|---|---|---|
| 1 | 0.93 | 0.76 – 1.15 |
| 2 | 1.04 | 0.88 – 1.26 |
| 3 | **6.77** | **1.99 – 20.06** |
| 4 | 0.98 | 0.73 – 1.11 |

Neurons 1, 2, 4 sit right around the Poisson signature (Fano factor ≈ 1). **Neuron 3** is wildly
over-dispersed — not Poisson.

**Q9 — Population vector decoding:** Using each neuron's average response to the mystery stimulus,
normalized by its own `r_max` (peak of its tuning curve) and weighted onto its preferred-direction
basis vector, then summed and converted to an angle (0° = north/+y, 90° = east/+x):

```
neuron1: weight=0.389, c=(0.707, 0.707)    [preferred 45°]
neuron2: weight=0.926, c=(0.707, -0.707)   [preferred 135°]
neuron3: weight=0.000, c=(-0.707, -0.707)  [preferred 225°]
neuron4: weight=0.000, c=(-0.707, 0.707)   [preferred 315°]
summed vector = (0.930, -0.379)
angle = 112.19° -> rounded to 112
```

**Answer: 112 degrees**

## Reproduction

```powershell
cd assignments/week4_information_theory
python analyze.py
```

Dataset files (`tuning.pickle`, `pop_coding.pickle`) are not committed (see `.gitignore`); download
from the assignment page if re-running.
