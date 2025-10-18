base = 0
altura = 0

def pedir_base_altura():
    print("ingrese la base del triangulo:")
    global base 
    base = int(input())
    print("ingrese la altura del triangulo:")
    global altura 
    altura = int(input())
    
def calcular_area_triangulo():
    area = (base*altura)/2
    return area

def mostrar_mensaje(area):
    print(f"el area del triangulo es:{area}cm²")
    
def menu():  
        while True: 
            print("==========MENU==========")
            print ("1.Calcular el area de otro triangulo \n 2. salir del programa")
            menu_op = int(input())
        
            match menu_op:
                case 1:
                    pedir_base_altura()
                    calculo = calcular_area_triangulo()
                    mostrar_mensaje(calculo)
                
                case 2:
                    print("ha salido del programa")
                    break
        
#------------------ZONA DE CODIGO PRINCIPAL---------------------
pedir_base_altura()
calculo = calcular_area_triangulo()
mostrar_mensaje(calculo)
menu()
        