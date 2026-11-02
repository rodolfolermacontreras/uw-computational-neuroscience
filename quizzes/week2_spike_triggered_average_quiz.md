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

**Submitted score: 85% (passing threshold 80%).** Coursera's per-question feedback
confirmed Q1–6 and Q9 correct; **Q7 and Q8 were marked wrong on the first submission**
(both "Differentiation" / "positive then negative"). Corrected below with the reasoning
that was missing the first time, and verified against the actual STA data (it is **never
meaningfully negative** — min −0.36 vs. peak +29.5, i.e., noise floor, not a real trough).

| Question | Answer | Basis | Result |
|---|---|---|---|
| 1 | `y(t) = cos[x(t-θ)]` is **not** linear | Only option where the output is a nonlinear function of the input | ✅ 1/1 |
| 2 | The stimuli preceding a spike, averaged over all stimuli that elicited a spike | Standard definition; matches lecture 2.3 | ✅ 1/1 |
| 3 | `sampling_period = 2` (ms) | 1000 ms / 500 Hz = 2 ms | ✅ 2/2 |
| 4 | `num_timesteps = 150` | 300 ms window / 2 ms per sample = 150 | ✅ 2/2 |
| 5 | `num_spikes = 53583` | Computed from data (53,601 total − 18 within the first 300 ms) | ✅ 5/5 |
| 6 | The plot that ramps up slowly, peaks sharply ~28 ms before the spike, then drops straight back to baseline (no sustained negative undershoot) | Matches our actual computed STA, see `sta_plot.png` | ✅ 5/5 |
| 7 | ~~Differentiation~~ → **Leaky integration** | The STA is single-signed (always ≥ ~0); a true derivative/differentiator needs a biphasic (positive-then-negative) kernel, which is absent here | ❌→fixed (was 0/2) |
| 8 | ~~A positive value followed by a negative value~~ → **A constant positive value** | The kernel is uniformly positive, so a sustained positive stimulus maximizes overlap with it; an alternating stimulus would partly cancel against a filter with no negative lobe | ❌→fixed (was 0/1) |
| 9 | Principal component analysis / covariance analysis | Explicitly the method taught in lecture 2.3 for multi-feature neurons | ✅ 1/1 |

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

**First submission answered "Differentiation" — marked wrong (0/2).** On reflection, a true
differentiator requires a **biphasic** kernel: a positive lobe immediately followed by a
comparably-sized **negative** lobe (sign reversal), because the derivative of a signal that
goes up then down is positive then negative. Checking the actual computed STA values: the
minimum across the whole 300 ms window is **−0.36**, compared to a peak of **+29.5** — that
"negative" tail is noise floor, not a real trough. The STA is **single-signed**: it is
indistinguishable from zero over most of the window, rises to one broad positive peak around
28 ms before the spike, and falls back toward zero — but never goes meaningfully negative.
That one-sided, broad, rise-and-decay shape (no sign reversal) is the signature of **leaky
integration**, not differentiation. Running average/sum would be flatter with less sharp
structure, and "no response" is clearly wrong given the large, consistent peak.

**Corrected answer: Leaky integration.**

## Question 8: Preferred stimulus pattern

**First submission answered "a positive value followed by a negative value" — marked wrong
(0/1).** That answer assumed the differentiator interpretation from Q7, which was incorrect.
Since the kernel (STA) is uniformly non-negative across the whole window — there is no
negative lobe to multiply against a negative stimulus segment — the response (a convolution
of the stimulus with this all-positive kernel) is maximized by a stimulus that stays positive
throughout the entire window, not one that flips sign.

**Corrected answer: A constant positive value.**

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
