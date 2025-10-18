longitud_base = 0
altura_triangulo = 0
altura_prisma = 0

def pedir_datos():
    global longitud_base 
    global altura_triangulo
    global altura_prisma
    
    print("ingrese la longitud de la base de la piramede de la cual quiere calcular el volumen")
    longitud_base = int(input())
    
    print("ingrese la altura del triangulo del prisma triangular del cual quiere calcular el volumen")
    altura_triangulo = int(input())

    print("ingrese la altura de del prisma triangular del cual quiere calcular el volumen")
    altura_prisma = int(input())
    
def calcular_volumen():
    volumen = ((longitud_base*altura_triangulo)/2)*altura_prisma
    return volumen

def mostrar_mensaje(vol):
    print(f"el volumen del prisma es de: {vol} cm³")
    
def crear_menu():
    while True:
        print ("============MENU==========")
        print("1.calcular el volumen de otro prisma triangular? \n 2.salir")
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
            