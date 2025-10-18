def pedir_lado():
    print("ingrese la longitud de un lado del cuadrado")
    longitud = int(input())
    return longitud

def calcular_area(l):
    area = (l**2)
    return area

def mostrar_mensaje(area):
    print (f"el area del cuadrado es: {area}cm²")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.Calcuar el area de otro cuadrado \n 2. salir del programa")
            menu_op = int(input())
            if menu_op == 1:
                lado = pedir_lado()
                area = calcular_area(lado)
                mostrar_mensaje(area)
            else:
                print("ha salido exitosamente del programa")
                break
            
#---------------ZONA DE CODIGO PRINCIPAL-----------
lado = pedir_lado()
area = calcular_area(lado)
mostrar_mensaje(area)
crear_menu()