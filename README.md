# Differential Cryptanalysis of a Substitution-Permutation Network

This repository contains a report and Python code for differential cryptanalysis applied to a 4x4 S-Box substitution-permutation network.

## Report
The **`report.pdf`** is the final report, which includes the theoretical analysis and experimental results based on 10,000 chosen plaintext strings.

The LaTeX source files are available in the **`src/`** folder, which includes `main.tex`, the main LaTeX document.

## Python Code
The **`code/`** directory contains the Python code used to perform the differential cryptanalysis:
- **`diff_cryptanalysis.py`**: Main differential cryptanalysis code to extract bits from the final round key.
- **`generate.py`**: Code to generate ciphertext pairs with the desired input differences.
- **`spn.py`**: Functions used to implement the substitution-permutation network.
