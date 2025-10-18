radio = 0
altura = 0

def pedir_numeros():
    global radio
    global altura
    print("ingrese el radio del cilindro del cual desea calcular el volumen:")
    radio = int(input())
    print("ingrese la altura del cilindro del cual desea calcular el volumen:")
    altura = int(input())
    
def calcular_volumen():
    cal_area = (3.1416)*(radio**2)*(altura)
    return cal_area

def mostrar_mensaje(area):
    print(f"el area del rectangulo es de :{area}cm³")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.Calcular el volumen de otra esfera \n 2. salir del programa")
            menu_op = int(input())
            if menu_op == 1:
                pedir_numeros()
                calcular = calcular_volumen()
                mostrar_mensaje(calcular)
            else:
                print("ha salido exitosamente del programa")
                break
            
#--------------------ZONA DE CODIGO PRINCIPAL------------------
pedir_numeros()
calcular = calcular_volumen()
mostrar_mensaje(calcular)
crear_menu()
    