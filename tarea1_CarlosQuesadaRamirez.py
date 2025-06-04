import math

def cantidadVectores():
    while True:
        try:
            cantidadVectores = int(input("Ingrese la cantidad de vectores que desea sumar: "))
            if cantidadVectores > 0:
                return cantidadVectores
            else:
                print("Cantidad inválida. El número debe ser mayor que 0.")
        except ValueError:
            print("El número ingresado no puede ser impar. Por favor, intentelo de nuevo.")

def metodoIngresoVector():
    def ingresoVector():
        while True:
            print("Seleccione el método que desea utilizar para ingresar el vector:")
            print("1. Ingresar por magnitud y dirección")
            print("2. Imgresar por componentes")
            print("Respuesta: ")
        