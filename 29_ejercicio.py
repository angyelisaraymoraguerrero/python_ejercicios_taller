def pedir_numeros():
    print("ingrese el numero del cual desea saber si es para o impar:")
    num = int(input())
    return num 
    
def operar_numeros(num):
    if num%2==0:
        tipo_num=("el numero es par")
    else:
        tipo_num=("el numero es impar")
        
    return tipo_num

def mostrar_mensaje(tipo, num):
    print(f"el numero {num} es " + tipo )
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.verificar si otro numero es par o impar \n2.salir del programa")
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