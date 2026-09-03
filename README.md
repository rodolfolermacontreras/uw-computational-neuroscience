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
├── assignments/          # graded quizzes and programming assignments
└── notes/                # cross-week notes, derivations, summaries
```

---

## Progress

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
