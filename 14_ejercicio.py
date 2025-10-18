def pedir_pulgadas():
    print("ingrese las pulgadas que desea convertir a centimetros")
    pulgadas = int(input())
    return pulgadas

def convertir_a_centimetros(pul):
    conversion = pul * 2.54 
    return conversion

def mostrar_mensaje(conversion, pulgadas):
    print (f"la conversion de {pulgadas} pulgadas a centimetros es: {conversion}cm")
    
def crear_menu():
    while True: 
            print("==========MENU==========")
            print ("1.Convertir otra cantidad de kilometros a millas \n2. salir del programa")
            menu_op = int(input())
            if menu_op == 1:
                pulgadas = pedir_pulgadas()
                conversion =  convertir_a_centimetros(pulgadas)
                mostrar_mensaje(conversion, pulgadas)
            else:
                print("ha salido exitosamente del programa")
                break
            
#---------------ZONA DE CODIGO PRINCIPAL-----------
pulgadas = pedir_pulgadas()
conversion =  convertir_a_centimetros(pulgadas)
mostrar_mensaje(conversion, pulgadas)
crear_menu()