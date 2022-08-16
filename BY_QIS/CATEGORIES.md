#  **Descriptions of QIS Topics**

[![QISCAT_TO_HEP](https://img.shields.io/badge/Link_to-HEP-5BC0EB)](/BY_HEP#readme) ⟵ Click the following for the living review organized by HEP topics  
[![QISCAT_TO_QIS](https://img.shields.io/badge/Link_to-QIS-9BC53D)](/BY_QIS#readme) ⟵ Click the following for the living review organized by QIS topics  
[![QISCAT_TO_MAIN](https://img.shields.io/badge/Link_to-Main-FDE74C)](/../../#readme) ⟵ Click the following to go to the main living review page  

## **Quantum Annealing** [![Papers-quantum-annealing](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_HEP/README.md#quantum-annealing-)
Quantum annealing is a quantum computing method used to solve optimization problems. It is currently the only quantum computing paradigm that enables architectures with large number of qubits, such as D-Wave Systems' Pegasus quantum processor chip with 5000 qubits. The classical counterpart, simulated annealing, mimics the process of heating up a material above its recrystallization temperature then cooled down slowly in order to change the material to a desirable structure. Simulated annealing is capable of finding global extrema as it is able to escape local extrema. The simulated annealing algorithm is as follows: (1) Start with an initial solution $s = s_0$ and an initial temperature $t = t_0$, Let $E(s)$ be the loss function of $s$; (2) Define a temperature reduction scheme. Some examples of temperature reduction schemes are: $t = t - \alpha$, $t = t\alpha$, and $t = \frac{t}{1+\alpha t}$; (3) Starting at $t = t_0$, consider some neighborhood of solution $N(s)$, and pick one of the solutions $s'$; (4) Calculate the difference of the loss function $\delta E$ between the solutions $s$ and $s'$. If $\delta E \geq 0$, accept the new solution. If $\delta < 0$, generate a uniform random number $r$ between 0 and 1. Accept the solution if $r < e^{\frac{\delta E}{t}}$. Note that for large $t$, the probability of selecting $s'$ is high; (5) Repeat steps (3) and (4) for $n$ iterations, updating $t$ given by the temperature reduction rule. \\\\ Quantum annealers solve very specific optimization problems called Quadratic Unconstrained Binary Optimization (QUBO) problems. The QUBO problem consists of finding a binary string that is minimal with respect to a quadratic polynomial over binary variables. The main challenge is to rephrase the loss function to a QUBO problem, which is equivalent to finding the ground state of a corresponding Ising model, whose Hamiltonian is given by $$H(\sigma) = \sum_{i,j=1}^{n}J_{ij} s_i s_j + \sum_{i=1}^{n} h_i s_i$$where $s_i \in \{-1, +1\}$ are the spin values, and $h_i$ and $J_{ij}$ are adjustable constants that represents biases and coupling strengths, respectively. The Hamiltonian of the quantum version of the Ising model, the transverse field Ising model, is given by $$ H_f = \sum_{i,j = 1}^{n}J_{ij}\sigma_{i}^{z}\sigma_{j}^{z} + \sum_{i}^{n}h_i\sigma_{i}^{z} $$where $\sigma_{i}^{z}$ is the Pauli-$Z$ acting on qubit $i$. In quantum annealing, one initializes the system in the ground state of the initial Hamiltonian $H_i$, given by $$ H_i = \sum_{i=1}^{n}\sigma_{i}^{x} $$corresponding to the state $(| 0 \rangle + | 1 \rangle)^{\otimes n}$. The quantum adiabatic theorem states that if the transition between two Hamiltonians is gradual, the system will stay in the ground state. After initializing the system, it slowly evolves by changing the Hamiltonian given by $$ H(t) = \left(1 - \frac{t}{T}\right)H_i + \frac{t}{T} H_f $$where $T$ is the total time in the annealing process. Measuring the final state after the anneal will give the solution to the QUBO problem, since the final system is in an eigenstate of $H_f$. This section reviews papers that involve quantum annealing approaches in particle physics.

## **Variational Quantum Circuits** [![Papers-variational-quantum-circuits](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_HEP/README.md#variational-quantum-circuits-)
To be written

## **Quantum Support Vector Machines** [![Papers-quantum-support-vector-machines](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_HEP/README.md#quantum-support-vector-machines-)
To be written

## **Algorithms Based on Amplitude Amplification** [![Papers-algorithms-based-on-amplitude-amplification](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_HEP/README.md#algorithms-based-on-amplitude-amplification-)
To be written

## **Quantum Walks** [![Papers-quantum-walks](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_HEP/README.md#quantum-walks-)
To be written

## **Continuous Variable Quantum Computing** [![Papers-continuous-variable-quantum-computing](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_HEP/README.md#continuous-variable-quantum-computing-)
To be written

## **Quantum Generative Adversarial Networks** [![Papers-quantum-generative-adversarial-networks](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_HEP/README.md#quantum-generative-adversarial-networks-)
To be written

## **Quantum Circuit Born Machines** [![Papers-quantum-circuit-born-machines](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_HEP/README.md#quantum-circuit-born-machines-)
To be written

## **Quantum-Inspired Algorithms** [![Papers-quantum-inspired-algorithms](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_HEP/README.md#quantum-inspired-algorithms-)
To be written

## **Quantum Simulations** [![Papers-quantum-simulations](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_HEP/README.md#quantum-simulations-)
To be written

## **Quantum Sensors** [![Papers-quantum-sensors](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_HEP/README.md#quantum-sensors-)
To be written

## **Uncategorized by QIS - TEMPORARY** [![Papers-uncategorized-by-qis---temporary](https://img.shields.io/badge/Link_to-Papers-AA96DA)](/BY_HEP/README.md#uncategorized-by-qis---temporary-)
To be written



