# Sparse Matrix Operations

## Overview

This project implements operations for sparse matrices using Python. The operations supported are addition, subtraction, and multiplication. Sparse matrices are read from input files, and the results are written to output files. it only stores the non-zero elements for more efficiency.

## Installation

- Clone this repository using Git:

  ```bash
  git clone https://github.com/yourusername/DSA-Sparse-Matrix.git

- Navigate to the project directory:

    ```bash
    cd DSA-Sparse-Matrix
    ```

### Input File Format

rows=8433

cols=3180

(0, 381, -694)

(0, 128, -838)

(0, 639, 857)

(0, 165, -933)

(0, 1350, -89)

### Entry Format

(0, 1350, -89): `0` stands for the row, `1350` stands for the column and `-89` is the value.

### Running the script

1. Place your matrix files in the inputs directory.
2. Run the script.

```bash
    python3 sparse_matrix.py
```

### Output File Format

The output file will have the same format as the input file, containing the resulting sparse matrix after the selected operation.

You will be prompted to choose an operation (addition, subtraction, multiplication).
The result will be written to the appropriate file in the output directory.

### Error Handling

The script handles various errors such as:

° Invalid file format.
° Matrix dimension mismatches for operations.
° Invalid user inputs.
