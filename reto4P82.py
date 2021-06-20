
#######
#Reto 4 Grupo P82 Palindrome#
########
#Formador de Programacion: Bernardo Cuervo Benitez
#(Se omiten tildes para evitar problemas de codificacion)

"""La funcion palindrome permite encontrar palabras palindromas en una lista de palabras."""

def palindrome(lista)->list:

    resp = []
    for i in lista:
        resp = list(filter(lambda x: (x == "".join(reversed(x))), lista))
    return resp


