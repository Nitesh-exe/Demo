# Experiment No. 01

**Aim/Title:** Design and Simulation of Quantum Circuits using Single-Qubit Gates in Qiskit

**Title:** Create a single-qubit circuit applying the Hadamard gate

### Software Requirements
- Python 3.x
- Jupyter Notebook
- Qiskit

### Theory
Quantum computing uses qubits, which can exist in the basis states |0⟩ and |1⟩ or in a superposition of both states. Single-qubit gates perform operations on individual qubits. Qiskit is a Python-based framework used to design, simulate, and visualize quantum circuits.

The Pauli-X gate acts as a quantum NOT gate by exchanging |0⟩ and |1⟩. The Pauli-Y gate performs a bit and phase transformation, while the Pauli-Z gate changes the phase of |1⟩ without changing the basis state. The Hadamard gate transforms basis states into superpositions. For example, H|0⟩ = (|0⟩ + |1⟩)/√2. This produces equal probabilities of measuring 0 or 1. Quantum circuits are constructed by applying gates in a particular sequence. Qiskit allows these circuits to be simulated and their outputs measured. These operations form the foundation of quantum algorithms and help demonstrate fundamental principles of quantum mechanics.

### Algorithm
1. Import the required Qiskit libraries.
2. Initialize a quantum circuit with one qubit.
3. Apply the X gate to the qubit.
4. Apply the Z gate to the qubit.
5. Apply the Hadamard gate.
6. Draw the quantum circuit.
7. Simulate the circuit using a quantum simulator.
8. Observe the resulting quantum state.

### Code
```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from IPython.display import display
qc = QuantumCircuit(1, 1)
qc.x(0)
qc.z(0)
qc.h(0)
qc.measure(0, 0)
display(qc.draw("mpl"))
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
print("Measurement Results:", result.get_counts())
```

### Conclusion
The experiment demonstrates single-qubit quantum gates using Qiskit. The circuit illustrates how X, Z, and Hadamard gates transform quantum states through successive operations.

---

# Experiment No. 02

**Aim/Title:** To construct, simulate, and visualize the quantum state (∣01⟩+∣10⟩)/√2 using Qiskit and understand the behaviour of quantum entanglement through measurement statistics and state vector visualization.

**Title:** Measure the qubit and plot the histogram of results

### Software Requirements
- Python 3.x
- Jupyter Notebook
- Qiskit

### Theory
Quantum entanglement is a fundamental property of quantum mechanics in which two or more qubits share a joint quantum state that cannot be described as independent states. An example is the state (|01⟩ + |10⟩)/√2, where measurements produce correlated outcomes: 01 or 10, each with an ideal probability of 50%.

Qiskit provides tools to construct, simulate, measure, and visualize entangled quantum circuits. A quantum circuit can be initialized with two qubits and prepared using X, Hadamard, and CNOT gates. Measurement converts quantum states into classical outcomes. A histogram displays the frequency of these outcomes and helps analyze their probabilities. Qiskit also supports state visualization through functions such as `plot_state_city()`, `plot_state_hinton()`, `plot_state_qsphere()`, and `plot_state_paulivec()`. These visualizations represent different aspects of a quantum state, including amplitudes and phases. Such tools help understand entanglement, measurement statistics, and quantum circuit behaviour.

### Algorithm
1. Import Qiskit and visualization libraries.
2. Create a quantum circuit with two qubits and two classical bits.
3. Apply the X gate to qubit 1.
4. Apply the Hadamard gate to qubit 0.
5. Apply a CNOT gate with qubit 0 as control and qubit 1 as target.
6. Measure both qubits.
7. Simulate the circuit using a quantum simulator.
8. Collect the measurement counts.
9. Plot a histogram of the outcomes.
10. Visualize the quantum state using Qiskit visualization functions.

### Code
```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import (
plot_histogram,
plot_state_city,
plot_state_hinton,
plot_state_qsphere,
plot_state_paulivec,
plot_bloch_multivector
)
from IPython.display import display
qc = QuantumCircuit(2, 2)
qc.x(1)
qc.h(0)
qc.cx(0, 1)
display(qc.draw("mpl"))
state = Statevector.from_instruction(qc)
display(plot_state_city(state))
display(plot_state_hinton(state))
display(plot_state_qsphere(state))
display(plot_state_paulivec(state))
display(plot_bloch_multivector(state))
measured_qc = qc.copy()
measured_qc.measure([0, 1], [0, 1])
simulator = AerSimulator()
result = simulator.run(measured_qc, shots=1024).result()
counts = result.get_counts()
display(plot_histogram(counts))
print("Measurement Results:", counts)
```

### Conclusion
The experiment demonstrates the preparation and measurement of an entangled two-qubit state. Qiskit simulations and histograms help analyze measurement probabilities and understand quantum-state behaviour.

---

# Experiment No. 03

**Aim/Title:** To design, simulate, and visualize a 2-qubit Bell state using Qiskit, and analyze its entangled properties using measurement results and statevector visualizations.

**Title:** Build a circuit to generate a Bell state

### Software Requirements
- Python 3.x
- Jupyter Notebook
- Qiskit

### Theory
Quantum entanglement occurs when two or more qubits share a joint quantum state that cannot be represented as a product of independent states. Bell states are important examples of maximally entangled two-qubit states and demonstrate correlations that cannot be explained using ordinary classical probabilities.

One of the four Bell states is the Phi-plus state, represented as |Φ⁺⟩ = (|00⟩ + |11⟩)/√2. In this state, measuring both qubits in the computational basis ideally produces either 00 or 11, each with a probability of 50%. A Bell state can be generated by initializing two qubits to |00⟩, applying a Hadamard gate to the first qubit, and then applying a CNOT gate with the first qubit as control and the second as target. Qiskit allows this circuit to be simulated using a quantum simulator. Measurements reveal the correlated outcomes, while statevector visualization tools help examine the quantum state before measurement.

### Algorithm
1. Import the required Qiskit libraries.
2. Initialize a circuit with two qubits and two classical bits.
3. Apply the Hadamard gate to qubit 0.
4. Apply a CNOT gate with qubit 0 as control and qubit 1 as target.
5. Measure both qubits into classical bits.
6. Simulate the circuit using AerSimulator.
7. Collect the measurement counts.
8. Plot a histogram of the results.
9. Visualize the quantum state using Qiskit visualization functions.

### Code
```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import (
plot_histogram,
plot_state_city,
plot_state_hinton,
plot_state_qsphere,
plot_state_paulivec,
plot_bloch_multivector
)
from IPython.display import display
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
display(qc.draw("mpl"))
state = Statevector.from_instruction(qc)
display(plot_state_city(state))
display(plot_state_hinton(state))
display(plot_state_qsphere(state))
display(plot_state_paulivec(state))
display(plot_bloch_multivector(state))
qc.measure([0, 1], [0, 1])
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()
display(plot_histogram(counts))
print("Measurement Results:", counts)
```

### Conclusion
The experiment successfully demonstrates Bell-state generation using Hadamard and CNOT gates. Simulation and visualization reveal entanglement and the correlated measurement outcomes of both qubits.

---

# Experiment No. 04

**Aim/Title:** To implement the Superdense Coding protocol using Qiskit and simulate it on a quantum circuit to verify the correct transfer of two classical bits using one qubit.

**Title:** Superdense Coding using Qiskit

### Software Requirements
- Python 3.x
- Jupyter Notebook
- Qiskit

### Theory
Superdense coding is a quantum communication protocol that enables the transmission of two classical bits of information by sending one qubit, provided the sender and receiver initially share an entangled pair of qubits. The protocol uses quantum entanglement and quantum gates to encode and decode information.

Initially, Alice and Bob share a Bell state, typically |Φ⁺⟩ = (|00⟩ + |11⟩)/√2. Alice encodes her two-bit message by applying an appropriate operation to her qubit. Depending on the message, she applies no gate or uses X, Z, or a combination of these gates. Alice then sends her qubit to Bob. Bob performs a decoding operation using a CNOT gate followed by a Hadamard gate. Finally, he measures both qubits to recover the encoded message. Qiskit can simulate the complete protocol and display measurement results using histograms. Superdense coding demonstrates how shared quantum entanglement can improve communication efficiency compared with sending the same information using an unentangled qubit alone.

### Algorithm
1. Import the required Qiskit libraries.
2. Create a circuit with two qubits and two classical bits.
3. Apply a Hadamard gate to qubit 0.
4. Apply a CNOT gate to create a Bell state.
5. Encode Alice's message using the appropriate gates.
6. Simulate the transfer of Alice's qubit to Bob.
7. Apply a CNOT gate for decoding.
8. Apply a Hadamard gate to qubit 0.
9. Measure both qubits.
10. Simulate the circuit using AerSimulator.
11. Display measurement counts and plot a histogram.
12. Repeat the process for messages 00, 01, 10, and 11.

### Code
```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from IPython.display import display
messages = ["00", "01", "10", "11"]
simulator = AerSimulator()
for message in messages:
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
if message == "01":
qc.z(0)
elif message == "10":
qc.x(0)
elif message == "11":
qc.z(0)
qc.x(0)
qc.cx(0, 1)
qc.h(0)
qc.measure([0, 1], [0, 1])
print(f"Message: {message}")
display(qc.draw("mpl"))
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()
display(plot_histogram(counts))
print("Measurement Results:", counts)
```

### Conclusion
The experiment demonstrates superdense coding using Qiskit. Shared entanglement and quantum gates enable the encoding and decoding of two classical bits by transmitting one qubit.

---

# Experiment No. 05

**Aim/Title:** To implement the SWAP gate using three CNOT gates in Qiskit and simulate it on a quantum circuit to verify correct swapping of qubits.

**Title:** Implement a multi-qubit circuit of SWAP Using CNOT

### Software Requirements
- Python 3.x
- Jupyter Notebook
- Qiskit

### Theory
The SWAP gate is a fundamental quantum gate that exchanges the quantum states of two qubits. It does not physically move the qubits; instead, it transfers their states between them. For example, the state |01⟩ becomes |10⟩ after applying the SWAP operation, while |00⟩ and |11⟩ remain unchanged.

In quantum computing, the SWAP gate can be constructed using three Controlled-NOT (CNOT) gates. The first CNOT uses qubit 0 as the control and qubit 1 as the target. The second CNOT reverses these roles, and the third CNOT again uses qubit 0 as the control and qubit 1 as the target. Together, these operations exchange the states of the two qubits. Qiskit allows this circuit to be designed, simulated, and visualized. By testing different input states, such as |01⟩, |10⟩, and |11⟩, the correctness of the SWAP construction can be verified through measurement results and histograms.

### Algorithm
1. Import the required Qiskit libraries.
2. Create a circuit with two qubits and two classical bits.
3. Prepare the required input state.
4. Apply CNOT from qubit 0 to qubit 1.
5. Apply CNOT from qubit 1 to qubit 0.
6. Apply CNOT from qubit 0 to qubit 1.
7. Measure both qubits.
8. Simulate the circuit using AerSimulator.
9. Display measurement results and plot a histogram.
10. Repeat for different input states to verify swapping.

### Code
```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from IPython.display import display
states = ["01", "10", "11"]
simulator = AerSimulator()
for state in states:
qc = QuantumCircuit(2, 2)
if state[0] == "1":
qc.x(1)
if state[1] == "1":
qc.x(0)
qc.cx(0, 1)
qc.cx(1, 0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])
print(f"Input State: |{state}>")
display(qc.draw("mpl"))
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()
display(plot_histogram(counts))
print("Measurement Results:", counts)
```

### Conclusion
The experiment demonstrates the implementation of a SWAP gate using three CNOT gates in Qiskit. Simulation verifies that the quantum states of two qubits are exchanged correctly.

---

# Experiment No. 06

**Aim/Title:** To implement the Deutsch–Jozsa algorithm using Qiskit and simulate it for both a constant and a balanced oracle in order to determine whether the given oracle function is constant or balanced.

**Title:** Implement and run the Deutsch–Jozsa algorithm on a balanced and constant function

### Software Requirements
- Python 3.x
- Jupyter Notebook
- Qiskit

### Theory
The Deutsch–Jozsa algorithm is a quantum algorithm used to determine whether a given Boolean function is constant or balanced. A constant function produces the same output for every input, whereas a balanced function produces 0 for half of the possible inputs and 1 for the other half. The function is provided through a quantum oracle.

The algorithm begins by initializing the input qubits to |0⟩ and an ancilla qubit to |1⟩. Hadamard gates are applied to all qubits to create superposition. The oracle then encodes information about the function into the quantum state. Applying Hadamard gates again to the input qubits produces interference that reveals the function's type. Finally, the input qubits are measured. If the measurement result is all zeros, the function is constant; otherwise, it is balanced. Unlike a classical approach that may require multiple queries, the quantum algorithm determines the function's type using a single oracle query under the promised conditions. Qiskit can simulate both oracle types and display their measurement results.

### Algorithm
1. Import Qiskit and visualization libraries.
2. Create a circuit with two input qubits, one ancilla qubit, and two classical bits.
3. Initialize the ancilla qubit to |1⟩.
4. Apply Hadamard gates to all qubits.
5. Construct the constant or balanced oracle.
6. Apply the oracle to the circuit.
7. Apply Hadamard gates to both input qubits.
8. Measure the input qubits.
9. Simulate the circuit using a quantum simulator.
10. Analyze the results to identify the function type.

### Code
```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from IPython.display import display
simulator = AerSimulator()
n=2
for oracle_type in ["Constant", "Balanced"]:
qc = QuantumCircuit(n + 1, n)
qc.x(n)
qc.h(range(n + 1))
if oracle_type == "Balanced":
qc.cx(0, n)
qc.h(range(n))
qc.measure(range(n), range(n))
print(f"{oracle_type} Oracle")
display(qc.draw("mpl"))
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()
display(plot_histogram(counts))
print("Measurement Results:", counts)
```

### Conclusion
The experiment demonstrates the Deutsch–Jozsa algorithm using Qiskit. Measurement results distinguish constant and balanced functions, illustrating quantum superposition, interference, and efficient oracle-based computation.

---

# Experiment No. 7

**Aim/Title:** To implement and run Grover’s algorithm to search for a marked state.

**Title:** Implement and run Grover’s algorithm to search for a marked state.

### Software Requirements
- Python 3.x
- Jupyter Notebook
- Qiskit

### Theory
Grover’s algorithm is a quantum search algorithm that finds a marked item in an unstructured search space faster than classical exhaustive search. For a search space containing N possible items, classical search may require O(N) queries in the worst case, whereas Grover’s algorithm requires approximately O(√N) oracle queries.

The algorithm begins by initializing n qubits to |0⟩ and applying Hadamard gates to create an equal superposition of all possible states. A quantum oracle identifies the marked state by reversing its phase. Next, the diffusion operator amplifies the probability amplitude of the marked state while reducing the amplitudes of other states. The oracle and diffusion operations are repeated an appropriate number of times to maximize the probability of finding the solution. Finally, the qubits are measured to identify the marked state. Qiskit can be used to construct and simulate the circuit, collect measurement counts, and visualize the results. Grover’s algorithm is important in quantum search and has implications for cryptography and other computational problems.

### Algorithm
1. Import the required Qiskit libraries.
2. Initialize a quantum circuit with the required number of qubits.
3. Apply Hadamard gates to create an equal superposition.
4. Construct an oracle that marks the target state.
5. Apply the oracle to the circuit.
6. Apply the Grover diffusion operator.
7. Repeat the oracle and diffusion operations the required number of times.
8. Measure all qubits.
9. Simulate the circuit using a quantum simulator.
10. Display measurement counts and analyze the probability of finding the marked state.

### Code
```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from IPython.display import display
qc = QuantumCircuit(2, 2)
qc.h([0, 1])
qc.cz(0, 1)
qc.h([0, 1])
qc.x([0, 1])
qc.h(1)
qc.cx(0, 1)
qc.h(1)
qc.x([0, 1])
qc.h([0, 1])
qc.measure([0, 1], [0, 1])
display(qc.draw("mpl"))
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()
display(plot_histogram(counts))
print("Measurement Results:", counts)
```

### Conclusion
The experiment demonstrates Grover’s algorithm using Qiskit. The oracle and diffusion operations amplify the marked state's probability, illustrating the quadratic search advantage over classical exhaustive search.

---

# Experiment No. 8

**Aim/Title:** To implement and run the Quantum Fourier Transform (QFT) and Shor’s algorithm.

**Title:** Implement and run the Quantum Fourier Transform (QFT) and Shor’s algorithm.

### Software Requirements
- Python 3.x
- Jupyter Notebook
- Qiskit

### Theory
The Quantum Fourier Transform (QFT) is a quantum operation that transforms the amplitudes of a quantum state into a representation related to the discrete Fourier transform. It plays an important role in quantum algorithms, particularly phase estimation and Shor’s algorithm.

Shor’s algorithm is a quantum algorithm designed to factor composite integers efficiently by reducing factorization to the problem of finding the period of a modular arithmetic function, f(x) = aˣ mod N. Here, N is the number to be factored, and a is an integer relatively prime to N. The period r is the smallest positive integer satisfying aʳ mod N = 1. The quantum period-finding procedure uses quantum superposition and the QFT to extract information about this period. Classical post-processing then uses the period to calculate possible factors through greatest common divisor operations. If the selected period is suitable, non-trivial factors of N can be obtained. Shor’s algorithm is significant because large-scale quantum computers could use it to threaten cryptographic systems such as RSA, motivating the development of post-quantum cryptography.

### Algorithm
1. Import the required Python and Qiskit libraries.
2. Initialize the quantum circuit required for the QFT.
3. Apply Hadamard and controlled-phase gates to implement the QFT.
4. Simulate the QFT circuit and observe the results.
5. Select a composite integer N for Shor’s algorithm.
6. Choose an integer a such that 1 < a < N.
7. Calculate gcd(a, N); if it is greater than 1, a factor is found.
8. Otherwise, determine the period r of aˣ mod N using quantum period finding.
9. Check whether the period is suitable for factorization.
10. Calculate gcd(aʳᐟ² − 1, N) and gcd(aʳᐟ² + 1, N).
11. Display the non-trivial factors obtained.

### Code
```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
from IPython.display import display
from math import gcd
from numpy import pi
def qft(qc, n):
for i in range(n):
qc.h(i)
for j in range(i + 1, n):
qc.cp(pi / (2 ** (j - i)), j, i)
for i in range(n // 2):
qc.swap(i, n - i - 1)
n=3
qc = QuantumCircuit(n, n)
qc.x(0)
qft(qc, n)
display(qc.draw("mpl"))
state = Statevector.from_instruction(qc)
print("QFT Statevector:")
print(state)
qc.measure(range(n), range(n))
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()
display(plot_histogram(counts))
print("Measurement Results:", counts)
N = 15
a=2
print("\nShor's Algorithm")
print("N =", N)
print("a =", a)
print("gcd(a, N) =", gcd(a, N))
r=1while pow(a, r, N) != 1:
r += 1
print("Order r =", r)
if r % 2 == 0 and pow(a, r // 2, N) != N - 1:
factor1 = gcd(pow(a, r // 2, N) - 1, N)
factor2 = gcd(pow(a, r // 2, N) + 1, N)
print("Factors:", factor1, "and", factor2)
```

### Conclusion
The experiment introduces QFT and Shor’s algorithm using quantum computing principles. It demonstrates how period finding and classical post-processing can determine non-trivial factors of composite integers.
