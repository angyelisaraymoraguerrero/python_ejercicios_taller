def pedir_numeros():
    print("ingrese la hora:")
    num = int(input())
    return num 
    
def operar_numeros(num):
    mul = num*60
    return mul

def mostrar_mensaje(mul):
    print(f"la hora ingresada convertida a minutos es {mul}min")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.convertir otras horas a minutos \n2.salir del programa")
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