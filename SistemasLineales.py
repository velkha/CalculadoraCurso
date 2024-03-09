import sympy as sp
from sympy import linsolve
import numpy as np
from Matrix import generateMatrixByUser
import matplotlib.pyplot as plt
from Matrix import MatrixOperations

class LinearSystemOperations:
    def __init__(self):
        self.matrix = np.array([[1, 1, -1, 2], [1,-1, 1, 1], [3,1,-1,5]])
        self.system = None
        
    def showMenu(self):
        while True:
            print("Linear System Operations:")
            print("Symbols used: x.1, x.2, x.3, ... *do not use the symbols on the matrix*")   
            print("1. Generate Matrix")
            print("2. Solve System")
            print("3. System Equation Visualization")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.generate_matrix()
            elif choice == "2":
                if self.matrix is None:
                    print("Please generate a matrix first.")
                    continue
                self.solve_system(self.matrix)
            elif choice == "3":
                if self.matrix is None:
                    print("Please generate a matrix first.")
                    continue
                self.solve_system_equation(self.matrix)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def generate_matrix(self):
        self.matrix = generateMatrixByUser()
    
    def solve_system(self, A):
        rtrValue = None
        symbols_tuple = sp.symbols(' '.join([f'x.{i}' for i in range(1, len(A)+1)]))
        solution = linsolve(sp.Matrix((A)), symbols_tuple)
        if solution:
            rtrValue = solution
            print(f"Solution: of the system")
            print("A: ")
            print(A[:,:-1])
            print("B: ")
            print(A[:,-1:])
            print("Solution: ")
            for s in solution:
                print(s)
            print(f"Rank of A: {np.linalg.matrix_rank(A)}")
            print(f"Rank of AB: {np.linalg.matrix_rank(np.concatenate((A[:,:-1], A[:,-1:]), axis=1))}")
            print(f"Rank of B: {np.linalg.matrix_rank(A[:,-1:])}")
        else:
            rtrValue = "no solution found."
            print("No solution found.")
        
        return rtrValue
    
    def solve_system_equation(self, A):
        symbols_tuple = sp.symbols(' '.join([f'x{i}' for i in range(1, len(A)+1)]))
        equations = [sp.Eq(A[i, :-1].dot(symbols_tuple), A[i, -1]) for i in range(A.shape[0])]
        solutions = sp.solve(equations, symbols_tuple)

        print(f"Equations: {equations}")
        print(f"Solutions: {solutions}")
        print(f"Synmbols: {symbols_tuple}")
        return {solutions, equations}
    
    def calcularMinimosCuadrados(self, M):
        # A = np.array([[1, 1, -1, 2], [1,-1, 1, 1], [3,1,-1,5]])
        A = M[:,:-1]
        B = M[:,-1:]
        x, residuals, rank, s = np.linalg.lstsq(A, B, rcond=None)
        return x, residuals, rank, s

    
    

















