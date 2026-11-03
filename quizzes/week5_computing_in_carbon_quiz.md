# Week 5 Quiz: Computing in Carbon

Graded assignment covering passive membrane (RC circuit), Hodgkin-Huxley ion channel
gating, the exponential integrate-and-fire model, FitzHugh-Nagumo phase-plane analysis,
and noisy integrate-and-fire spiking.

## Conceptual questions (Q1-10)

1. **Y-axis of a spike plot (x-axis = time):** Voltage
   - A spike is a transient change in membrane *voltage* over time.

2. **Battery / resistor / capacitor analogy:** ion concentration gradient, ion channels, lipid bilayer
   - Battery = electrochemical (ion concentration) gradient driving current.
   - Resistor = ion channels (conductance pathway).
   - Capacitor = lipid bilayer (charge storage across the membrane).

3. **Im+ channel, E=-100 mV, resting=-65 mV, conductance increases:** hyperpolarize, decreasing
   - Opening channels pulls V toward E_Im (-100 mV), which is below rest → hyperpolarizes
     the cell, decreasing membrane potential.

4. **Im+ current with 5 independent subunits (open prob. u) + ball-in-socket gate (open prob. z):**
   I = ḡ·u⁵·z·(V − E)
   - All 5 subunits AND the gate must be open simultaneously (independent probabilities multiply).

5. **Hyperpolarizing step to -75 mV — which reaches new steady state first, m or h:** m
   - Activation (m) kinetics are fast at all voltages; inactivation (h) is slow.

6. **Why can the membrane depolarize past -30 mV (where h∞→0) up to +40 mV during a spike:**
   τ_h is high relative to τ_m, so h does not reach h∞ fast enough to block the spike.
   - m is fast and tracks m∞ almost instantly; h is slow, so during the fast upstroke h
     hasn't had time to inactivate yet — Na+ current persists briefly past -30 mV.

7. **True/False: all neural coding reduces to firing rate ("rate code"):** False
   - Temporal/precise-timing and population codes carry information beyond simple rate.

8. **Exponential integrate-and-fire model — number of stable fixed points:** 1
   - One stable resting fixed point; the "threshold" region is unstable (not stable), and
     above threshold the trajectory diverges (spike), so no additional stable fixed point.

9. **FitzHugh-Nagumo w-nullcline** (dw/dt = bV − cw = 0): w = bV/c

10. **Phase-plane figure — region of the "upstroke":** D
    - System rests at the fixed point (bottom, left branch of the cubic V-nullcline).
      Counterclockwise flow means the first (fast) movement is rightward at ~constant w —
      this horizontal jump from the left branch to the right branch of the cubic happens
      below the hump, in region D. (Then slow rise through B = plateau, fast leftward
      jump through A = downstroke, slow decay through C back to rest.)

## Computational questions (Q11-18) — real code run

Downloaded and ran the course's own Python scripts
(`assignments/week5_computing_in_carbon/membrane.py`, `intfire.py`, `intfire_noise.py`),
Euler method, same parameters given in the quiz.

### Q11 — Passive membrane, steady-state voltage if current is never turned off
C = 0.1 nF, R = 100 MΩ, I = 10 nA → V_steady = I·R = 10 nA × 100 MΩ = **1000** (mV)
(verified against `membrane.py`'s own `V_inf = I*R` line)

### Q12 — Multiply R by 5, does it reach steady state faster or slower?
**More slowly.** τ = RC, so ×5 on R → ×5 on τ.

### Q13 — Divide C by 10, faster or slower?
**More quickly.** τ = RC, so ÷10 on C → ÷10 on τ.

### Q14 — Multiply R by 10 AND divide C by 10, faster/slower/same?
**Same rate.** τ = RC → (×10)·(÷10) = ×1, net no change.

### Q15 — Solution to dV/dt = −V/RC + I/C, V(0)=0
**V(t) = IR(1 − e^(−t/τ))** — the standard RC-charging curve (confirmed Vpeak=IR,
V(τ)=0.6321·IR as stated in the question).

### Q16 — Integrate-and-fire neuron: largest current that fails to cause a spike
Simulated `intfire.py` (R=40 MΩ, C=1 nF, V_th=10 mV, abs_ref=5 ms, tstop=200 ms),
scanning current from 0 up in 1 pA steps:
- First current that spikes: 251 pA
- Largest current that does **not** spike: **250** (pA)
- Matches analytic result: steady state V∞ = I·R must stay below V_th=10mV →
  I < 10 mV / 40 MΩ = 0.25 nA = 250 pA exactly.

### Q17 — Maximum firing rate (continued from Q16)
Ran `intfire.py` with very large I (saturates the response) over the script's default
tstop = 200 ms:
- Spike count plateaus at 34 spikes in 200 ms once I is large enough.
- Max firing rate = 34 spikes / 0.2 s = **170** (Hz)
- (Mechanism: each cycle = 5 ms absolute refractory + 1 ms to re-cross threshold = 6 ms/spike;
  with the 200 ms trial window this gives 34 spikes → 170 Hz. The theoretical
  long-duration-average limit is 1000/6 ≈ 166.67 Hz, but per the question's own
  trial-duration definition — spike count / 200 ms trial — it's 170.)

### Q18 — ISI distribution shape vs. noise amplitude (0-5 nA, I_const=1 nA)
Simulated `intfire_noise.py` logic over long trials for noise amplitudes 0, 0.5, 1, 2, 3, 5 nA:

| noise (nA) | n spikes | ISI mean (ms) | ISI std (ms) | ISI min | ISI max |
|---|---|---|---|---|---|
| 0   | 1333 | 15.00 | 0.00  | 15 | 15  |
| 0.5 | 1338 | 14.94 | 1.85  | 10 | 23  |
| 1   | 1320 | 15.15 | 3.57  | 9  | 33  |
| 2   | 1293 | 15.47 | 6.92  | 7  | 55  |
| 3   | 1294 | 15.45 | 9.59  | 6  | 80  |
| 5   | 1317 | 15.19 | 13.11 | 6  | 110 |

At noise=0 the ISI distribution is a single delta spike (perfectly regular firing).
As noise increases, the distribution broadens strongly to the right (max grows much
faster than the mean) while the minimum ISI stays bounded near the refractory/recharge
time (~6-10 ms) — i.e. it never approaches zero. This is a right-skewed, exponential-like
shape with a lower cutoff, not a symmetric Gaussian.

**Answer: "The distribution of intervals broadens from a single sharp peak to an
exponential-like distribution, but with an avoided range near zero."**

## Answer summary

| Q | Answer |
|---|---|
| 1 | Voltage |
| 2 | ion concentration gradient, ion channels, lipid bilayer |
| 3 | hyperpolarize, decreasing |
| 4 | I = ḡ·u⁵·z·(V−E) |
| 5 | m |
| 6 | τ_h is high relative to τ_m, so h does not reach h∞ fast enough to block the spike |
| 7 | False |
| 8 | 1 |
| 9 | w = bV/c |
| 10 | D |
| 11 | 1000 |
| 12 | More slowly |
| 13 | More quickly |
| 14 | Same rate |
| 15 | V(t) = IR(1 − e^(−t/τ)) |
| 16 | 250 |
| 17 | 170 |
| 18 | Broadens from sharp peak to exponential-like distribution, avoided range near zero |
