
from suma import suma


def Resta (n1, n2):
    resta= n1 - n2
    return resta

def parametro (texto, valor):
    print (str ("La impresion de texto y valor es: "), str (texto), int (valor))

def producto (n1, n2, n3, n4):
   producto= n1 * n2 * n3 * n4
   return producto


if __name__ == "__main__":
    print('Primer programa en Python')
    print("La suma es: ", str(suma(2,3,4)))
    parametro("Julio",16)
    print("El producto es: ", str(producto(2,3,5,2)))
    print("Resultado de la resta: ", str(Resta(10,3)))
    