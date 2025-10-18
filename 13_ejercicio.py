longitud_base = 0
ancho_base = 0
altura = 0

def pedir_datos():
    global longitud_base 
    global ancho_base
    global altura
    
    print("ingrese la longitud de la base de la piramede de la cual quiere calcular el volumen")
    longitud_base = int(input())
    
    print("ingrese el ancho de la base de la piramede de la cual quiere calcular el volumen")
    ancho_base = int(input())

    print("ingrese la altura de la piramide del cual quiere calcular el volumen")
    altura = int(input())
    
def calcular_volumen():
    volumen = (longitud_base*ancho_base*altura)/3
    return volumen

def mostrar_mensaje(vol):
    print(f"el volumen de la piramide es de: {vol} cm³")
    
def crear_menu():
    while True:
        print ("============MENU==========")
        print("1.calcular el volumen de otra piramide? \n 2.salir")
        pregunta = int(input())
        if pregunta == 1:
            pedir_datos()
            vol = calcular_volumen()
            mostrar_mensaje(vol)
        else:
            print("ha salido exitosamente del programa")
            break
            
#--------------------ZONA DE CODIGO PRINCIPAL-------------------
pedir_datos()
vol = calcular_volumen()
mostrar_mensaje(vol) 
crear_menu()          
            