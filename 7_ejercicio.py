def pedir_grados_celsius():
    print("ingrese los grados celsius que desea convertir a grados farenheit")
    grados_celsius = int(input())
    return grados_celsius

def convertir_a_grados_farenheit(celsius):
    conversion = ((celsius)* (9/5)) + 32
    return conversion

def mostrar_mensaje(conversion):
    print (f"la conversion a grados farenheit es: {conversion} °F")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.Calcular el volumen de otra esfera \n 2. salir del programa")
            menu_op = int(input())
            if menu_op == 1:
                celsius = pedir_grados_celsius()
                conversion = convertir_a_grados_farenheit(celsius)
                mostrar_mensaje(conversion)
            else:
                print("ha salido exitosamente del programa")
                break
            
#---------------ZONA DE CODIGO PRINCIPAL-----------
celsius = pedir_grados_celsius()
conversion = convertir_a_grados_farenheit(celsius)
mostrar_mensaje(conversion)
crear_menu()