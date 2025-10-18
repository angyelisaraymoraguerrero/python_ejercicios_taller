def pedir_numeros():
    print("ingrese el el precio del cual desea calcular el 10% de descuento:")
    num = int(input())
    return num 
    
def operar_numeros(num):
    des = num*0.1
    print(f"el 10% de descuento es:{des} ")
    mul = num-des
    return mul

def mostrar_mensaje(mul):
    print(f"el precio con el 10% de descuento es {mul}")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.hallar el descuento de otros precios \n2.salir del programa")
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