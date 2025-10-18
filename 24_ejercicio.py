def pedir_numeros():
    print("ingrese el numero que desea elevar al cuadrado:")
    num = int(input())
    return num 
    
def operar_numeros(num):
    mul = num**2
    return mul

def mostrar_mensaje(mul, num):
    print(f"el numero {num} elvado al cuadrado da como  resultado {mul}")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.multiplicar otros numeros \n2.salir del programa")
            menu_op = int(input())
            if menu_op == 1:
                pedir = pedir_numeros()
                operar =  operar_numeros(pedir)
                mostrar_mensaje(operar, pedir)
            else:
                print("ha salido exitosamente del programa")
                break
            
pedir = pedir_numeros()
operar =  operar_numeros(pedir)
mostrar_mensaje(operar, pedir)
crear_menu()