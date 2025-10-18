def pedir_radio():
    print("ingrese el radio del circulo para poder calcular el area")
    radio = int(input())
    return radio

def calcular_area(radio):
    area = 3.1416 * (radio**2)
    return area

def mostrar_mensaje(area):
    print (f"el area del circulo es: {area} cm³")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.Calcular el volumen de otra esfera \n 2. salir del programa")
            menu_op = int(input())
            if menu_op == 1:
                radio = pedir_radio()
                area = calcular_area(radio)
                mostrar_mensaje(area)
            else:
                print("ha salido exitosamente del programa")
                break
            
#---------------ZONA DE CODIGO PRINCIPAL-----------
radio = pedir_radio()
area = calcular_area(radio)
mostrar_mensaje(area)
crear_menu()