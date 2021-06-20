#######
#Reto 4 Grupo P59 conversor de Farenheit a Celsius#
########
#Formador de Programacion: Bernardo Cuervo Benítez
#(Se omiten tildes para evitar problemas de codificacion) 

def grados_celsius(n)->str:
    
    try:
        for i in n:
            cels = list(map(lambda x: round(((x - 32) * 5 / 9),1), n))
        return f'{n} en grados Farenheit corresponde a {cels} en grados Celsius respectivamente'
        
    except:
        return 'Error al convertir los grados, revise los datos de entrada' 

#print(grados_celsius([212, 104, 50]))

#print(grados_celsius([50, 176, 104]))

#print(grados_celsius([104, 320, 50]))

#print(grados_celsius([122, 95, 50]))

#print(grados_celsius([113, 104, 50]))
