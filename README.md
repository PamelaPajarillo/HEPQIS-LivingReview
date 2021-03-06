#  **A Living Review of Quantum Information Science in Particle Physics**


**🟥🟥🟥 Warning! LaTeX formatting in GitHub (used in the descriptions of each paper) is not functioning properly. Please refer to the <a href="https://github.com/PamelaPajarillo/HEPQIS-LivingReview/blob/main/HEPQIS_DETAIL.pdf"> PDF version found here </a> 🟥🟥🟥**


**<a href="https://github.com/PamelaPajarillo/HEPQIS-LivingReview/blob/main/HEPQIS_LIST.pdf"> PDF of list of references </a>**


**<a href="https://github.com/PamelaPajarillo/HEPQIS-LivingReview/blob/main/HEPQIS_BRIEF.pdf"> PDF of references with short descriptions (HEP context, methods, results and conclusions) </a>**


**<a href="https://github.com/PamelaPajarillo/HEPQIS-LivingReview/blob/main/HEPQIS_DETAIL.pdf"> PDF of references with detailed descriptions </a>**

*Inspired by "A Living Review of Machine Learning for Particle Physics", the goal of this repository is to provide an extensive list of citations for those developing and applying quantum information approaches to experimental, phenomenological, or theoretical analyses.  Applications of quantum information science to high energy physics is a relatively new field of research.  This repository will be updated as often as possible with the relevant literature.  Suggestions are most welcome.*

The goal of this repository is to collect references for quantum information science as applied to particle and nuclear physics.  

##  **Reviews**

<details>
<summary> <a href="https://arxiv.org/abs/2005.08582"> Quantum Machine Learning in High Energy Physics</a> [<a href="https://doi.org/10.1088/2632-2153/abc17d">DOI</a>]</summary>

+ ***HEP Context:*** *Di-photon event classification, galaxy morphology classification, particle track reconstruction, and signal-background discrimination with the SUSY data set*
+ ***Methods:*** *Quantum machine learning using quantum annealing, restrictive Boltzmann machines, quantum graph networks, and variational quantum circuits*
+ ***Results and Conclusions:*** *This paper presents several papers on performing classification using quantum machine learning. The studies presented some of the challenges faced, such as the restrictive problem formulation for quantum annealers and the limited performance due to hardware restrictions for quantum-circuit-based machine learning.*

This review presents papers using quantum machine learning (QML) to perform classification with quantum annealing, restricted Boltzmann machines, quantum graph networks and variational quantum circuits. One of the main challenges of quantum annealing is its restrictive formulation (i.e rephrasing the loss function into a Quadratic Unconstrained Binary (QUBO) problem). Quantum-circuit-based machine learning is still at limited performance because of quantum device limitations. This review also discusses implementing QML directly on quantum data and practical considerations of experimenting with quantum annealers and quantum circuits.

</details>



##  **Whitepapers**

<details>
<summary> <a href="https://arxiv.org/abs/2204.03381"> Quantum Simulation for High Energy Physics</a></summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2203.08805"> Quantum Computing for Data Analysis in High-Energy Physics</a></summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2203.07091"> Snowmass White Paper: Quantum Computing Systems and Software for High-energy Physics Research</a></summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>



##  **Quantum Optimization Algorithms Based on Gate-Based Quantum Computers**



##  **Quantum Optimization Algorithms Based on Quantum Annealing**

<details>
<summary> <a href="https://arxiv.org/abs/2205.10375"> Degeneracy Engineering for Classical and Quantum Annealing: A Case Study of Sparse Linear Regression in Collider Physics</a></summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2205.02814"> Quantum Annealing for Jet Clustering with Thrust</a></summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2111.07806"> Leveraging Quantum Annealer to identify an Event-topology at High Energy Colliders</a></summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/1908.04475"> Charged particle tracking with quantum annealing-inspired optimization</a> [<a href="https://doi.org/10.1007/s42484-021-00054-w">DOI</a>]</summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>



##  **Quantum Machine Learning Algorithms Based on Gate-Based Quantum Computers**

<details>
<summary> <a href="https://arxiv.org/abs/2012.11560"> Application of quantum machine learning using the quantum variational classifier method to high energy physics analysis at the LHC on IBM quantum computer simulator and hardware with 10 qubits</a> [<a href="https://doi.org/10.1088/1361-6471/ac1391">DOI</a>]</summary>

+ ***HEP Context:*** *Signal-background discrimination, where signal events are $t\bar{t}H$ ($H\rightarrow\gamma\gamma$) and $H\rightarrow\mu\mu$, and background events are dominant Standard Model processes*
+ ***Methods:*** *Variational quantum circuits*
+ ***Results and Conclusions:*** *TBD*

Using IBM gate-based quantum computers, the quantum variational classifier method is applied to the $t\bar{t}H$ (examines the Higgs coupling to the top quark) and $H\rightarrow\mu\mu$ (examines the Higgs coupling to second-generation fermions) analyses, with the goal of classifying physics events of interest from background events. Using event generators to produce signal and background events for $t\bar{t}H$ and $H\rightarrow\mu\mu$, a Principal Component Analysis (PCA) method converts kinematic variables to a smaller amount of variables so that the number of encoded variables is equal to the number of available qubits. Then, a feature map circuit which encodes the input data $\vec{x}$ into a quantum state is applied. A quantum variational circuit $W(\vec{\theta})$ which is parametrized by gate angles $\vec{\theta}$ is then applied. Finally, the qubit state is measured in the computational basis and the output state is classified as either signal or background through the action of a diagonal operator in the standard basis. To train the quantum variational circuit $W(\vec{\theta})$ for the optimized parameters $\vec{\theta}$, a set of input data and its labels are used. With 100 training events, 100 test events, and 10 encoded variables, the AUC of IBM's quantum computer simulator that includes a noise model with 10 qubits are similar to the AUC of a classical support vector machine (SVM) and a boosted decision tree (BDT) classifier. The quantum variational classifier is then employed on two of IBM's quantum computers, and the results show that the quantum computer and quantum simulator are in good agreement, however, the run time on the quantum computer is longer than the classical machine learning algorithms due to the limitations in quantum hardware. The paper concludes by stating that the use of quantum machine learning could potentially offer an advantage with the rapid advances in quantum computing technology.

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2104.05059"> Application of quantum machine learning using the quantum kernel algorithm on high energy physics analysis at the LHC</a> [<a href="https://doi.org/10.1103/PhysRevResearch.3.033221">DOI</a>]</summary>

+ ***HEP Context:*** *Signal-background discrimination, where signal events are $t\bar{t}H$ ($H\rightarrow\gamma\gamma$), and background events are dominant Standard Model processes*
+ ***Methods:*** *Support vector machine with a quantum kernel estimator (QSVM-Kernel)*
+ ***Results and Conclusions:*** *TBD*

To classify signal and background events in the $t\bar{t}H$ analysis, the use of a support vector machine (SVM) with a quantum kernel estimator (QSVM-Kernel) is explored. A major limitation of the classical SVM is evaluating the similarity between any two data points in a large feature space is computationally expensive. The QSVM-Kernel algorithm exploits the quantum state space as a direct representation of the feature space, which gives rise to kernel functions that are hard to calculate classically, but are efficiently evaluated using quantum kernels. The QSVM-Kernel algorithm is the following: (1) Using a Quantum Feature Map function, map classical data to a quantum state; (2) Calculate the similarity between any two data points using a quantum computer; and finally (3) To find the separate hyperplane, use the kernel entries. This algorithm is then applied to separate between $t\bar{t}H$ (signal) and non-resonant di-photons (background). The quantum simulators used in this paper are from IBM, Google, and Amazon, all of which model the noiseless execution of their respective quantum computer hardware. The performance of these quantum simulators, using 15 qubits and 60 independent datasets of 20000 training events and 20000 testing events, are similar to the performance of a classical SVM and a classical BDT. The QSVM-Kernel algorithm is then implemented on IBM's quantum processor. The mean performance of QSVM-Kernel on IBM's quantum processor and IBM's quantum computer simulator is about 5\% lower. This difference is expected due to hardware noise. The results on IBM's quantum processor does approach the performance of IBM's quantum computer simulator. The paper concludes that the running time is expected to be reduced with improved quantum hardware and predicts that quantum machine learning could potentially become a powerful tool for HEP data analyses.

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2206.08391"> Quantum Anomaly Detection for Collider Physics</a></summary>

+ ***HEP Context:*** *Anomaly detection in the four-lepton final state*
+ ***Methods:*** *Variational Quantum Circuits (VQC) and Quantum Circuit Learning (QCL)*
+ ***Results and Conclusions:*** *After comparing VQC and QCL to traditional classical machine learning algorithms, this paper states that there is no evidence that quantum machine learning provides any advantage to classical machine learning.*

From the studies in Quantum Machine Learning (QML) in high energy physics, one of the common themes is it seems to outperform classical machine learning (CML) with small training datasets. This paper studies the feasibility of anomaly detection in collider physics. The approach in signal model-independent anomaly detection is to train a classifier to distinguish data from an accurate prediction of the background, which is a form of weakly/semi-supervised learning. One of the final states that is precisely known is the four charged lepton final states. The current approach use Monte Carlo (MC) simulations to estimate the background, however this is signal model-specific and does not easily extend to other models. The two QML methods that are analyzed in this paper are Variational Quantum Circuits (VQC) and Quantum Circuit Learning (QCL), which are both implementations of parametrized quantum circuits where the rotation angles are optimized using classical methods and only differ in the encoding of classical data and the parameterization. The approach for both methods is as follows: (1) Scale the input features $x_{i}$ such that the arguments for some unitary function $U(x_{i})$ are valid angles; (2) Initialize qubits with $ \vert 0 \rangle \vert 0 \rangle \ldots \vert 0 \rangle $; (3) Apply $U_{in}(x_{i})$ to each $i^{\text{th}}$ qubit. This step encodes classical input data into quantum states; (4) Apply a unitary circuit $U(\theta)$ where $\theta$ are the trainable weights of the circuit; (5) Measure the output values from the circuit and evaluate the loss function; (6) Repeat steps (2)-(5) $n$ times updating $\theta$ such that it minimizes the loss function. $U_{in}(x)$ for VQC consists of rotation gates $R_{Y}(x_{i})$, whereas $U_{in}(x)$ for QCL consists of Hadamard gates followed by rotation gates $R_{Y}(\arcsin(x_{i}))$ and $R_{Z}(\arccos(x_{i}^{2}))$ and CNOT gates. $U(\theta)$ consists of rotation gates followed by CNOT gates, whereas $U(\theta)$ consists of time evolution of operation based on the Ising model Hamiltonian followed by rotation gates $R_{Y}(\theta)$ and $R_{Z}(\theta)$. These methods are compared against two neural networks implemented in TensorFlow. The results show that there is no evidence that QML provides any advantage over CML.

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2002.09935"> Event Classification with Quantum Machine Learning in High-Energy Physics</a> [<a href="https://doi.org/10.1007/s41781-020-00047-7">DOI</a>]</summary>

+ ***HEP Context:*** *Signal-background discrimination, where the signal is a SUSY process, in particular, a chargino-pair production via a Higgs boson, where the final state has two charged leptons and missing transverse momentum. The background event is a $W$ boson pair production $WW$ where each $W$ decays into a charged lepton and a neutrino.*
+ ***Methods:*** *Variational Quantum Circuits (VQC) and Quantum Circuit Learning (QCL)*
+ ***Results and Conclusions:*** *TBD*

In this paper, two quantum machine learning (QML) algorithms based on gate-based quantum computers, in particular variational quantum algorithms, Quantum Circuit Learning (QCL) and Variational Quantum Classification (VQC) are analyzed in the context of signal-background discrimination, where signal is an event originating from new physics beyond the Standard Model and background is an event originating from Standard Model processes. In this case, the signal event is a chargino-pair production via a Higgs boson, where the final state has two charged leptons and missing transverse momentum. The background event is a $W$ boson pair production $WW$ where each $W$ decays into a charged lepton and a neutrino. Both variational quantum algorithms have 3 steps: (1) quantum gates $U_{in}(\vec{x})$ to encode classical input data $\vec{x}$ into quantum states; (2) quantum gates $U(\vec{\theta})$ to produce output states used for supervised learning parametrized by a set of free parameters $\theta$ which will be optimized to model input training data; (3) measurement gates to obtain output values which will be compared by the labels $\vec{y}$. These steps are repeated $N$ times, tuning $\vec{\theta}$ using a classical computer by minimizing a loss function. In QCL, $U_{in}(\vec{x})$ is composed of a series of single qubit rotation gates $R_{Y}$ and $R_{Z}$, where the angles of the rotations gates are $\arcsin(\vec{x})$ and $\arccos(\vec{x}^2)$ where $\vec{x}$ is the normalized within $[-1,1]$. In VQC, $U_{in}(\vec{x})$ is characterized by a set of Hadamard gates and rotation gates with angles from the input data $\vec{x}$. In QCL, $U(\theta)$ is constructed by a time evolution gate denoted $e^{-iHt}$, where $H$ is the Hamiltonian of an Ising model and a series of $R_{X}$, $R_{Y}$, and $R_{Z}$ gates with angles as the arguments. In VQC, $U(\theta)$ is comprised of Hadamard, CNOT, and single-qubit rotation gates $R_{Y}$ and $R_{Z}$. A deep neural network (DNN) and a boosted decision tree (BDT) are used as benchmark tools for comparison with the performances of QCL and VQC. The VQC algorithm is performed on a quantum circuit simulator called Qulacs. The VQC algorithm is performed on a quantum circuit simulator Qiskit Aqua and on IBM's quantum computer. The performance of the QCL algorithms on quantum simulators is characterized by a relatively flat AUC as a function of the number of training events. The AUC for QCL is higher than the AUC for BDT and DNN for a low number of training events, however, for high training events, the performance for BDT and DNN surpasses QCL. The VQC algorithm has been tested on IBM's quantum computer, and the performance is similar to that of the quantum simulator. However, there is an increase in uncertainty due to hardware noise. Other QCL and VQC models are tested, which do not show any improvement to the nominal QCL and VQC models. The behavior that variational quantum algorithms does better with a small number of training data could be considered as a possible advantage over classical machine learning.

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2202.13943"> Quantum Machine Learning for $b$-jet identification</a></summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2202.10471"> Classical versus Quantum: comparing Tensor Network-based Quantum Circuits on LHC data</a></summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2112.04958"> Anomaly detection in high-energy physics using a quantum autoencoder</a> [<a href="https://doi.org/10.1103/PhysRevD.105.095004">DOI</a>]</summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://doi.org/10.1038/s41598-021-01552-4"> Implementation and analysis of quantum computing application to Higgs boson reconstruction at the large Hadron Collider</a></summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2110.06933"> Style-based quantum generative adversarial networks for Monte Carlo events</a></summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>



##  **Quantum Machine Learning Algorithms Based on Quantum Annealing**

<details>
<summary> <a href="https://doi.org/10.1038/nature24047"> Solving a Higgs optimization problem with quantum annealing for machine learning</a></summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

Using D-Wave's programmable quantum annealer, this paper explores quantum annealing for machine learning (QAML). The paper shows that quantum and classical annealing-based classifiers perform comparably with no clear advantage to traditional machine learning methods, including deep neural network (DNN) and an ensemble of boosted decision trees (BDTs), to solve a Higgs signal-background discrimination machine learning optimimzation problem, which identifies features from a pair of photons correspond to a decay from the Higgs or other Standard Model processes. The inputs of the weak binary classifiers are the encoded transverse momentum of photons and the correlations between the two photons. The strong classifier is then constructed from a linear combination of weak classifiers, where the weights are obtained through an optimization problem, which must have a mapping to a quadratic unconstrained binary optimization (QUBO) problem. This classifier is resistant to overfitting, since due to noise, the D-Wave quantum annealer will avoid the global minimum of the loss functional, and it has a slight advantage over BDT and DNN with a smaller training dataset.

</details>

<details>
<summary> <a href="https://arxiv.org/abs/1908.04480"> Quantum adiabatic machine learning with zooming</a> [<a href="https://doi.org/10.1103/PhysRevA.102.062405">DOI</a>]</summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

Inspired by quantum annealing for machine learning (QAML), which constructs a strong classifier from a linear combination of weak binary classifiers. this paper proposes a variant called QAML-Z, where the binary classifiers are modified to continuous real values by performing a search on the real numbers. This works by zooming into a region of the energy surface and iteratively perform quantum annealing to an augmented set of weak classifiers, which then makes a strong classifier. The iteration rule that gives the weight of each classifier consists of shifting the value of mean based on the spin of the qubit then narrowing the search breadth. The zooming algorithm increases the probability of overfitting, so the authors of the paper propose regularizing the iterative process by applying a bit flip between each iteration with monotonically decreasing probability. This effectively prevents the strong classifier from overfitting and overcomes getting out of a local minima. The QAML-Z algorithm is applied to the Higgs optimization problem, where features of a diphoton event must be identified in order to classify events as a Higgs decay or other Standard Model processes. QAML-Z does not show an obvious advantage over traditional machine learning methods, including deep neural networks (DNNs) and boosted decision trees (BDTs), however, its performance surpasses the QAML algorithm and simulated annealing with zooming.

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2106.00051"> Quantum algorithm for the classification of supersymmetric top quark events</a> [<a href="https://doi.org/10.1103/PhysRevD.104.096004">DOI</a>]</summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>



##  **Quantum Simulation**



##  **Quantum-Inspired Algorithms**

<details>
<summary> <a href="https://arxiv.org/abs/2106.08334"> Quantum-inspired event reconstruction with Tensor Networks: Matrix Product States</a> [<a href="https://doi.org/10.1007/JHEP08(2021)112">DOI</a>]</summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>



##  **TBD**

<details>
<summary> <a href="https://arxiv.org/abs/2012.12177"> Quantum convolutional neural networks for high energy physics data analysis</a> [<a href="https://doi.org/10.1103/PhysRevResearch.4.013231">DOI</a>]</summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2101.06189"> Hybrid Quantum-Classical Graph Convolutional Network</a></summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2010.07335"> Quantum Machine Learning for Particle Physics using a Variational Quantum Classifier</a> [<a href="https://doi.org/10.1007/JHEP02(2021)212">DOI</a>]</summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/1902.08324"> A pattern recognition algorithm for quantum annealers</a> [<a href="https://doi.org/10.1007/s41781-019-0032-5">DOI</a>]</summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/1908.08949"> Quantum Algorithms for Jet Clustering</a> [<a href="https://doi.org/10.1103/PhysRevD.101.094015">DOI</a>]</summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2104.11583"> Quantum speedup for track reconstruction in particle accelerators</a> [<a href="https://doi.org/10.1103/PhysRevD.105.076012">DOI</a>]</summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2012.14514"> Adiabatic Quantum Algorithm for Multijet Clustering in High Energy Physics</a></summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2010.00649"> Application of a Quantum Search Algorithm to High- Energy Physics Data at the Large Hadron Collider</a></summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2203.03578"> Unsupervised Quantum Circuit Learning in High Energy Physics</a></summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2103.12257"> Quantum Support Vector Machines for Continuum Suppression in B Meson Decays</a> [<a href="https://doi.org/10.1007/s41781-021-00075-x">DOI</a>]</summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2103.03897"> Unsupervised event classification with graphs on classical and photonic quantum computers</a> [<a href="https://doi.org/10.1007/JHEP08(2021)170">DOI</a>]</summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>

<details>
<summary> <a href="https://arxiv.org/abs/2104.07692"> Higgs analysis with quantum classifiers</a> [<a href="https://doi.org/10.1051/epjconf/202125103070">DOI</a>]</summary>

+ ***HEP Context:*** *TBD*
+ ***Methods:*** *TBD*
+ ***Results and Conclusions:*** *TBD*

TBD

</details>



