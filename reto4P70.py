from math import sqrt
#######
#Reto 4 Grupo P70 Números Primos#
########
#Formador de Programacion: Bernardo Cuervo Benitez
#(Se omiten tildes para evitar problemas de codificacion)

"""La funcion primos calcula los numeros de primos entre el 2 y el número n."""

def primos(n):
    numeros = range(2, n)
    for i in range(2, int(2*sqrt(n))):
        numeros = list(filter(lambda x: x==i or x%i, numeros))
    return numeros



