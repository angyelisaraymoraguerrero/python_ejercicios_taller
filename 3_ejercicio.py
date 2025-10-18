longitud = 0
ancho = 0

def pedir_numeros():
    global longitud
    global ancho
    print("ingrese el ancho del rectangulo")
    ancho = int(input())
    print("ingrese la longitud del rectangulo")
    longitud = int(input())
    
def calcular_area():
    area = longitud*ancho
    return area

def mostrar_mensaje(area):
    print(f"el area del rectangulo es: {area}cm² ")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.Calcular el area de otro rectangulo \n 2. salir del programa")
            menu_op = int(input())
        
            match menu_op:
                case 1:
                    pedir_numeros()
                    calculo = calcular_area()
                    mostrar_mensaje(calculo)
                case 2:
                    print("ha salido del programa")
                    break
    
#------------------ZONA DE CODIGO PRINCIPAL----------------
pedir_numeros()
calculo = calcular_area()
mostrar_mensaje(calculo)
crear_menu()