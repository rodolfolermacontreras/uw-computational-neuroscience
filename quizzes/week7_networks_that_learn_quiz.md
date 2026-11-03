# Week 7 Quiz: Networks that Learn

Graded assignment covering Hebbian learning, Oja's rule, learning-rate behavior,
the EM algorithm, and a hands-on implementation of Oja's rule on a real 2D
dataset (with and without zero-mean centering, and with/without the
stabilizing subtractive term).

## Question 1: Final weight vector under the Hebb rule

Given correlation matrix `Q = [[0.2, 0.1], [0.1, 0.3]]`, the Hebb-rule weight
vector converges in *direction* to the principal eigenvector of `Q` (largest
eigenvalue). Computed exactly in Python:

```
eigenvalues: [0.1382, 0.3618]
principal eigenvector (λ=0.3618): [0.5257, 0.8507]  (ratio v2/v1 = 1.618, golden ratio)
```

Checking each answer option's ratio `w2/w1`:
- [0.8944, 1.7889] → ratio 2.0 ✗
- [-1.5155, -1.3051] → ratio 0.861 ✗
- [-1.5764, -1.2308] → ratio 0.781 ✗
- [1.0515, 1.7013] → ratio 1.618 ✓ (matches principal eigenvector direction exactly; length 2.0 = 1/√(0.25), consistent with Oja's-rule-style convergence)

**Answer: w = [1.0515, 1.7013]**

## Question 2: What does that weight vector tell us?

None of the listed claims hold: the vector's direction/length come from the
principal eigenvector and the Oja normalization constant, not from the input
mean being (0,0) (Q is given directly as a correlation matrix — nothing here
establishes the actual data mean), not from any specific τ_w (τ_w only
controls convergence *speed*, not the converged value), and the synapse is
growing (LTP-like), not undergoing depression.

**Answer: None of these options**

## Question 3: Learning rate and noise sensitivity (check all that apply)

A higher learning rate weights each new (possibly noisy) data point more
heavily in the running update, making the estimate jumpier/more
noise-sensitive. A constant (non-decaying) learning rate keeps the estimate
responsive to new data indefinitely (vs. a 1/T schedule that eventually stops
adapting).

**Answer (2 checked):**
- A higher learning rate makes the parameter estimate more influenced by noise during online estimation.
- A constant learning rate allows the parameter estimate to remain sensitive to new data.

## Question 4: Why does EM alternate between E and M steps?

The two parameter sets are mutually dependent, so they can't be solved
independently in one shot — but EM is only guaranteed to improve (or hold) the
objective each iteration, not to find the global optimum (it can get stuck in
local optima depending on initialization).

**Answer:** "We need the alternating steps because the two sets of parameters
are mutually dependent on each other, necessitating that they be optimized
together. This is justified by the fact that these algorithms will always
attempt to move towards a better solution with each iteration."

## Questions 5-6: Discretizing Oja's rule

Continuous Oja's rule: `τ_w dw/dt = v·u − α·v²·w`, with `η = 1/τ_w`.

- Discrete-time form: **Δw = Δt·η·(v·u − α·v²·w)** (needs both the `Δt` step
  size and the `η` rate constant — options missing either are wrong).
- Discrete update rule: **w_{i+1} = w_i + Δt·η·(v·u − α·v²·w_i)**

## Questions 7-9: Real implementation of Oja's rule (c10p1 dataset)

Downloaded `c10p1.pickle` (100 2D points, Dayan & Abbott textbook exercise set)
and implemented the discrete update rule exactly as derived in Q5/Q6
(η=1, α=1, Δt=0.01, random initial w, 100,000 iterations, cycling through the
100 points) — see
[oja_rule.py](../assignments/week7_networks_that_learn/oja_rule.py).

**Q7 — mean-centered data:** After subtracting the data mean, the
covariance/correlation matrix has eigenvalues **[0.583, 0.065]**, with
principal eigenvector **[0.710, −0.704]** (length 1). Running the Oja update
from 5 different random initial weight vectors:

```
seed=0: w = [ 0.709, -0.705], |w| = 1.000
seed=1: w = [-0.709,  0.705], |w| = 1.000
seed=2: w = [ 0.709, -0.705], |w| = 1.000
seed=3: w = [ 0.709, -0.705], |w| = 1.000
seed=4: w = [-0.709,  0.705], |w| = 1.000
```

`w` always converges to the principal eigenvector direction, scaled to length
1/√α = 1 — but the *sign* (±) depends on the random initialization, i.e. `w`
converges to one of exactly two possible vectors (parallel, opposite signs).

**Answer:** "The correlation matrix has only one principal eigenvector, but
there are two vectors of length 1/√α that are parallel to this eigenvector.
w can converge to either of these two vectors."

**Q8 — data not zero-mean centered:** Shifted the data to means (3,3) and
(−2,5) and reran:

```
shift=(3,3):  w converges to ±[0.555, 0.833] (56.3°) vs. mean direction 45.0°
shift=(-2,5): w converges to ±[0.441,-0.898]/[-0.441,0.898] (-63.9°/116.1°) vs. mean direction 111.8°
```

In both cases the converged direction is clearly different from the
zero-mean-centered result ([0.710,−0.704], Q7), and it lands roughly (not
exactly) along the direction pointing toward the new data mean — confirming
the mean term is no longer being "subtracted out," so it now dominates/biases
the direction `w` settles into.

**Answer:** "The two vectors that w converges to in different runs of the
algorithm are parallel to the vector that points roughly towards the mean of
the data."

**Q9 — pure Hebb rule (drop the −αv²w term), mean-centered data:**

```
n_iter=2000:  w ≈ ±[14266, -14177],  |w| ≈ 2.0e4   (ratio w2/w1 ≈ -1.006)
n_iter=20000: w ≈ ±[3.46e49, -3.44e49], |w| ≈ 4.9e49 (same ratio ≈ -1.006)
```

The direction (ratio ≈ −1.006) matches the same principal-eigenvector
direction found with Oja's rule in Q7 ([0.709,−0.705], ratio ≈ −1.006) — but
the magnitude explodes from ~2×10⁴ at 2,000 iterations to ~5×10⁴⁹ at 20,000
iterations, i.e. unbounded growth, exactly the instability predicted
analytically in lecture 7.1 (no −αv²w term to cap ‖w‖).

**Answer:** "The vectors found by the learning rule have the same direction as
those found by Oja's rule, but the length grows without bound as a function of
the number of iterations."

## Answer summary

| Q | Answer |
|---|---|
| 1 | w = [1.0515, 1.7013] |
| 2 | None of these options |
| 3 | Check: higher learning rate → more noise-influenced; constant learning rate → stays sensitive to new data |
| 4 | Mutually dependent parameters, justified by monotonic improvement (not guaranteed global optimum) |
| 5 | Δw = Δt·η·(vu − αv²w) |
| 6 | w_{i+1} = w_i + Δt·η·(vu − αv²w_i) |
| 7 | Converges to ±(principal eigenvector, length 1/√α) |
| 8 | Converges roughly toward the (nonzero) data mean direction |
| 9 | Same direction as Oja's rule, but length grows without bound |
