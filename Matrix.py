import numpy as np
import scipy as sp
class MatrixOperations:
    def __init__(self):
        self.A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.axis = 0
        self.scalar = 5

    def showMenu(self):
        self.printMenu()
        while True:
            print("0.1. ShowMenu")
            user_choice = self.get_user_choice()
            if user_choice == '0':
                break
            
            self.ask_user_details(user_choice)
            print("-------- Result: ---------")
            print(f"{self.execute_option(user_choice)}") 
            print("--------------------------")


    def printMenu(self):
        print("Choose the operation to perform")
        print("1. Sum single matrix")
        print("2. Sum two matrix")
        print("3. Sum two matrix by axis")
        print("4. Sum by pro")
        print("5. prod with scalar")
        print("6. Prod two matrix")
        print("7. Media mean")
        print("8. transpose")
        print("9. trace")
        print("10. Invert matrix")
        print("11. Determinant")
        print("12. Rank")
        print("13. Factorization LU")
        print("0. Exit")
        

    def get_user_choice(self):
        choice = input("Enter your choice (1-9): ")
        return choice

    def execute_option(self, user_choice):
        rtrVal = None
        if user_choice == '1':
            rtrVal = self.sum_single_matrix(self.A)
        elif user_choice == '2':
            rtrVal = self.sum_two_matrix(self.A, self.B)
        elif user_choice == '3':
            rtrVal = self.sum_two_matrix_by_axis(self.A, self.B, self.axis)
        elif user_choice == '4':
            rtrVal = self.prod_by_axis(self.A, self.B, self.axis)
        elif user_choice == '5':
            rtrVal = self.prod_with_scalar(self.A, self.scalar)
        elif user_choice == '6':
            rtrVal = self.prod_two_matrix(self.A, self.B)
        elif user_choice == '7':
            rtrVal = self.media_mean(self.A)
        elif user_choice == '8':
            rtrVal = self.transpose(self.A)
        elif user_choice == '9':
            rtrVal = self.trace(self.A)
        elif user_choice == '10':
            rtrVal = self.invertMatrix(self.A)
        elif user_choice == '11':
            rtrVal = self.determinant(self.A)
        elif user_choice == '12':
            rtrVal = self.rank(self.A)
        elif user_choice == '13':
            rtrVal = self.factorizationLU(self.A)
        elif user_choice == '0.1':
            rtrVal = self.showMenu()
        else:
            rtrVal = "Invalid choice. Please try again."
        return rtrVal
        
    def ask_user_details(self, user_choice):
        if user_choice == '1':
            self.ask_single_matrix()
        elif user_choice == '2':
            self.ask_double_matrix()
        elif user_choice == '3':
            self.ask_double_matrix_and_axis()
        elif user_choice == '4':
            self.ask_double_matrix_and_axis()
        elif user_choice == '5':
            self.ask_matrix_and_scalar()
        elif user_choice == '6':
            self.ask_double_matrix()
        elif user_choice == '7':
            self.ask_single_matrix()
        elif user_choice == '8':
            self.ask_single_matrix()
        elif user_choice == '9':
            self.ask_single_matrix()
        elif user_choice == '10':
            self.ask_single_matrix()
        elif user_choice == '11':
            self.ask_single_matrix()
        else:
            print("Invalid choice. Please try again.")

    def ask_single_matrix(self):
        if self.A is not None:
                regenerate = input("The matrix A is already generated. Do you want to regenerate it? (y/n): ")
                if regenerate.lower() == 'y':
                    self.A = generateMatrixByUser()
        else:
            self.A = generateMatrixByUser()
    
    def ask_double_matrix(self):
        if self.A is not None and self.B is not None:
                regenerate = input("The matrices A and B are already generated. Do you want to regenerate them? (y/n): ")
                if regenerate.lower() == 'y':
                    self.A = generateMatrixByUser()
                    self.B = generateMatrixByUser()
        else:
            self.A = generateMatrixByUser()
            self.B = generateMatrixByUser()

    def ask_matrix_and_scalar(self):
        if self.A is not None and self.scalar is not None:
                regenerate = input("The matrix A and the scalar value are already generated. Do you want to regenerate them? (y/n): ")
                if regenerate.lower() == 'y':
                    self.A = generateMatrixByUser()
                    self.scalar = float(input("Enter the scalar value: "))
        else:
            self.A = generateMatrixByUser()
            self.scalar = float(input("Enter the scalar value: "))
    
    def ask_double_matrix_and_axis(self):
        if self.A is not None and self.B is not None and self.axis is not None:
                regenerate = input("The matrices A and B and the axis are already generated. Do you want to regenerate them? (y/n): ")
                if regenerate.lower() == 'y':
                    self.A = generateMatrixByUser()
                    self.B = generateMatrixByUser()
                    self.axis = int(input("Enter the axis (0 or 1): "))
        else:
            self.A = generateMatrixByUser()
            self.B = generateMatrixByUser()
            self.axis = int(input("Enter the axis (0 or 1): "))


    def sum_single_matrix(self,A):
        return np.sum(A)

    def sum_two_matrix(self,A,B):
        return np.sum([A, B])

    def sum_two_matrix_by_axis(self, A,B,axis):
        if axis > 1:
            print("Invalid axis")
            return "Invalid axis"
        return np.sum([A, B], axis=axis)

    #matrix subtraction
    def matrix_subtraction(self,a, b):
        c = np.subtract(a, b)
        return c

    def prod_by_axis(self,A,B, axis):
        return np.prod([A, B], axis=axis)

    def prod_with_scalar(self,A, scalar):
        return scalar*A

    def prod_two_matrix(self,A,B):
        return A*B

    def prod_element_to_element(A,B):
        return A@B

    def media_mean(self,A):
        return np.mean(A)

    def transpose(self,A):
        return np.transpose(A)

    def trace(self,A):
        return np.trace(A)

    def invertMatrix(self,A):
        return np.linalg.inv(A)

    def determinant(self,A):
        return np.linalg.det(A)

    def rank(self,A):
        return np.linalg.matrix_rank(A)
    
    def factorizationLU(self,A):
        # Perform LU factorization
        result = {}
        lu, piv = sp.linalg.lu_factor(A)
        result["P"] = np.eye(len(A))[piv]
        # Extract the lower triangular matrix L
        result["L"] = np.tril(lu, k=-1) + np.eye(len(A))
        # Extract the upper triangular matrix U
        result["U"] = np.triu(lu)
        return result


def generateMatrixByUser():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter the element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    return np.array(matrix)