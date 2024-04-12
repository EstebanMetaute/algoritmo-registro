import os

def fnt_limpiar_pantalla():
    os.system('cls')

class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto.cantidad
        return -1

inventario = Inventario()

while True:
    print('1. Agregar producto')
    print('2. Buscar producto')
    print('3. Salir')
    opcion = int(input('Elejir una opcion: '))


    if opcion == 1:
        nombre = input('Ingrese nombre del producto: ')
        cantidad = int(input('Ingrese cantidad del producto: '))
        producto = Producto(nombre, cantidad)
        inventario.agregar_producto(producto)
        enter = input('\n<<<ENTER>>>')
        fnt_limpiar_pantalla()

    elif opcion == 2:
        nombre = input('Ingrese nombre del producto: ')
        cantidad = inventario.buscar_producto(nombre)
        if cantidad == -1:
            print('El producto no fue encontrado')
            enter = input('\n<<<ENTER>>>')
            fnt_limpiar_pantalla()
        else:
            print(f"Cantidad disponible: {cantidad}")
            enter = input('\n<<<ENTER>>>')
            fnt_limpiar_pantalla()
    elif opcion == 3:
        break
    else:
        print("Opción inválida")
        enter = input('\n<<<ENTER>>>')
        fnt_limpiar_pantalla()