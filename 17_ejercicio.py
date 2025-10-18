def pedir_datos():
    print("ingrese las pulgadas que desea convertir a centimetros")
    libras = int(input())
    return libras

def convertir(libras):
    conversion = libras * 0.453592 
    return conversion

def mostrar_mensaje(conversion, libras):
    print (f"la conversion de {libras} libras a kilogramos es: {conversion}kg")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.Convertir otra cantidad de libras a kilogramos \n2. salir del programa")
            menu_op = int(input())
            if menu_op == 1:
                libras = pedir_datos()
                conversion =  convertir(libras)
                mostrar_mensaje(conversion, libras)
            else:
                print("ha salido exitosamente del programa")
                break
            
#---------------ZONA DE CODIGO PRINCIPAL-----------
libras = pedir_datos()
conversion =  convertir(libras)
mostrar_mensaje(conversion, libras)
crear_menu()