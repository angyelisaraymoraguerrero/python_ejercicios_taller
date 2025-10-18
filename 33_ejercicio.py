def pedir_kilometros():
    print("ingrese los kilometros  que desea convertir a millas")
    kilometros = int(input())
    return kilometros

def convertir_a_millas(km):
    conversion = km * 0.621371 
    return conversion

def mostrar_mensaje(conversion):
    print (f"la conversion de {kilometros}km a millas es: {conversion}millas ")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.Convertir otra cantidad de kilometros a millas \n 2. salir del programa")
            menu_op = int(input())
            if menu_op == 1:
                kilometros = pedir_kilometros()
                conversion = convertir_a_millas(kilometros)
                mostrar_mensaje(conversion)
            else:
                print("ha salido exitosamente del programa")
                break
            
#---------------ZONA DE CODIGO PRINCIPAL-----------
kilometros = pedir_kilometros()
conversion = convertir_a_millas(kilometros)
mostrar_mensaje(conversion)
crear_menu()