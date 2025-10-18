radio_base = 0
altura_cono = 0

def pedir_datos():
    global radio_base
    global altura_cono
    
    print("ingrese el radio de la base del cono del cual se quiere calcular el volumen")
    radio_base = int(input())
    
    print("ingrese la altura del cono del cual se quiere calcular el volumen")
    altura_cono = int(input())
    
def calcular_volumen():
    volumen = (1/3)*(3.1416)*(radio_base**2)*(altura_cono)
    return volumen

def mostrar_mensaje(volumen):
    print(f"el volumen del cono es de: {volumen}cm³")
    
def crear_menu():
    while True:
        print ("============MENU==========")
        print("1.calcular el volumen de otro cono? \n 2.salir")
        pregunta = int(int(input()))
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
            