import os

class SparseMatrix:

    #initialiizng sparsematrix with a specified number of rows and columns

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
    # Using a dictionary to store non-zero elements for efficient access
        self.elements = {} 

    def add_element(self, row, col, value):
    #Adding a non-zero element on specified row and column of the sparsematrix
        if value != 0:
            self.elements[(row, col)] = value

    @staticmethod
    def load_from_file(file_path):
        """
        Load a sparse matrix from a file.
        Reads and extract the dimensions and elements of the matrix
        then returns an instance of the class
        """
        with open(file_path, 'r') as file:
            line = file.readline().strip()
            if not line.startswith("rows="):
                raise ValueError("Input file has wrong format")
            rows = int(line[5:])

            line = file.readline().strip()
            if not line.startswith("cols="):
                raise ValueError("Input file has wrong format")
            cols = int(line[5:])

            matrix = SparseMatrix(rows, cols)
            for line in file:
                line = line.strip()
                if line:
                    if not (line.startswith("(") and line.endswith(")")):
                        raise ValueError("Input file has wrong format")
                    line = line[1:-1]
                    parts = line.split(',')
                    if len(parts) != 3:
                        raise ValueError("Input file has wrong format")
                    row, col, value = map(int, map(str.strip, parts))
                    matrix.add_element(row, col, value)
        return matrix

    def get_element(self, row, col):
        """
        Retrieves the value of an element in the sparsematrix.
        Returns the value of the element, or 0 if it is not explicitly stored.
        """
        return self.elements.get((row, col), 0)

    def set_element(self, row, col, value):
        """
        Sets the value of an element in the sparsematrix
        Removes the element if the value is zero
        else updates the element
        """
        if value == 0:
            self.elements.pop((row, col), None)
        else:
            self.elements[(row, col)] = value

    def add(self, other):
        """
        function to add two matrices together
        Returns new instance of the class holding the result of addition
        """
        max_rows = max(self.rows, other.rows)
        max_cols = max(self.cols, other.cols)
        result = SparseMatrix(max_rows, max_cols)
        for (row, col), value in self.elements.items():
            result.add_element(row, col, value)
        for (row, col), value in other.elements.items():
            result.set_element(row, col, result.get_element(row, col) + value)
        return result

    def subtract(self, other):
        """
        function to subtract one matrix from the other
        Returns new instance of the class holding the result of the subtraction
        """
        max_rows = max(self.rows, other.rows)
        max_cols = max(self.cols, other.cols)
        result = SparseMatrix(max_rows, max_cols)
        for (row, col), value in self.elements.items():
            result.add_element(row, col, value)
        for (row, col), value in other.elements.items():
            result.set_element(row, col, result.get_element(row, col) - value)
        return result

    def multiply(self, other):
        """
        function to multiply two matrices together
        Returns new instance of the class holding the result of multiplication
        and raises a valueError if the matrices dimensions do not match
        """
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not match for multiplication")
        result = SparseMatrix(self.rows, other.cols)
        for (row1, col1), value1 in self.elements.items():
            for (row2, col2), value2 in other.elements.items():
                if col1 == row2:
                    current_value = result.get_element(row1, col2)
                    result.set_element(row1, col2, current_value + value1 * value2)
        return result

    def save_to_file(self, file_path):
        """
        Save the sparsematrix to a file, writes the matrix dimensions 
        and non-zero elements to the files
        """
        with open(file_path, 'w') as file:
            file.write(f"rows={self.rows}\n")
            file.write(f"cols={self.cols}\n")
            for (row, col), value in self.elements.items():
                file.write(f"({row}, {col}, {value})\n")

def main():

    """
    Main function for loading the matrices from input files,
    allow user to select a preferred operation, call the function
    for performing operations, and saving the result.
    """

    input_path1 = os.path.join("inputs", "matrixfile1.txt")
    input_path2 = os.path.join("inputs", "easy_sample_04_1.txt")
    try:
        matrix1 = SparseMatrix.load_from_file(input_path1)
        matrix2 = SparseMatrix.load_from_file(input_path2)

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")

        try:
            operation = int(input())
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
            return

        result = None
        try:
            if operation == 1:
                result = matrix1.add(matrix2)
                print("\nAddition Done:")
            elif operation == 2:
                result = matrix1.subtract(matrix2)
                print("\nSubtraction Done:")
            elif operation == 3:
                result = matrix1.multiply(matrix2)
                print("\nMultiplication Done:")
            else:
                print("Invalid operation choice.")
                return
        except ValueError as e:
            print(f"Operation error: {e}")
            return

        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, "output.txt")
        result.save_to_file(output_file)
        print(f"Result saved to {output_file}")

    except (IOError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()
