import pandas as pd

def CasosCovid(ruta_archivo_csv: str)-> dict:
    
    
    # Validaciones
    # 1 Extension
    if ruta_archivo_csv.endswith('.csv'): 
        # 2 Open File (ruta_archivo_csv)
        try:
            df = pd.read_csv(ruta_archivo_csv)
        except:
            return 'Error al leer el archivo de datos'        
        
        d = df[['ID de caso','Ciudad de ubicación','Edad','Sexo','Estado']]
        
        d2 = df[['ID de caso','Estado']]
        df_resp = d2.groupby(['Estado']).count() 
                
    else:
        return 'Extensión inválida'    
        
    # Preparar Salida
    df_resp = df_resp.to_dict()
    return df_resp

print(CasosCovid('https://raw.githubusercontent.com/bernoulli/MisionTIC2022/main/casos_covid_19.csv'))
