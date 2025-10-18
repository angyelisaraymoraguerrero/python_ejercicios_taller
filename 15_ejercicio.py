base = 0
altura = 0

def pedir_numeros():
    global base
    global altura
    print("ingrese la base del paralelogramo del rectangulo")
    base = int(input())
    print("ingrese la altura del del paralelogramo")
    altura = int(input())
    
def calcular_area():
    area = base*altura
    return area

def mostrar_mensaje(area):
    print(f"el area del paralelogramo es: {area}cm² ")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.Calcular el area de otro paralelogramo \n2. salir del programa")
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