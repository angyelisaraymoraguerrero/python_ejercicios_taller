

def pedir_datos():
    print("ingrese la longitud de un lado del cubo del cual desea calcular el volumen")
    longitud_lado = int(input())
    return longitud_lado
    
def calcular_volumen(lado):
    volumen = lado**3
    return volumen

def mostrar_mensaje(vol):
    print(f"el volumen de la piramide es de: {vol} cm³")
    
def crear_menu():
    while True:
        print ("============MENU==========")
        print("1.calcular el volumen de otra piramide? \n 2.salir")
        pregunta = int(input())
        if pregunta == 1:
            lado_cubo = pedir_datos()
            vol = calcular_volumen(lado_cubo)
            mostrar_mensaje(vol)
        else:
            print("ha salido exitosamente del programa")
            break
            
#--------------------ZONA DE CODIGO PRINCIPAL-------------------
lado_cubo = pedir_datos()
vol = calcular_volumen(lado_cubo)
mostrar_mensaje(vol) 
crear_menu()          
            