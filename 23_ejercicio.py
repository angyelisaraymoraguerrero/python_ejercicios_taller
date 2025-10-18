num_1 = 0
num_2 = 0

def pedir_numeros():
    global num_1
    global num_2
    print("ingrese el primer numero que desea multiplicar:")
    num_1 = int(input())
    print("ingrese el segundo numero que desea multiplicar:")
    num_2 = int(input())
    
def operar_numeros():
    mul = num_2 * num_1
    return mul

def mostrar_mensaje(mul):
    print(f"la multiplicacion de {num_1} x {num_2} da como resultado {mul}")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.multiplicar otros numeros \n2.salir del programa")
            menu_op = int(input())
            if menu_op == 1:
                pedir_numeros()
                operar =  operar_numeros()
                mostrar_mensaje(operar)
            else:
                print("ha salido exitosamente del programa")
                break
            
pedir_numeros()
operar =  operar_numeros()
mostrar_mensaje(operar)
crear_menu()