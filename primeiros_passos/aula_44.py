"""
for item in list:
   ...
"""

qubits = [0, 0, 1, 1]
numbers = range(len(qubits))

for i in numbers:
    print(f"Q{i}({qubits[i]})", type(qubits[i]))
