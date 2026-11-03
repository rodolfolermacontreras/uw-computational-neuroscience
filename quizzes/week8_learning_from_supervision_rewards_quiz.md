# Week 8 Quiz: Learning from Supervision and Rewards (Final Module)

Graded assignment covering supervised vs. unsupervised vs. reinforcement learning,
the perceptron learning rule, learning-rate annealing, and reward-function design
for a maze reinforcement-learning problem (including a teleportation variant and
time-vs-distance penalty shaping).

## Question 1: Supervised vs. unsupervised learning (check all that apply)

- In supervised learning, both inputs AND the correct/desired outputs are
  provided to the network (that's what makes it "supervised").
- In unsupervised learning, only inputs are provided — no correct outputs.

**Answer (3 of 4 checked):**
- In supervised learning, correct outputs are provided to the network.
- In unsupervised learning, inputs are provided to the network.
- In supervised learning, inputs are provided to the network.

(Not checked: "In unsupervised learning, correct outputs are provided to the
network" — false, that would make it supervised.)

## Question 2: Perceptron output sign (check all that apply)

w₁=1, w₂=3, threshold μ=0. Output is positive when `u₁·1 + u₂·3 > 0`:

| [u₁, u₂] | u₁+3u₂ | positive? |
|---|---|---|
| [-1, 1]  | -1+3 = 2   | **yes** |
| [1, 1]   | 1+3 = 4    | **yes** |
| [-1, -1] | -1-3 = -4  | no |
| [1, -1]  | 1-3 = -2   | no |

**Answer (2 checked):** [-1, 1] and [1, 1]

## Question 3: Perceptron weight/threshold update (check all that apply)

Input pattern u=[+1,-1,-1,+1,-1], perceptron output v=+1 but desired v_d=-1
→ error = v_d − v = −2 (negative).

Update rules (from lecture 8.1): Δw_i = ε(v_d−v)u_i, and the threshold
decreases when the error is positive / increases when the error is negative.

- w₃: u₃ = −1, so Δw₃ = ε·(−2)·(−1) = +2ε > 0 → **w₃ should increase**
- Error is negative → **threshold should increase**

**Answer (2 checked):** w₃ should increase; the threshold should increase.

## Question 4: Avoiding oscillation in perceptron learning

With a fixed positive learning rate the perceptron can bounce around the
optimum forever instead of settling. The standard fix is to anneal
(gradually shrink) the learning rate over training passes.

**Answer:** "In each pass through the dataset, divide the learning rate by a
value greater than 1."

## Questions 5-10: Which learning paradigm fits each scenario?

| Q | Scenario | Answer |
|---|---|---|
| 5 | Chess agent, no expert, feedback only win/loss at game end | **Reinforcement** |
| 6 | Robot pouring milk, "good/bad robot" feedback + reward at completion | **Reinforcement** |
| 7 | Disease outbreak, only case locations known, want to find outbreak clusters | **Unsupervised** |
| 8 | Reduce 1M-pixel car images to simple color-balance features, no labels | **Unsupervised** |
| 9 | Disease outbreak with full labeled patient histories + soda consumption, estimate the connection | **Supervised** |
| 10 | Car images labeled "red car"/"blue car", build a system to label new images | **Supervised** |

## Question 11: Maze value with a teleportation twist

Baseline (from lecture 8.3): v(B) = 0.5×0 + 0.5×5 = 2.5; v(C) = 0.5×0 + 0.5×2 = 1.

New rule: on arriving at B, 20% of the time the rat is teleported to C instead
(then follows C's normal process); 80% of the time B proceeds normally.
C's own process is unchanged, so v(C) stays 1.

```
v(B)_new = 0.8 × (0.5×5 + 0.5×0) + 0.2 × v(C) = 0.8×2.5 + 0.2×1 = 2.0 + 0.2 = 2.2
v(C)_new = 1   (unchanged — C's transitions were not altered)
```

**Answer:** v(B) = 2.2; v(C) = 1

## Question 12: Reward function that penalizes TIME taken (check all that apply)

Extending the maze to a fine grid where the rat can move step-by-step or
rest, a true *time* penalty must apply to every time step regardless of
whether the rat moves or rests (resting still costs time).

- "Using a reward function defined over only states, set R equal to some
  negative constant r_penalty for all states, excluding the final states...":
  applies the penalty to every time step no matter the action (including
  resting) → **correct, this is a time penalty**.
- "Set R equal to some negative constant r_penalty for all states and actions
  excluding the final states, which will remain as they are marked in the
  maze for all actions": same effect, defined over state-action pairs instead
  of states alone, but penalty still applies to every action including
  resting → **also correct**.
- "Subtract some amount from each final state proportional to its distance
  from the maze entrance": distance-based, not time-based, and doesn't
  penalize resting/dawdling → **not correct** for a time penalty.
- "Set a penalty at B and C proportional to the sum of their distance from A
  and the neighboring final states": also distance-based, applied only at
  specific states → **not correct**.

**Answer (2 checked):**
- Using a reward function defined over only states, set R equal to some
  negative constant r_penalty for all states, excluding the final states,
  which will remain as they are marked presently.
- Set R equal to some negative constant r_penalty for all states and actions
  excluding the final states, which will remain as they are marked in the
  maze for all actions.

## Question 13: Reward function that penalizes DISTANCE instead of TIME

Now the rat can rest anywhere for free, and we want to penalize only actual
movement (distance), not time spent resting. The only option that excludes
resting from the penalty (giving it 0 reward) while still penalizing every
movement action is the right one — it directly decouples "distance traveled"
from "time taken."

**Answer:** "Set R equal to some negative constant r_penalty for all states
and all actions excluding resting, which will have a 0 reward. The final
states will remain as they are marked in the maze for all actions."

## Answer summary

| Q | Answer |
|---|---|
| 1 | Check: supervised→correct outputs provided; unsupervised→inputs provided; supervised→inputs provided |
| 2 | Check: [-1, 1] and [1, 1] |
| 3 | Check: w₃ should increase; threshold should increase |
| 4 | Divide the learning rate by a value > 1 each pass (anneal it) |
| 5 | Reinforcement |
| 6 | Reinforcement |
| 7 | Unsupervised |
| 8 | Unsupervised |
| 9 | Supervised |
| 10 | Supervised |
| 11 | v(B) = 2.2; v(C) = 1 |
| 12 | Check: the two "penalty for all states/actions excluding final states" options |
| 13 | Penalty for all states/actions excluding resting (resting = 0 reward) |
