from utilidades import menu,registro_producto

menu()
opcion = int(input("ingrese la opcion que necesite: "))

while True:
    try:
        if opcion == 1:
            registro_producto()
        elif opcion == 2:
            registro_producto()
        elif opcion == 3:
            
        elif opcion == 4:
            
        elif opcion == 5:
            print("Uste ha salido del programa y su archivo se guardo exitosamente!")
            break
        else:
            print("opcion invalida!, ingrese una opcion de 1-5")
        
        
    except ValueError:
        opcion = int(input("Dato invalido! ingrese solo numeros, escribe 1 para continuar: "))
 
    except ZeroDivisionError:
        opcion = int(input("Dato invalido! No puedes ingresar 0, Escribe 1 para continuar: "))