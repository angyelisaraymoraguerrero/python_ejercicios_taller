num_1 = 0
num_2 = 0

def pedir_numeros():
    global num_1
    global num_2
    print("ingrese el primer numero:")
    num_1 = float(input())
    print("ingrese el segundo numero:")
    num_2 = float(input())
    
def operar_numeros():
    mul = (num_1+num_2)/2
    return mul

def mostrar_mensaje(mul):
    print(f"el promedio de {num_1} y {num_2} es {mul}")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.calcular el promedio de otro par de numeros \n2.salir del programa")
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