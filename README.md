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
| 2 | Neural encoding models | Fairhall | Not started |
| 3 | Neural decoding | Fairhall | Not started |
| 4 | Information theory and neural coding | Fairhall | Not started |
| 5 | Computing in carbon | Fairhall | Not started |
| 6 | Computing with networks | Rao | Not started |
| 7 | Networks that learn: plasticity | Rao | Not started |
| 8 | Learning from supervision and rewards | Rao | Not started |

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
