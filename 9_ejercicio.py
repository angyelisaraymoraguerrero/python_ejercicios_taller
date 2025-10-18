base_mayor = 0
base_menor = 0
altura = 0

def pedir_datos():
    global base_mayor
    global base_menor
    global altura
    
    print("ingree la base mayor del trapecio del cual quiere calcular el area")
    base_mayor = int(input())
    
    print("ingrese la base menor del trapecio del cual quiere calcular el area")
    base_menor = int(input())

    print("ingrese la altura del trapecio del cual quiere calcular el area")
    altura = int(input())
    
def calcular_area():
    area = ((base_mayor+base_menor)*altura)/2
    return area

def mostrar_mensaje(area):
    print(f"el area del trapecio es de: {area} cm²")
    
def crear_menu():
    while True:
        print ("============MENU==========")
        print("1.calcular el volumen de otro trapecio? \n 2.salir")
        pregunta = int(input())
        if pregunta == 1:
            pedir_datos()
            area = calcular_area()
            mostrar_mensaje(area)
        else:
            print("ha salido exitosamente del programa")
            break
            
#--------------------ZONA DE CODIGO PRINCIPAL-------------------
pedir_datos()
area = calcular_area()
mostrar_mensaje(area)  
crear_menu()          
            