def pedir_numeros():
    print("ingrese la cantida de dinero de la cual desea calcular el 5% de interes:")
    num = int(input())
    return num 
    
def operar_numeros(num):
    mul = (num*0.05)
    return mul

def mostrar_mensaje(mul):
    print(f"el 5% de interes de la cantidad ingresada es {mul}")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.hallar el interes de otros montos de dinero \n2.salir del programa")
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