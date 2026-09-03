# Topics Checklist: Computational Neuroscience

Check items off as I can explain them **without notes**.

---

## Week 1: Introduction and Basic Neurobiology

- [ ] Define what computational neuroscience studies and the questions it asks
- [ ] Describe the anatomy of a neuron: soma, dendrites, axon, synapse
- [ ] Explain the action potential and why it is all-or-nothing
- [ ] Explain synaptic transmission (excitatory vs inhibitory)
- [ ] Describe major brain regions and their functional roles
- [ ] Explain the descriptive / mechanistic / interpretive model distinction

## Week 2: Neural Encoding Models

- [ ] Define a receptive field
- [ ] Define the tuning curve and read one
- [ ] Compute a **spike-triggered average** and explain what it recovers
- [ ] Explain the linear-nonlinear (LN) model structure
- [ ] Explain why a nonlinearity is required after the linear filter
- [ ] Apply spike-triggered covariance to find multiple features
- [ ] Explain feature selection in a neural encoding context

## Week 3: Neural Decoding

- [ ] State the decoding problem as the inverse of encoding
- [ ] Apply signal detection theory: hits, false alarms, ROC curves
- [ ] Explain the relationship between neural discriminability and behavior
- [ ] Apply Bayes rule to decode a stimulus from a response
- [ ] Explain population decoding and population vector coding
- [ ] Explain maximum likelihood decoding

## Week 4: Information Theory and Neural Coding

- [ ] Define entropy and compute it for a discrete distribution
- [ ] Define mutual information and explain what it measures
- [ ] Compute the information carried by a spike train
- [ ] Explain the efficient coding hypothesis
- [ ] Explain why maximizing information is a plausible design principle
- [ ] Explain the bias problem in estimating information from limited data

## Week 5: Computing in Carbon

- [ ] Explain the membrane as an RC circuit
- [ ] Write the **Hodgkin-Huxley** equations and explain each current term
- [ ] Explain the roles of the sodium and potassium channels in a spike
- [ ] Explain the integrate-and-fire model and what it simplifies away
- [ ] Explain dendritic computation and why dendrites are not passive wires
- [ ] Solve or numerically simulate a simple neuron model
- [ ] State clearly what the ML "neuron" abstraction discards

## Week 6: Computing with Networks

- [ ] Explain feedforward network computation in a neural context
- [ ] Explain recurrent network dynamics
- [ ] Explain how recurrent connections produce memory and amplification
- [ ] Explain attractor dynamics at a high level
- [ ] Map biological network concepts onto their ANN counterparts

## Week 7: Networks that Learn: Plasticity and Learning

- [ ] State **Hebb's rule** and its instability problem
- [ ] Explain Oja's rule and what it stabilizes
- [ ] Explain **spike-timing dependent plasticity** (STDP)
- [ ] Explain unsupervised learning in a neural context
- [ ] Explain **sparse coding** and why it is a useful representation
- [ ] Explain **predictive coding** and its relation to modern ML
- [ ] Connect Hebbian learning to PCA

## Week 8: Learning from Supervision and Rewards

- [ ] Derive or explain **backpropagation** in a network
- [ ] Explain why backprop is considered biologically implausible
- [ ] Explain the reinforcement learning problem setup
- [ ] Explain **temporal difference learning** and the TD error
- [ ] Explain the **dopamine reward prediction error** hypothesis
- [ ] Explain the role of the **basal ganglia** in action selection
- [ ] Connect the neuroscience of reward to modern RL algorithms

---

## Cross-cutting outcomes

- [ ] Maintain a running **biology to ML translation table** in this folder
- [ ] Reimplement at least 4 Matlab assignments in Python
- [ ] Read one computational neuroscience paper end to end without stalling
- [ ] Be able to explain to a non-specialist what artificial neural networks got right
      and what they got wrong about real neurons
