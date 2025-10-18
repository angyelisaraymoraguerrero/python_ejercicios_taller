num_1 = 0
num_2 = 0

def pedir_numeros():
    global num_1
    global num_2
    print("ingrese el primer numero del cual desea obtener el residuo de la division:")
    num_1 = int(input())
    print("ingrese el segundo numero del cual desea obtener el residuo de la division:")
    num_2 = int(input())
    
def operar_numeros():
    mul = num_1 % num_2
    return mul

def mostrar_mensaje(div):
    print(f"la dividision de {num_1} / {num_2} da como residuo: {div}")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.dividir otros numeros \n2.salir del programa")
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