##########################################
#####          LIBRERIAS             #####
##########################################

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import json
import os

##########################################
#####          FUNCIONES             #####
##########################################

''' 
Resumen:
- convertir_fecha(fecha:int, formato:str="%Y-%m-%d")
- call_situacion_estaciones(directorio:str='./datos/Situacion de Estaciones')
- call_uso_bicicletas(directorio:str='./datos/Datos usos')

'''
#----------------------------------------------------------------------------------------------------------------------------------
def convertir_fecha(fecha:int, formato:str="%Y-%m-%d"):
    ''' 
    Esta es un funcion para convertir un fecha numerica a fecha.

    Input:
        fecha:int
    
    Output:
        fecha_convertida:date ("%Y-%m-%d")
    '''
    fecha_base = datetime(1899, 12, 30)
    fecha_convertida = (fecha_base + timedelta(days=fecha)).strftime(formato)
    return fecha_convertida

#----------------------------------------------------------------------------------------------------------------------------------

def call_situacion_estaciones(directorio:str='./data/Datos Originales/Situacion de Estaciones'):
    ''' 
    Funcion para leer varios ficheros de json de un directorio.

    Input:
        directorio:str
    
    Output:
        bases:DataFrame
    '''
    bases = pd.DataFrame()
    for archivo in os.listdir(directorio):
        records = []
        ruta_completa = os.path.join(directorio, archivo)
        with open(ruta_completa, 'r', encoding='utf-8') as f:
            for line in f:
                record = json.loads(line)
                records.append(record)
        df = pd.DataFrame(records)
        df_exploded = df.explode('stations', ignore_index=True)
        stations_df = pd.json_normalize(df_exploded['stations'])
        stations_df['_id'] = df_exploded['_id']
        bases = pd.concat([bases,stations_df], ignore_index=True)
    return bases

#----------------------------------------------------------------------------------------------------------------------------------

def call_uso_bicicletas(directorio:str='./data/Datos Originales/Datos usos'):
    ''' 
    Funcion para leer varios ficheros de csv de un directorio.

    Input:
        directorio:str
    
    Output:
        bases:DataFrame
    '''
    bases = pd.DataFrame()
    for archivo in os.listdir(directorio):
        records = []
        ruta_completa = os.path.join(directorio, archivo)
        with open(ruta_completa, 'r', encoding='utf-8') as f:
            record = pd.read_csv(f, sep=";", comment=";", skip_blank_lines=True, dtype={"station_unlock": str})
            record.dropna(how="all", inplace=True)
            bases = pd.concat([bases,record], ignore_index=True)
    return bases