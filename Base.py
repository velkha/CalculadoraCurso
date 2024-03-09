from Matrix import MatrixOperations
from SistemasLineales import LinearSystemOperations
from Vectores import VectorOperations
from EspaciosVectoriales import VectorSpacesOperations
def show_menu():
    print("Menu:")
    print("1. Matrix ")
    print("2. Sistemas Lineales ")
    print("3. Vectores")
    print("4. Espacios Vectoriales")
    print("0. Exit")

def get_user_choice():
    choice = input("Enter your choice (1-3): ")
    return choice

def execute_option(choice):
    if choice == "1":
        mo = MatrixOperations()
        mo.showMenu()
    elif choice == "2":
        lso = LinearSystemOperations()
        lso.showMenu()
    elif choice == "3":
        vo = VectorOperations()
        vo.showMenu()
    elif choice == "4":
        vso = VectorSpacesOperations()
        vso.showMenu()
    else:
        print("Invalid choice")

while True:
    show_menu()
    user_choice = get_user_choice()
    if user_choice == '0':
        break
    execute_option(user_choice)