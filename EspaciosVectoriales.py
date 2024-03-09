from Vectores import VectorOperations
from Matrix import MatrixOperations
from SistemasLineales import LinearSystemOperations
import numpy as np
class VectorSpacesOperations:
    def __init__(self):
        self.vo = VectorOperations()
        self.mo = MatrixOperations()
        self.lso = LinearSystemOperations()
        self.vectorSpaces = []
        #initialize 2 default vector spaces
        V1 = [np.array([1, 0]), np.array([0, 1])]
        V2 = [np.array([1, 1]), np.array([-1, -1])]
        self.vectorSpaces.append(V1)
        self.vectorSpaces.append(V2)
        

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
        print("1. Create vector space")
        print("2. Check if a set is a subspace")
        print("3. Check if a set is linearly independent")
        print("4. Check if a set is a basis")
        print("5. Check if a set is orthogonal")
        print("6. Check if a set is orthonormal")
        print("7. Calculate dimension")
        print("8. Calculate rank")
        print("9. Change base")
        print("10. Inverse base")
        print("11. Get base")
        print("12. Suma Directa de Espacios Vectoriales")
        print("13. Producto Cartesiano de Espacios Vectoriales")
        print("14. Calcular Coordenadas")
        print("0. Exit")

    def get_user_choice(self):
        choice = input("Enter your choice (0-14): ")
        return choice

    def execute_option(self, user_choice):
        rtrVal = None
        if user_choice == '1':
            rtrVal = self.create_vector_space()
        elif user_choice == '2':
            rtrVal = self.is_subspace(
                self.vectorSpaces[0], self.vectorSpaces[1]
            )
        elif user_choice == '3':
            rtrVal = self.is_linearly_independent(
                self.vectorSpaces[0]
            )
        elif user_choice == '4':
            rtrVal = self.is_basis(
                self.vectorSpaces[0], self.vectorSpaces[1]
            )
        elif user_choice == '5':
            rtrVal = self.is_orthogonal(
                self.vectorSpaces[0]
            )
        elif user_choice == '6':
            rtrVal = self.is_orthonormal(
                self.vectorSpaces[0]
            )
        elif user_choice == '7':
            rtrVal = self.calculateDimension(
                self.vectorSpaces[0]
            )
        elif user_choice == '8':
            rtrVal = self.calculateRank(
                self.vectorSpaces[0]
            )
        elif user_choice == '9':
            rtrVal = self.changeBase(
                self.vectorSpaces[0], self.vectorSpaces[1]
            )
        elif user_choice == '10':
            rtrVal = self.inverseBase(
                self.vectorSpaces[0]
            )
        elif user_choice == '11':
            rtrVal = self.getBase(
                self.vectorSpaces[0]
            )
        elif user_choice == '12':
            rtrVal = self.sumaDirectaEV(
                self.vectorSpaces[0], self.vectorSpaces[1]
            )
        elif user_choice == '13':
            rtrVal = self.productoCartesianoEV(
                self.vectorSpaces[0], self.vectorSpaces[1]
            )
        elif user_choice == '14':
            rtrVal = self.calcular_coordenadas(
                self.vectorSpaces[0], self.vectorSpaces[1]
            )
        elif user_choice == '0.1':
            self.printMenu()
        else:
            print("Invalid choice")
        return rtrVal

    def ask_user_details(self, user_choice):
        pass

    def create_vector_space(self):
        print("How many vector spaces do you want to create?") 
        n = int(input())
        for i in range(n):
            print(f"Creating vector space {i+1}: ")
            self.vectorSpaces.append(self.vo.createVector())

    def is_subspace(self, vector_space, subspace):
        # Check if zero vector in subspace
        zero_vector = np.zeros_like(vector_space[0])
        if not any(np.array_equal(zero_vector, vec) for vec in subspace):
            return False

        # Check closure under addition and scalar multiplication
        for v1 in subspace:
            for v2 in subspace:
                # Check closure under addition
                if not any(np.array_equal(v1 + v2, vec) for vec in vector_space):
                    return False
                # Check closure under scalar multiplication
                for scalar in range(-10, 10):  # Check for a range of scalars
                    if not any(np.array_equal(scalar * v1, vec) for vec in vector_space):
                        return False

        return True
    
    def is_linearly_independent(self, vector_space):
        # Check if zero vector in vector space
        zero_vector = np.zeros_like(vector_space[0])
        if any(np.array_equal(zero_vector, vec) for vec in vector_space):
            return False

        # Check if the vectors are linearly independent
        for i in range(len(vector_space)):
            for j in range(len(vector_space)):
                if i != j:
                    if np.array_equal(vector_space[i], vector_space[j]):
                        return False
                    if np.array_equal(vector_space[i], -1 * vector_space[j]):
                        return False
        return True

    def is_basis(self, vector_space, subspace):
        return self.is_subspace(vector_space, subspace) and self.is_linearly_independent(subspace)
    
    def is_orthogonal(self, vector_space):
        for i in range(len(vector_space)):
            for j in range(len(vector_space)):
                if i != j:
                    if np.dot(vector_space[i], vector_space[j]) != 0:
                        return False
        return True

    def is_orthonormal(self, vector_space):
        return self.is_orthogonal(vector_space) and all(np.linalg.norm(vec) == 1 for vec in vector_space)
    
    def calculateDimension(self, vector_space):
        return len(vector_space)
    
    def calculateRank(self, vector_space):
        return np.linalg.matrix_rank(vector_space)
    
    def changeBase(self, vector_space, new_base):
        return np.linalg.solve(vector_space, new_base)
    
    def inverseBase(self, vector_space):
        return np.linalg.inv(vector_space)
    
    def getBase(self, vector_space):
        return np.linalg.eig(vector_space)
    def sumaDirectaEV(self, U, V):
        # Verificar que la intersección de U y V es solo el vector cero
        # interseccion = [vec for vec in U if vec in V and not np.allclose(vec, 0)]
        interseccion = [vec for vec in U if any(np.array_equal(vec, v) for v in V) and not np.allclose(vec, 0)]
        if interseccion:
            return None  # U y V no son una suma directa

        # Calcular la suma directa
        suma_directa = [u + v for u in U for v in V]

        return suma_directa
    
    def productoCartesianoEV(self, U, V):
        return [(u, v) for u in U for v in V]

    def calcular_coordenadas(self, base, vector):
        # Convertir la base a una matriz
        base_matrix = np.column_stack(base)
        # Resolver el sistema de ecuaciones lineales para obtener las coordenadas
        coordenadas = np.linalg.solve(base_matrix, vector)
        return coordenadas