def pedir_radio():
    print("ingrese el radio de la esfera para poder calcular el volumen")
    radio = int(input())
    return radio

def calcular_volumen(radio):
    #cal_volumen = (4/3)
    cal_volumen = (4/3)*(3.1416)*(radio**3)
    return cal_volumen

def mostrar_mensaje(volumen):
    print (f"el volumen de la esfera es: {volumen} cm³")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.Calcular el volumen de otra esfera \n 2. salir del programa")
            menu_op = int(input())
            if menu_op == 1:
                radio = pedir_radio()
                vol = calcular_volumen(radio)
                mostrar_mensaje(vol)
            else:
                print("ha salido exitosamente del programa")
                break
            
#---------------ZONA DE CODIGO PRINCIPAL-----------
radio = pedir_radio()
calcular = calcular_volumen(radio)
mostrar_mensaje(calcular)
crear_menu()