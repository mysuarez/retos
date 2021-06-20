def reto_4(diccionario: dict) -> tuple:

    import numpy as np

    llaves = list(diccionario.keys())
    resultados = [[resultado for resultado in llave.values()]
                  for llave in diccionario.values()]
    normalizado = [list(map(lambda resultado: 5 if resultado <
                        6 else resultado, i)) for i in resultados]
    matriz = np.array(normalizado)
    promedio_pruebas = np.around(np.average(normalizado, axis=0), decimals=1)
    puntajes = np.sum(normalizado, axis=1)
    seleccionado = llaves[puntajes.argmax()]

    return (normalizado, matriz, promedio_pruebas, puntajes, seleccionado)
