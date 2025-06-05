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
            opcion = input()

            if opcion == '1':
                return ingresoPorMagnitudDireccion()
            elif opcion == '2':
                return ingresoPorComponentes()
            else:
                print("Opción inválida. Por favor, intente de nuevo.")

def ingresoPorMagnitudDireccion():
    try:
        magnitud = float(input("Ingrese la magnitud del vector: "))
        angulo = float(input("Ingrese el ángulo del vector (en grados): "))
        anguloRadiantes = math.radians(angulo)
        ladoX = magnitud * math.cos(anguloRadiantes)
        ladoY = magnitud * math.sin(anguloRadiantes)
        return (ladoX, ladoY)
    except ValueError:
        print("El número que ingresó, no es correcto. Asegúrese de ingresar números válidos.")
        return ingresoPorMagnitudDireccion()
    

def ingresoPorComponentes():
    try:
        ladoX = float(input("Ingrese el componente X del vector: "))
        ladoY = float(input("Ingrese el componente Y del vector: "))
        return (ladoX, ladoY)
    except ValueError:
        print("El número que ingresó, no es correcto. Asegúrese de ingresar números válidos.")
        return ingresoPorComponentes()

        
        