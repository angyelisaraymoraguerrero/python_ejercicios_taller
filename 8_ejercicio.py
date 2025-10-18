tasa_cambio = 0
dolares = 0

def pedir_datos():
    global dolares
    global tasa_cambio
    
    print("ingrese la cantidad de dolares que desea convertir a euros")
    dolares = int(input())
    print("ingrese la tasa de cambio co  la cual desea convertir los dolares a euros \n nota:la tasa de cambio del dia de hoy es 0.86")
    tasa_cambio = float(input())
    
def convertir_dolares_a_euros():
    conversion = dolares*tasa_cambio
    return conversion

def mostrar_mensaje(conversion):
    print(f"dolares:{dolares} * {tasa_cambio} = {conversion} euros")
    
def crear_menu():
    while True:
        print ("============MENU==========")
        print("1.realizar otra conversion \n 2.salir del programa")
        pregunta = int(input())
        if pregunta == 1:
            pedir_datos()
            conversion = convertir_dolares_a_euros()
            mostrar_mensaje(conversion)
        else:
            print("ha salido exitosamente del programa")
            break

#------------------ZONA DE CODIGO PRINCIPAL-------------------
pedir_datos()
conversion = convertir_dolares_a_euros()
mostrar_mensaje(conversion)
crear_menu()
    
    