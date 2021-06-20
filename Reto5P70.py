import pandas as pd

def Titanic(ruta_archivo_csv: str)-> dict:
    
    
    # Validaciones
    # 1 Extension
    if ruta_archivo_csv.endswith('.csv'): 
        # 2 Open File (ruta_archivo_csv)
        try:
            df = pd.read_csv(ruta_archivo_csv)
        except:
            return 'Error al leer el archivo de datos'        
        
        d = df[['name','sex','age','survived']]
        
        d2 = df[['pclass','survived']]
        df_resp = d2.groupby(['survived']).count() 
                
    else:
        return 'Extensión inválida'    
        
    # Preparar Salida
    df_resp = df_resp.to_dict()
    return df_resp

print(Titanic('titanic.csv'))
