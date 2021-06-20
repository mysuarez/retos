def reto_5(ruta_archivo: str) -> list:
    import pandas as pd

    df = pd.read_csv("25-listado-clases.csv")
    df['PUNTAJE'] = df.sum(axis=1)
    mejores_5 = df.sort_values('PUNTAJE', ascending=False)[
        ['ESTUDIANTE', 'PUNTAJE']].head()
    mejores_5 = mejores_5.set_index([pd.Index([1, 2, 3, 4, 5], name='PUESTO')])
    promedios = pd.DataFrame(df.mean()).round(2)
    promedios.index.name = 'PRUEBAS'
    promedios.columns = ['PROMEDIO']

    return [mejores_5, promedios]
