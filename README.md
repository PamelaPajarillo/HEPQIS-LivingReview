#  **A Living Review of Quantum Information Science in Particle Physics**

*Inspired by "A Living Review of Machine Learning for Particle Physics", the goal of this repository is to provide an extensive list of citations for those developing and applying quantum information approaches to experimental, phenomenological, or theoretical analyses.  Applications of quantum information science to high energy physics is a relatively new field of research.  This repository will be updated as often as possible with the relevant literature.  Suggestions are most welcome.*

The goal of this repository is to collect references for quantum information science as applied to particle and nuclear physics.  

##  **Reviews**

<details>
<summary> <a href="https://arxiv.org/abs/2005.08582"> Quantum Machine Learning in High Energy Physics</a> [<a href="https://doi.org/10.1088/2632-2153/abc17d">DOI</a>]</summary>

This review presents papers using quantum machine learning (QML) to perform classification with quantum annealing, restricted Boltzmann machines, quantum graph networks and variational quantum circuits. One of the main challenges of quantum annealing is its restrictive formulation (i.e rephrasing the loss function into a Quadratic Unconstrained Binary (QUBO) problem). Quantum-circuit-based machine learning is still at limited performance because of quantum device limitations. This review also discusses implementing QML directly on quantum data and practical considerations of experimenting with quantum annealers and quantum circuits.

</details>



##  **Quantum Machine Learning**



###  **Quantum Annealing**

<details>
<summary> <a href="https://doi.org/10.1038/nature24047"> Solving a Higgs optimization problem with quantum annealing for machine learning</a></summary>

Using D-Wave's programmable quantum annealer, this paper explores quantum annealing for machine learning (QAML). The paper shows that quantum and classical annealing-based classifiers perform comparably with no clear advantage to traditional machine learning methods, including deep neural network (DNN) and an ensemble of boosted decision trees (BDTs), to solve a Higgs signal-background discrimination machine learning optimimzation problem, which identifies features from a pair of photons correspond to a decay from the Higgs or other Standard Model processes. The inputs of the weak binary classifiers are the encoded transverse momentum of photons and the correlations between the two photons. The strong classifier is then constructed from a linear combination of weak classifiers, where the weights are obtained through an optimization problem, which must have a mapping to a quadratic unconstrained binary optimization (QUBO) problem. This classifier is resistant to overfitting, since due to noise, the D-Wave quantum annealer will avoid the global minimum of the loss functional, and it has a slight advantage over BDT and DNN with a smaller training dataset.

</details>

<details>
<summary> <a href="https://arxiv.org/abs/1908.04480"> Quantum adiabatic machine learning with zooming</a> [<a href="https://doi.org/10.1103/PhysRevA.102.062405">DOI</a>]</summary>

Inspired by quantum annealing for machine learning (QAML), which constructs a strong classifier from a linear combination of weak binary classifiers. this paper proposes a variant called QAML-Z, where the binary classifiers are modified to continuous real values by performing a search on the real numbers. This works by zooming into a region of the energy surface and iteratively perform quantum annealing to an augmented set of weak classifiers, which then makes a strong classifier. The iteration rule that gives the weight of each classifier consists of shifting the value of mean based on the spin of the qubit then narrowing the search breadth. The zooming algorithm increases the probability of overfitting, so the authors of the paper propose regularizing the iterative process by applying a bit flip between each iteration with monotonically decreasing probability. This effectively prevents the strong classifier from overfitting and overcomes getting out of a local minima. The QAML-Z algorithm is applied to the Higgs optimization problem, where features of a diphoton event must be identified in order to classify events as a Higgs decay or other Standard Model processes. QAML-Z does not show an obvious advantage over traditional machine learning methods, including deep neural networks (DNNs) and boosted decision trees (BDTs), however, its performance surpasses the QAML algorithm and simulated annealing with zooming.

</details>



###  **Quantum Circuits**

<details>
<summary> <a href="https://arxiv.org/abs/2012.11560"> Application of quantum machine learning using the quantum variational classifier method to high energy physics analysis at the LHC on IBM quantum computer simulator and hardware with 10 qubits</a> [<a href="https://doi.org/10.1088/1361-6471/ac1391">DOI</a>]</summary>

Using IBM gate-based quantum computers, the quantum variational classifier method is applied to the $t\bar{t}H$ (examines the Higgs coupling to the top quark) and $H\rightarrow\mu\mu$ (examines the Higgs coupling to second-generation fermions) analyses, with the goal of classifying physics events of interest from background events. Using event generators to produce signal and background events for $t\bar{t}H$ and $H\rightarrow\mu\mu$, a Principal Component Analysis (PCA) method converts kinematic variables to a smaller amount of variables so that the number of encoded variables is equal to the number of available qubits. Then, a feature map circuit which encodes the input data $\vec{x}$ into a quantum state is applied. A quantum variational circuit $W(\vec{\theta})$ which is parametrized by gate angles $\vec{\theta}$ is then applied. Finally, the qubit state is measured in the computational basis and the output state is classified as either signal or background through the action of a diagonal operator in the standard basis. To train the quantum variational circuit $W(\vec{\theta})$ for the optimized parameters $\vec{\theta}$, a set of input data and its labels are used. With 100 training events, 100 test events, and 10 encoded variables, the AUC of IBM’s quantum computer simulator that includes a noise model with 10 qubits are similar to the AUC of a classical support vector machine (SVM) and a boosted decision tree (BDT) classifier. The quantum variational classifier is then employed on two of IBM’s quantum computers, and the results show that the quantum computer and quantum simulator are in good agreement, however, the run time on the quantum computer is longer than the classical machine learning algorithms due to the limitations in quantum hardware. The paper concludes by stating that the use of quantum machine learning could potentially offer a “speed up” advantage with the rapid advances in quantum computing technology.

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2104.05059"> Application of quantum machine learning using the quantum kernel algorithm on high energy physics analysis at the LHC</a> [<a href="https://doi.org/10.1103/PhysRevResearch.3.033221">DOI</a>]</summary>

To classify signal and background events in the $t\bar{t}H$ analysis, the use of a support vector machine (SVM) with a quantum kernel estimator (QSVM-Kernel) is explored. A major limitation of the classical SVM is evaluating the similarity between any two data points in a large feature space is computationally expensive. The QSVM-Kernel algorithm exploits the quantum state space as a direct representation of the feature space, which gives rise to kernel functions that are hard to calculate classically, but are efficiently evaluated using quantum kernels. The QSVM-Kernel algorithm is the following: (1) Using a Quantum Feature Map function, map classical data to a quantum state; (2) Calculate the similarity between any two data points using a quantum computer; and finally (3) To find the separate hyperplane, use the kernel entries. This algorithm is then applied to separate between $t\bar{t}H$ (signal) and non-resonant di-photons (background). The quantum simulators used in this paper are from IBM, Google, and Amazon, all of which model the noiseless execution of their respective quantum computer hardware. The performance of these quantum simulators, using 15 qubits and 60 independent datasets of 20000 training events and 20000 testing events, are similar to the performance of a classical SVM and a classical BDT. The QSVM-Kernel algorithm is then implemented on IBM’s quantum processor. The mean performance of QSVM-Kernel on IBM’s quantum processor and IBM’s quantum computer simulator is about 5\% lower. This difference is expected due to hardware noise. The results on IBM’s quantum processor does approach the performance of IBM’s quantum computer simulator. The paper concludes that the running time is expected to be reduced with improved quantum hardware and predicts that quantum machine learning could potentially become a powerful tool for HEP data analyses.

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2104.05059"> Application of quantum machine learning using the quantum kernel algorithm on high energy physics analysis at the LHC</a> [<a href="https://doi.org/10.1103/PhysRevResearch.3.033221">DOI</a>]</summary>

To classify signal and background events in the $t\bar{t}H$ analysis, the use of a support vector machine (SVM) with a quantum kernel estimator (QSVM-Kernel) is explored. A major limitation of the classical SVM is evaluating the similarity between any two data points in a large feature space is computationally expensive. The QSVM-Kernel algorithm exploits the quantum state space as a direct representation of the feature space, which gives rise to kernel functions that are hard to calculate classically, but are efficiently evaluated using quantum kernels. The QSVM-Kernel algorithm is the following:\n \begin{itemize} \item Using a Quantum Feature Map function, map classical data to a quantum state\n \item Calculate the similarity between any two data points using a quantum computer\n \item To find the separate hyperplane, use the kernel entries.\n \end{itemize} This algorithm is then applied to separate between $t\bar{t}H$ (signal) and non-resonant di-photons (background). The quantum simulators used in this paper are from IBM, Google, and Amazon, all of which model the noiseless execution of their respective quantum computer hardware. The performance of these quantum simulators, using 15 qubits and 60 independent datasets of 20000 training events and 20000 testing events, are similar to the performance of a classical SVM and a classical BDT. The QSVM-Kernel algorithm is then implemented on IBM’s quantum processor. The mean performance of QSVM-Kernel on IBM’s quantum processor and IBM’s quantum computer simulator is about 5\% lower. This difference is expected due to hardware noise. The results on IBM’s quantum processor does approach the performance of IBM’s quantum computer simulator. The paper concludes that the running time is expected to be reduced with improved quantum hardware and predicts that quantum machine learning could potentially become a powerful tool for HEP data analyses.

</details>

