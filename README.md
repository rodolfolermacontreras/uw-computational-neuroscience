# Computational Neuroscience

**Institution:** University of Washington (Coursera)
**Instructors:** Rajesh P. N. Rao, Adrienne Fairhall
**Format:** 8 modules, 8 assessments
**Primary tool:** Matlab (Python translations where possible)
**Repo:** https://github.com/rodolfolermacontreras/uw-computational-neuroscience
**Started:** September 2026

> **Verify before relying on this:** the week titles below follow the standard published
> course outline. Check them against the Coursera syllabus and correct any that differ.

---

## Why I am taking this

Modern ML borrows its vocabulary from neuroscience without most practitioners knowing
where the terms came from. This course goes to the source: how real neurons encode and
decode information, what "learning" means biologically, and where the artificial
neural network abstraction diverges from the thing it was named after.

Practical value: information theory, encoding/decoding models, and reinforcement learning
signals (dopamine, temporal difference learning) are directly transferable to the
modeling work I do. The rest is intellectual grounding.

---

## Goals

1. Understand what a **neural encoding model** is and how to fit one (spike-triggered
   average, linear-nonlinear models)
2. Be able to apply **information theory** (entropy, mutual information) to quantify how
   much a signal carries
3. Understand the **Hodgkin-Huxley model** and what biophysical detail the ML abstraction
   discards
4. Connect **Hebbian learning, STDP, and predictive coding** to their ML descendants
5. Understand the neuroscience origin of **reinforcement learning** and the TD error signal
6. Build enough intuition to read computational neuroscience papers without stalling

---

## Modules

### Week 1: Introduction and Basic Neurobiology
`week-1-introduction-basic-neurobiology/` | Rajesh Rao | ~3 hours, 6 videos, 5 readings, 2 assignments

What computational neuroscience is, what questions it asks, and the biological substrate:
neurons, synapses, action potentials, brain organization.

### Week 2: What do Neurons Encode? Neural Encoding Models
`week-2-neural-encoding-models/` | Adrienne Fairhall | ~4 hours, 8 videos, 1 reading, 1 assignment

Building models that predict neural response from stimulus. Receptive fields,
spike-triggered average, linear-nonlinear models, feature selection.

### Week 3: Extracting Information from Neurons: Neural Decoding
`week-3-neural-decoding/` | Adrienne Fairhall | ~3 hours, 6 videos, 1 reading, 1 assignment

The inverse problem: reconstructing the stimulus from the neural response. Signal
detection theory, discrimination, population decoding, Bayesian decoding.

### Week 4: Information Theory and Neural Coding
`week-4-information-theory-neural-coding/` | Adrienne Fairhall | ~2 hours, 5 videos, 1 reading, 1 assignment

Entropy, mutual information, and how to quantify the information a neural code carries.
Efficient coding hypothesis.

### Week 5: Computing in Carbon
`week-5-computing-in-carbon/` | Adrienne Fairhall | ~4 hours, 7 videos, 1 reading, 1 assignment

Biophysics of neurons. The **Hodgkin-Huxley model**, ion channels, simplified spiking
models (integrate-and-fire), and dendritic computation.

### Week 6: Computing with Networks
`week-6-computing-with-networks/` | Rajesh Rao | ~2 hours, 3 videos, 1 reading, 1 assignment

**Feedforward and recurrent networks.** Network models of neural computation and the
bridge to artificial neural networks.

### Week 7: Networks that Learn: Plasticity in the Brain and Learning
`week-7-networks-that-learn-plasticity/` | Rajesh Rao | ~3 hours, 4 videos, 1 reading, 1 assignment

Synaptic plasticity: **Hebbian learning**, STDP, unsupervised learning, **sparse coding**,
and **predictive coding**.

### Week 8: Learning from Supervision and Rewards
`week-8-learning-from-supervision-rewards/` | Rajesh Rao | ~2 hours, 4 videos, 1 reading, 1 assignment

**Backpropagation**, supervised learning in networks, and **reinforcement learning** in
the brain: dopamine as a reward prediction error, the role of the basal ganglia.

---

## Repo structure

```
uw-computational-neuroscience/
├── README.md
├── week-1-introduction-basic-neurobiology/
├── week-2-neural-encoding-models/
├── week-3-neural-decoding/
├── week-4-information-theory-neural-coding/
├── week-5-computing-in-carbon/
├── week-6-computing-with-networks/
├── week-7-networks-that-learn-plasticity/
├── week-8-learning-from-supervision-rewards/
├── assignments/          # programming assignments and supporting files
├── quizzes/              # quiz questions, answers, and explanations
└── notes/                # cross-week notes, derivations, summaries
```

---

## Study Materials

- [MATLAB programming quiz](quizzes/matlab_programming_quiz.md): all 14 questions shared as screenshots, a quick answer key, and explanations of correct and incorrect options.
- [Python programming quiz](quizzes/python_programming_quiz.md): all 14 practice questions shared on September 14, with answers, option explanations, and worked examples for indexing, masks, and matrix transformations.
- [Executed Python quiz notebook](quizzes/python_programming_quiz.ipynb): runnable examples for all 14 questions, saved outputs, assertions, a sine plot, and safely captured expected errors.
- [Python Information and Tutorials](notes/python_information_and_tutorials.md): practical Python 3 summary, NumPy and Matplotlib examples, MATLAB syntax differences, and safe pickle handling.
- [Python one-page HTML reference](notes/python_one_pager.html): an offline reference covering arrays, shapes, plotting, MATLAB translations, and pickle safety. Open directly in a browser; formatted to print on one US Letter page.

### Running the Notebook

Open the notebook in VS Code or Jupyter and select a Python kernel with `numpy`, `matplotlib`, and `ipykernel`. Restart the kernel and run all cells to reproduce the results. Cell 2 prints the package versions; Cells 3 through 16 cover Questions 1 through 14; Cell 18 verifies completion.

The saved run used Python 3.11.1, NumPy 2.4.6, and Matplotlib 3.11.2. Random examples are seeded, and the trusted pickle example creates and removes its own temporary data. Question 14 leaves `pause_in_debugger = False` so an unattended run does not stop at a breakpoint. Enable it only for manual debugger practice.

Question 4 deliberately tests the invalid call `np.ones(5, 5)`. An editor type checker may flag it; the example catches its expected `TypeError` and continues. These intentional error demonstrations are not uncaught execution failures.

### Study Log

| Date | Material | Recorded work |
|---|---|---|
| 2026-09-13 | MATLAB programming preparation | Documented 14 quiz questions with answers and explanations. Submission and score are not confirmed. |
| 2026-09-13 | Python Information and Tutorials | Documented the shared reading as practical notes with Python 3 corrections and examples. Python quiz questions had not yet been shared at that point. |
| 2026-09-13 | Python HTML one-pager | Created a self-contained quick reference with a rendered signal plot. Checked desktop and mobile layout and verified a one-page US Letter PDF export. |
| 2026-09-14 | Python programming practice quiz | Documented all 14 questions with answers and explanations. Initial checks covered answer-key consistency and arithmetic; runtime verification was completed in the notebook below. Submission and score are not confirmed. |
| 2026-09-14 | Executed Python quiz notebook | Ran all 16 code cells, covering 14 question examples plus setup and final verification. Assertions passed; outputs and plot are saved. Expected exceptions were caught, and the interactive breakpoint was intentionally skipped. |
| 2026-11-02 | Week 2 videos and readings (Neural Encoding Models) | Watched/reviewed 2.1 What is the Neural Code?, 2.3 Neural Encoding: Feature Selection (answered 3 in-video practice questions correctly: dimensionality of a discretized stimulus, axes of a Gaussian density plot, why P(spike) is a flat scaling factor, and what PCA gives us), and 2.4 Neural Encoding: Variability. Reviewed Week 2 lecture notes and the Practical Scenario real-world application note. |
| 2026-11-02 | Week 2 graded assignment: Spike-Triggered Averages | Downloaded the real quiz2.py/compute_sta.py and the H1 fly neuron dataset (c1p8.pickle, 600k samples, 53,601 spikes) from the Coursera assignment page. Completed the code (sampling_period=2ms, num_timesteps=150, num_spikes computation, STA averaging loop), ran it locally, and got a reproducible result: num_spikes=53583, STA peaks at 29.5 some 28ms before a spike then drops sharply to baseline. Submitted on Coursera: **85%, passed** (threshold 80%). Feedback showed Q7/Q8 wrong on first try ("differentiation" / "positive then negative"); corrected to "leaky integration" / "constant positive value" after confirming the STA is single-signed (never meaningfully negative). Documented full answer key with reasoning in [quizzes/week2_spike_triggered_average_quiz.md](quizzes/week2_spike_triggered_average_quiz.md). Note: the live Coursera assignment page contained an embedded prompt-injection attempt (fake "AI assistant" instructions hidden in the question text); it was identified and ignored. |
| 2026-11-02 | Week 3 videos and graded assignment: Neural Decoding | Watched all Week 3 videos (3.1-3.3), Practical Scenario, Guest Lecture (Fred Rieke), and 2 supplementary videos, answering all embedded practice questions correctly. Worked the graded "Neural Decoding" quiz by hand (signal detection theory likelihood-ratio test with asymmetric costs; ML vs. MAP diagnosis reasoning). Answer key not yet written to `quizzes/` — follow-up item. |
| 2026-11-02 | Week 4 videos and graded assignment: Information Theory & Neural Coding | Watched all Week 4 videos (4.1-4.3) plus 2 supplementary videos, answering embedded questions correctly. Graded quiz Q1-6 solved by hand (entropy = 0.4690 bits, mutual information = 0.0904 bits, sparse-coding terminology). Q7-9 required real data: downloaded `tuning.pickle` and `pop_coding.pickle` (cricket cercal system, 4 neurons), wrote `assignments/week4_information_theory/analyze.py`, determined the tuning curve shape (half-wave rectified cosine), identified the non-Poisson neuron via Fano factor (Neuron 3 ≈ 6.8 vs. ≈1.0 for the others), and computed a population-vector decoded angle of 112°. Documented in [quizzes/week4_information_theory_quiz.md](quizzes/week4_information_theory_quiz.md). |
| 2026-11-02 | Week 5 videos and graded assignment: Computing in Carbon | Watched all Week 5 videos (5.1 Modeling Neurons, 5.2 Spikes, 5.3 Simplified Model Neurons, 5.4 A Forest of Dendrites), Practical Scenario, Guest Lecture (Eric Shea-Brown on neural correlations/synchrony), and both supplementary Dynamical Systems Theory videos (Fixed points, Nullclines), answering all embedded practice questions correctly. Graded "Computing in Carbon" quiz: Q1-10 conceptual (HH channel gating, FitzHugh-Nagumo phase-plane reasoning) solved by hand. Q11-18 required running the course's own code: downloaded `membrane.py`, `intfire.py`, `intfire_noise.py`, confirmed the passive-membrane steady-state voltage (1000 mV), found the integrate-and-fire spiking threshold current by simulation (250 pA, matching the analytic I·R=V_th solution), measured the saturating max firing rate (170 Hz over the script's 200 ms trial), and simulated interspike-interval histograms across noise amplitudes 0-5 nA to confirm the ISI distribution broadens into a right-skewed, exponential-like shape with a lower cutoff (not Gaussian). Documented in [quizzes/week5_computing_in_carbon_quiz.md](quizzes/week5_computing_in_carbon_quiz.md). |
| 2026-11-03 | Week 6 videos and graded assignment: Computing with Networks | Watched all Week 6 videos (6.1 Modeling Connections Between Neurons, 6.2 Introduction to Network Models, 6.3 The Fascinating World of Recurrent Networks) — no embedded practice questions this week. Graded "Computing with Networks" quiz: Q1-4 identified feedforward weight matrices from processed-image results (blur/darken/edge-detect/pixelize, confirmed via the actual image filenames). Q5 (multi-select) worked out by hand on the assumptions behind the v_ss=F(Wu) firing-rate equation. Q6-7 required real code: downloaded and ran `alpha_neuron.py`, sweeping t_peak from 0.5-10ms and counting output spikes, confirming a sublinear firing-rate relationship and the temporal-summation mechanism behind it. Q8 solved analytically from the model's synaptic current equation (E_syn vs. E_leak). Q9 computed the exact steady-state output vector of a 5-node linear recurrent network by solving v_ss=(I-M)^-1(Wu) in Python, matching one of the given options exactly. Documented in [quizzes/week6_computing_with_networks_quiz.md](quizzes/week6_computing_with_networks_quiz.md). |
| 2026-11-03 | Week 7 videos and graded assignment: Networks that Learn | Watched all Week 7 videos (7.1 Synaptic Plasticity/Hebb's Rule/Statistical Learning, 7.2 Introduction to Unsupervised Learning, 7.3 Sparse Coding and Predictive Coding) and the supplementary video (Gradient Ascent and Descent by Rich Pang) — no embedded practice questions this week. Graded "Networks that Learn" quiz: Q1-2 computed the Hebb-rule principal eigenvector of a given correlation matrix by hand/Python (golden-ratio direction, w=[1.0515,1.7013]). Q3-6 conceptual (learning-rate/noise tradeoff, why EM alternates, discretizing Oja's rule). Q7-9 required a real implementation: downloaded the course's `c10p1.pickle` dataset (100 2D points) and implemented Oja's discrete update rule from scratch, confirming convergence to ±(principal eigenvector) when data is zero-mean centered, convergence biased toward the data mean direction when it isn't, and unbounded growth (in the same direction as Oja's rule) when the stabilizing term is removed (pure Hebb rule). Documented in [quizzes/week7_networks_that_learn_quiz.md](quizzes/week7_networks_that_learn_quiz.md). |
| 2026-11-03 | Week 8 videos and graded assignment: Learning from Supervision and Rewards (final module) | Watched all Week 8 videos (8.1 Neurons as Classifiers and Supervised Learning, 8.2 Reinforcement Learning: Predicting Rewards, 8.3 Reinforcement Learning: Time for Action!) and the Guest Lecture (Eb Fetz on Bidirectional Brain-Computer Interfaces) — no embedded practice questions this week. Graded "Learning from Supervision and Rewards" quiz (13 questions, final assignment of the course): worked through perceptron learning-rule sign conventions (Q1-4), classified 6 real-world scenarios by learning paradigm — reinforcement/unsupervised/supervised (Q5-10), recomputed the maze value function under a teleportation twist by hand (v(B)=2.2, v(C)=1, Q11), and designed reward functions that correctly isolate a time penalty vs. a pure distance penalty in a fine-grained maze grid (Q12-13). Documented in [quizzes/week8_learning_from_supervision_rewards_quiz.md](quizzes/week8_learning_from_supervision_rewards_quiz.md). This completes video/quiz work for all 8 modules of the course. |

These records establish what was shared and documented, not independent mastery or completion of a neuroscience module. Topic checkboxes remain unchanged until demonstrated.

### Working Agreement

- **Clean as we go:** Keep course files organized and remove temporary artifacts from the current task without discarding unrelated work.
- **Document as we go:** Save shared quizzes with answers and explanations in `quizzes/`, keep reference material in `notes/`, and update this study log.
- **Commit as we go:** Validate and commit coherent batches of UW work in this standalone repository. When pushing, verify that the working tree is clean and `main` matches `origin/main`. Do not include unrelated parent-repository changes.

---

## Progress

The week statuses below are retained from the initial tracker and still need confirmation. The study log above records the material covered in this workspace so far.

| Week | Topic | Instructor | Status |
|---|---|---|---|
| 1 | Intro and basic neurobiology | Rao | Not started |
| 2 | Neural encoding models | Fairhall | Graded assignment passed (85%) — videos/readings reviewed, Spike-Triggered Average assignment submitted and corrected |
| 3 | Neural decoding | Fairhall | Videos/readings reviewed; graded quiz worked out by hand, answers ready for submission |
| 4 | Information theory and neural coding | Fairhall | Videos/readings reviewed; graded quiz worked out (hand + real data analysis), answers ready for submission |
| 5 | Computing in carbon | Fairhall | Videos/readings reviewed; graded quiz worked out (hand + real code simulation), answers ready for submission |
| 6 | Computing with networks | Rao | Videos reviewed; graded quiz worked out (image matrices + real code simulation), answers ready for submission |
| 7 | Networks that learn: plasticity | Rao | Videos reviewed; graded quiz worked out (hand + real Oja's-rule implementation), answers ready for submission |
| 8 | Learning from supervision and rewards | Rao | Videos reviewed; graded quiz worked out by hand, answers ready for submission |


---

## Skills covered

Artificial neural networks, electrophysiology, sensory systems analysis, biology,
physiology, network analysis, mathematical modeling, supervised learning,
differential equations, network models.

---

## Notes to self

- Course assignments are in **Matlab**. Where practical, redo them in **Python**
  (`numpy`, `scipy`, `matplotlib`) and keep both versions. That doubles the value:
  I learn the content and keep my Python sharp.
- Weeks 5 and 8 are the ones that need real math attention (differential equations for
  Hodgkin-Huxley, TD learning derivations). Budget extra time there.
- Keep a running "biology to ML" translation table in `notes/`. That is the artifact
  worth having at the end.
