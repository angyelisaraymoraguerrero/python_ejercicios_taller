def pedir_numeros():
    print("ingrese el radio del circulo:")
    num = int(input())
    return num 
    
def operar_numeros(num):
    mul = 2*(3.1416)*num
    return mul

def mostrar_mensaje(mul):
    print(f"la circunferencia del circulo es {mul}cm")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.hallar la circunferencia de otros circulos \n2.salir del programa")
            menu_op = int(input())
            if menu_op == 1:
                pedir = pedir_numeros()
                operar =  operar_numeros(pedir)
                mostrar_mensaje(operar)
            else:
                print("ha salido exitosamente del programa")
                break
            
pedir = pedir_numeros()
operar =  operar_numeros(pedir)
mostrar_mensaje(operar)
crear_menu()