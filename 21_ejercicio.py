num_1 = 0
num_2 = 0

def pedir_numeros():
    global num_1
    global num_2
    print("ingrese el primer numero que desea sumar:")
    num_1 = int(input())
    print("ingrese el segundo numero que desea sumar:")
    num_2 = int(input())
    
def sumar_numeros():
    suma = num_2+ num_1
    return suma

def mostrar_mensaje(suma):
    print(f"la suma de {num_1} + {num_2} da como resultado {suma}")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.Sumar otros numeros \n2.salir del programa")
            menu_op = int(input())
            if menu_op == 1:
                pedir_numeros()
                sumar =  sumar_numeros()
                mostrar_mensaje(sumar)
            else:
                print("ha salido exitosamente del programa")
                break
            
pedir_numeros()
sumar =  sumar_numeros()
mostrar_mensaje(sumar)
crear_menu()