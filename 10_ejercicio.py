longitud = 0
base = 0
altura = 0

def pedir_datos():
    global longitud
    global base
    global altura
    
    print("ingrese la longitud  del prisma rectangular del cual quiere calcular el volumen")
    longitud = int(input())
    
    print("ingrese el ancho del prisma rectangular del cual quiere calcular el volumen")
    base = int(input())

    print("ingrese la altura del prisma rectangular del cual quiere calcular el volumen")
    altura = int(input())
    
def calcular_volumen():
    volumen = longitud*base*altura
    return volumen

def mostrar_mensaje(vol):
    print(f"el area del trapecio es de: {vol} cm³")
    
def crear_menu():
    while True:
        print ("============MENU==========")
        print("1.calcular el volumen de otro prisma rectangular? \n 2.salir")
        pregunta = int(input())
        if pregunta == 1:
            pedir_datos()
            volumen = calcular_volumen()
            mostrar_mensaje(volumen)
        else:
            print("ha salido exitosamente del programa")
            break
            
#--------------------ZONA DE CODIGO PRINCIPAL-------------------
pedir_datos()
volumen = calcular_volumen()
mostrar_mensaje(volumen) 
crear_menu()          
            