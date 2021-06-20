import pandas as pd

def censo(ruta_archivo_csv: str)-> dict:
    
    # Validaciones
    # 1 Extension
    if ruta_archivo_csv.endswith('.csv'): 
        # 2 Open File (ruta_archivo_csv)
        try:
            df = pd.read_csv(ruta_archivo_csv, sep=';')
        except:
            return 'Error al leer el archivo de datos'        
        
        
        d = df[['DIRECTORIO','P1','P1S1','P8R','P9','P13','P23S1R']]
        
        d2 = df[['DIRECTORIO','P13']]
        df_resp = d2.groupby(['P13']).count() 
        
                
    else:
        return 'Extensión inválida'    
        
    # Preparar Salida
    df_resp = df_resp.to_dict()
    return df_resp

#print(censo('CHC_2020.csv'))

print(censo('https://raw.githubusercontent.com/bernoulli/MisionTIC2022/main/CHC_2020.csv'))
