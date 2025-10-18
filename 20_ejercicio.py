def pedir_datos():
    print("ingrese las pulgadas que desea convertir a centimetros")
    litros = int(input())
    return litros

def convertir(litros):
    conversion = litros * 0.264172 
    return conversion

def mostrar_mensaje(conversion, litros):
    print (f"la conversion de {litros} litros a galones es: {conversion}galones")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.Convertir otra cantidad de litros a galones \n2. salir del programa")
            menu_op = int(input())
            if menu_op == 1:
                cantidad_litros = pedir_datos()
                conversion =  convertir(cantidad_litros)
                mostrar_mensaje(conversion, cantidad_litros)
            else:
                print("ha salido exitosamente del programa")
                break
            
#---------------ZONA DE CODIGO PRINCIPAL-----------
libras = pedir_datos()
conversion =  convertir(libras)
mostrar_mensaje(conversion, libras)
crear_menu()