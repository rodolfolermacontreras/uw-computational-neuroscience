# Week 6 Quiz: Computing with Networks

Graded assignment covering feedforward filter matrices on images, the assumptions
behind the firing-rate network equation, alpha-synapse dynamics, inhibitory vs.
excitatory reversal potentials, and the steady state of a linear recurrent network.

## Questions 1-4: Feedforward image-processing matrices

The quiz reuses one input image across four questions, each showing a different
processed result and asking which weight matrix `W` produces it. The actual image
file names given to the browser (`q5_pave.jpg`, `q5_paveBlurred.jpg`,
`q5_paveDarkened.jpg`, `q5_paveEdges.jpg`, `q5_pavePixelized.jpg`) directly identify
the operation for each question, in the order they appear on the page:

| Q | Processed image | Operation | Matching matrix |
|---|---|---|---|
| 1 | Blurred | local averaging/smoothing (each pixel mixed with neighbors) | the 0.33 circular-averaging matrix |
| 2 | Darkened | uniform intensity scale-down, no spatial mixing | the diagonal 0.5·I matrix |
| 3 | Edges | derivative/edge filter (each row: +0.75 on diagonal, −0.75 on a neighbor) | the 0.75 / −0.75 matrix |
| 4 | Pixelized | groups of neighboring pixels replaced by one reference pixel's value | the matrix with rows of 1s copying pixel 1 into rows 1-3 and pixel 4 into rows 4-5 |

**Answers:**
- Q1: 0.33 averaging matrix (smoothing/blur)
- Q2: 0.5·I diagonal matrix (uniform darkening)
- Q3: 0.75/−0.75 matrix (edge detector)
- Q4: 1/0 block-replication matrix (pixelization)

## Question 5: Assumptions behind v_ss = F(W·u) (check all that apply)

Deriving the steady-state firing-rate equation from lecture 6.2 requires:
replacing spike trains with instantaneous firing rates (losing timing patterns and
losing synchrony/correlation effects), and assuming static inputs so you can set
dv/dt = 0 and dIs/dt = 0 (losing the time dynamics of convergence).

**Answer (4 of 10 checked):**
- This model ignores patterns in the input and output spike timings, opting instead to simply look at firing rates.
- This model shows us the outputs the system will converge to, but no longer describes the time dynamics of that convergence.
- This model assumes static, unchanging inputs, so it does not account for the dynamics resulting from constantly changing inputs.
- This model ignores the effects of synchrony and correlation between the input neurons.

(Not checked: "no inhibitory synapses", "no differences in input firing rates",
"ignores output firing rates", "ignores input firing rates" — all false, since W
can hold negative weights and u/v are exactly the input/output firing rate
vectors. "Cannot represent refractory period" and "does not account for synaptic
strength" are also false/not applicable here — W explicitly is the synaptic
strength matrix, and refractory-period loss is a property of rate-coding models in
general, not something introduced in this specific 10-minute derivation.)

## Questions 6-8: Alpha-synapse integrate-and-fire neuron (real simulation)

Downloaded and ran the course's own `alpha_neuron.py`
(E_leak=-60mV, V_th=-40mV, E_syn=0mV, same fixed random input spike train,
seed=0). Swept `t_peak` from 0.5 ms to 10 ms in 0.5 ms steps and counted output
spikes — see [sweep_t_peak.py](../assignments/week6_computing_with_networks/sweep_t_peak.py).

| t_peak (ms) | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 | 3.5 | 4.0 | 4.5 | 5.0 | 5.5 | 6.0 | 6.5 | 7.0 | 7.5 | 8.0 | 8.5 | 9.0 | 9.5 | 10.0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| spike count | 0 | 5 | 13 | 15 | 15 | 18 | 21 | 24 | 25 | 27 | 29 | 30 | 31 | 31 | 33 | 33 | 34 | 34 | 35 | 36 |

Firing rate rises quickly over the first half of the range (0.5→5.0 ms: +27
spikes) and much more slowly over the second half (5.0→10.0 ms: +9 spikes) —
diminishing returns, i.e. a **sublinear** relationship.

**Q6 answer:** The neuron's firing rate increases **sublinearly** as a function of t_peak.

**Q7 — why:** A larger `t_peak` means the alpha function decays more slowly after
each input spike (the synaptic conductance lingers longer), so successive input
spikes' conductance "tails" overlap and sum more — more charge flows into the cell
per spike and temporal summation between inputs increases, raising the firing
rate (which saturates/levels off because of the neuron's refractory period and
the fact that the input spike train itself is fixed/finite).

**Answer:** "Increasing the value of t_peak decreases the decay rate of the
synaptic conductance, allowing more charge to flow per spike and increasing the
extent of the summation between input spikes."

**Q8 — turning this synapse inhibitory:** In this model `I_syn = g_syn·(E_syn − V)`.
The synapse is excitatory when its reversal potential `E_syn` is above the resting
potential `E_leak` (default E_syn=0 > E_leak=-60mV, so it always depolarizes).
To make it truly hyperpolarizing/inhibitory, E_syn must be moved **below** the
resting potential E_leak, not just below the spike threshold V_th or below 0 —
either of those leaves E_syn still above E_leak, so the synapse would still
depolarize the cell toward E_syn (just capped below threshold), which is
different from true hyperpolarizing inhibition.

**Answer (check all that apply — only one is correct):** "Changing the value of
E_syn to be less than that of E_leak."

## Question 9: Steady state of a linear recurrent network

Given:
```
W = [[0.6,0.1,0.1,0.1,0.1],
     [0.1,0.6,0.1,0.1,0.1],
     [0.1,0.1,0.6,0.1,0.1],
     [0.1,0.1,0.1,0.6,0.1],
     [0.1,0.1,0.1,0.1,0.6]]

u = [0.6, 0.5, 0.6, 0.2, 0.1]

M = [[-0.125, 0,     0.125, 0.125, 0],
     [0,     -0.125, 0,     0.125, 0.125],
     [0.125,  0,    -0.125, 0,     0.125],
     [0.125,  0.125, 0,    -0.125, 0],
     [0,      0.125, 0.125, 0,    -0.125]]
```

Steady state satisfies `τ dv/dt = -v + Wu + Mv = 0`, i.e. `v_ss = (I - M)^-1 (Wu)`.
Computed exactly in Python — see
[recurrent_network_steady_state.py](../assignments/week6_computing_with_networks/recurrent_network_steady_state.py):

```
h = W.u = [0.5, 0.45, 0.5, 0.3, 0.25]
v_ss    = [0.547, 0.480, 0.543, 0.381, 0.336]
```

**Answer:** v_ss = [0.547, 0.480, 0.543, 0.381, 0.336] — matches exactly one of
the given options.

## Answer summary

| Q | Answer |
|---|---|
| 1 | 0.33 local-averaging matrix (smoothing) |
| 2 | 0.5·I diagonal matrix (darkening) |
| 3 | 0.75/−0.75 edge-detector matrix |
| 4 | 1/0 block-replication matrix (pixelization) |
| 5 | 4 checked: ignores spike timing patterns; shows only converged output, not dynamics; assumes static inputs; ignores synchrony/correlation |
| 6 | Increases sublinearly |
| 7 | Decreases decay rate of synaptic conductance → more charge/spike, more temporal summation |
| 8 | E_syn < E_leak |
| 9 | v_ss = [0.547, 0.480, 0.543, 0.381, 0.336] |
