import math

def menu ():
    print("1. Registrar producto")
    print("2. Listar todos los productos")
    print("3. Buscar productos por categoría")
    print("4. Calcular el precio promedio de los productos")
    print("5. Salir del programa y guardar")
    

def registro_producto():
    lista = []
    nombre = input("ingrese el nombre del producto: ")
    categoria = input("ingrese la categoria del producto: ")
    cantidad = input("ingrese la cantidad del productos: ")

    registro_producto = [nombre, categoria, cantidad]
    
    
def precio_promedio():
    promedio_producto = ()