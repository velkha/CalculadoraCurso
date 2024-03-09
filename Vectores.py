import numpy as np

class VectorOperations:
    def __init__(self):
        self.vectorList = []
        #default value for vectorList
        self.vectorList.append(np.array([1,2,3,4,5]))
        self.vectorList.append(np.array([5,4,3,2,1]))
        self.vectorList.append(np.array([5,1,4,2,3]))
        self.scalar = 5

    def showMenu(self):
        self.printMenu()
        while True:
            rtrValue = None
            print("0.1 Show Menu")
            choice = input("Enter your choice: ")
            if choice == "0":
                break
            rtrValue = self.executeOption(choice)
            if rtrValue is not None:
                print("----------------- Result  -----------------") 
                print(rtrValue)
                print("----------------- End Result  -----------------")

    def printMenu(self):
        print("Menu:")
        print("1. Create Vectors")
        print("1.1 Create Scalars")
        print("2. Add Vectors")
        print("3. Subtract Vectors")
        print("4. Multiply Vectors")
        print("5. Divide Vectors")
        print("6. Dot Product")
        print("7. Cross Product")
        print("8. Scalar*vector")
        print("9. Norm")
        print("10. Distance between two points")
        print("11. Angle between two vectors")
        print("12. Orthogonal Projection")
        print("13. Octogonal Projection")
        print("14. Vectorial product")
        print("15. Mixed product")
        print("16. Calculate perpendicular vector")
        print("0. Exit")
    
    def executeOption(self, choice):
        rtrValue = None
        if choice == "1":
            if self.vectorList:
                print("Vector list already exists. Do you want to overwrite it? (y/n)")
                overwrite = input()
                if overwrite.lower() == "y":
                    self.vectorList = self.createVector()
            else:
                self.vectorList = self.createVector()
        elif choice == "1.1":  
            if self.scalar:
                print("Scalar already exists. Do you want to overwrite it? (y/n)")
                overwrite = input()
                if overwrite.lower() == "y":
                    self.scalar = float(input("Enter the scalar value: "))
            else:
                self.scalar = float(input("Enter the scalar value: "))
        elif choice == "2":
            if len(self.vectorList) >= 2:
                rtrValue = self.addVectors(
                    self.vectorList[0],
                    self.vectorList[1]
                )
            else:
                print("Insufficient vectors. Please create at least 2 vectors.")
        elif choice == "3":
            if len(self.vectorList) >= 2:
                rtrValue = self.subtractVector(
                    self.vectorList[0],
                    self.vectorList[1]
                )
            else:
                print("Insufficient vectors. Please create at least 2 vectors.")
        elif choice == "4":
            if len(self.vectorList) >= 2:
                rtrValue = self.multiplyVectors(
                    self.vectorList[0],
                    self.vectorList[1]
                )
            else:
                print("Insufficient vectors. Please create at least 2 vectors.")
        elif choice == "5":
            if len(self.vectorList) >= 2:
                rtrValue = self.divideVectors(
                    self.vectorList[0],
                    self.vectorList[1]
                )
            else:
                print("Insufficient vectors. Please create at least 2 vectors.")
        elif choice == "6":
            if len(self.vectorList) >= 2:
                rtrValue = self.dotProduct(
                    self.vectorList[0],
                    self.vectorList[1]
                )
            else:
                print("Insufficient vectors. Please create at least 2 vectors.")
        elif choice == "7":
            if len(self.vectorList) >= 2:
                rtrValue = self.crossProduct(
                    self.vectorList[0],
                    self.vectorList[1]
                )
            else:
                print("Insufficient vectors. Please create at least 2 vectors.")
        elif choice == "8":
            if len(self.vectorList) >= 1:
                rtrValue = self.scalarProduct(
                    self.vectorList[0]
                )
            else:
                print("Insufficient vectors. Please create at least 2 vectors.")
        elif choice == "9":
            if self.vectorList:
                rtrValue = self.norm(self.vectorList[0])
            else:
                print("No vectors created. Please create a vector.")
        elif choice == "10":
            if len(self.vectorList) >= 2:
               rtrValue = self.distanceBetweenPoints(
                    self.vectorList[0],
                    self.vectorList[1]
                )
            else:
                print("Insufficient vectors. Please create at least 2 vectors.")
        elif choice == "11":
            if len(self.vectorList) >= 2:
                rtrValue = self.angleBetweenVectors(
                    self.vectorList[0],
                    self.vectorList[1]
                )
            else:
                print("Insufficient vectors. Please create at least 2 vectors.")
        elif choice == "12":
            if len(self.vectorList) >= 2:
                rtrValue = self.orthogonalProjection(
                    self.vectorList[0],
                    self.vectorList[1]
                )
            else:
                print("Insufficient vectors. Please create at least 2 vectors.")
        elif choice == "13":
            if len(self.vectorList) >= 2:
                rtrValue = self.octogonalProjection(
                    self.vectorList[0],
                    self.vectorList[1]
                )
            else:
                print("Insufficient vectors. Please create at least 2 vectors.")
        elif choice == "14":
            if len(self.vectorList) >= 2:
                rtrValue = self.vectorialProduct(
                    self.vectorList[0],
                    self.vectorList[1]
                )
            else:
                print("Insufficient vectors. Please create at least 2 vectors.")
        elif choice == "15":
            if len(self.vectorList) >= 3:
               rtrValue = self.mixedProduct(
                    self.vectorList[0],
                    self.vectorList[1],
                    self.vectorList[2]
                )
            else:
                print("Insufficient vectors. Please create at least 3 vectors.")
        elif choice == "16":
            if len(self.vectorList) >= 1:
                rtrValue = self.calculatePerpendicularVector(
                    self.vectorList[0]
                )
            else:
                print("Insufficient vectors. Please create at least 1 vector.")

        elif choice == "0.1":
            self.printMenu()
        else:
            print("Invalid choice. Please try again.")
        
        return rtrValue

             
    def createVector(self):
        print("How many vectors do you want to create?")
        n = int(input())
        vectorList = []
        for i in range(n):
            print(f"Enter the elements of vector {i+1} separated by comas (,):")
            elements = input().split(',')
            vectorList.append(np.array(elements, dtype=int))
        print(vectorList)
        return vectorList

    def addVectors(self,vector1,vector2):
        return(vector1 + vector2)

    def subtractVector(self,vector1,vector2):
        return(vector1 - vector2)

    def multiplyVectors(self,vector1,vector2):
        return(vector1 * vector2)

    def divideVectors(self,vector1,vector2):
        return(vector1 / vector2)

    def dotProduct(self,vector1,vector2):
        return(np.dot(vector1, vector2))

    def crossProduct(self,vector1,vector2):
        #check if the vectors are 3D or 2D
        if (len(self.vectorList[0]) == 3 and len(self.vectorList[1]) == 3 or 
            len(self.vectorList[0]) == 2 and len(self.vectorList[1]) == 2):
            return(np.cross(vector1, vector2))
        else:
            return "The vectors must be 2D or 3D"
        

    def scalarProduct(self,vector1):
        vector1 = np.array(self.vectorList[0], dtype=int)
        scalar = self.scalar
        return(vector1 * scalar)

    def norm(self,vector1,):
        vector1 = np.array(self.vectorList[0], dtype=int)
        return(np.linalg.norm(vector1))

    def distanceBetweenPoints(self,vector1,vector2):
        return(np.linalg.norm(vector1 - vector2))

    def angleBetweenVectors(self,vector1,vector2):
        dot_product = np.dot(vector1, vector2)
        norm_product = np.linalg.norm(vector1) * np.linalg.norm(vector2)
        angle = np.arccos(dot_product / norm_product)
        return(np.degrees(angle))

    def orthogonalProjection(self,vector1,vector2):
        projection = np.dot(vector1, vector2) / np.linalg.norm(vector2)**2 * vector2
        return(projection)

    def octogonalProjection(self,vector1,vector2):
        projection = vector1 - np.dot(vector1, vector2) / np.linalg.norm(vector2)**2 * vector2
        return(projection)

    def vectorialProduct(self,vector1,vector2):
        if (len(self.vectorList[0]) == 3 and len(self.vectorList[1]) == 3 or 
            len(self.vectorList[0]) == 2 and len(self.vectorList[1]) == 2):
            return(np.cross(vector1, vector2))
        else:
            return "The vectors must be 2D or 3D"

    def mixedProduct(self,vector1,vector2,vector3):
        if (len(self.vectorList[0]) == 3 and len(self.vectorList[1]) == 3 and len(self.vectorList[2]) == 3 or 
            len(self.vectorList[0]) == 2 and len(self.vectorList[1]) == 2 and len(self.vectorList[2]) == 2):
            return(np.dot(np.cross(vector1, vector2), vector3))
        else:
            return "The vectors must be 2D or 3D"
    
    def calculatePerpendicularVectors(self, vector1):
        if len(vector1) < 2:
            print("Vector dimension must be at least 2.")
            return None
        
        # Create a zero vector with the same dimension as vector1
        perpendicular_vector = np.zeros_like(vector1)
        
        # Calculate the perpendicular vector
        perpendicular_vector[0] = -vector1[1]
        perpendicular_vector[1] = vector1[0]
        perpendicular_vector[2] = vector1[2]

        return perpendicular_vector

    def calculatePerpendicularVector(self, v):
        # Definir un vector de la base canónica que no sea paralelo a v
        if not np.allclose(v, [1, 0, 0]):
            e = np.array([1, 0, 0])
        else:
            e = np.array([0, 1, 0])

        # Calcular el vector perpendicular usando el producto cruz
        return np.cross(v, e)

    