num_1 = 0
num_2 = 0

def pedir_numeros():
    global num_1
    global num_2
    print("ingrese el primer numero que desea restar:")
    num_1 = int(input())
    print("ingrese el segundo numero que desea restar:")
    num_2 = int(input())
    
def restar_numeros():
    resta = num_2 - num_1
    return resta

def mostrar_mensaje(resta):
    print(f"la resta de {num_1} - {num_2} da como resultado {resta}")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.restar otros numeros \n2.salir del programa")
            menu_op = int(input())
            if menu_op == 1:
                pedir_numeros()
                restar =  restar_numeros()
                mostrar_mensaje(restar)
            else:
                print("ha salido exitosamente del programa")
                break
            
pedir_numeros()
restar =  restar_numeros()
mostrar_mensaje(restar)
crear_menu()