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
- limpiar_coordenadas(coord:str)
- def percentile(n:int)
- corregir_letras(texto:str)
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
    fecha_convertida = datetime.strptime(fecha_convertida, '%Y-%m-%d')
    return fecha_convertida

#----------------------------------------------------------------------------------------------------------------------------------

def call_situacion_estaciones(directorio:str='../data/Datos Originales/Situacion de Estaciones'):
    ''' 
    Funcion para leer varios ficheros de json de un directorio.

    Input:
        directorio:str
    
    Output:
        bases:DataFrame
    '''
    bases = pd.DataFrame()
    for archivo in os.listdir(directorio):
        lista = []
        ruta_completa = os.path.join(directorio, archivo)
        with open(ruta_completa, 'r', encoding='utf-8') as f:
            for linea in f:
                valores = json.loads(linea)
                lista.append(valores)
        df = pd.DataFrame(lista)

        df_exploded = df.explode('stations', ignore_index=True) # Funcion que convierte lista en registros de la tabla
        stations_df = pd.json_normalize(df_exploded['stations']) # Normalize semi-structured JSON data into a flat table.
        stations_df['_id'] = df_exploded['_id']
        bases = pd.concat([bases,stations_df], ignore_index=True)
    return bases

#----------------------------------------------------------------------------------------------------------------------------------

def call_uso_bicicletas(directorio:str='../data/Datos Originales/Datos usos'):
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

#----------------------------------------------------------------------------------------------------------------------------------

def limpiar_coordenadas(coord:str):
    ''' 
    Función de lipieza que limpia las coordenadas.

    Input:
        coord:str
    
    Output:
        coord_cambiada:str
    '''
    coord_str = coord.replace(".", "")
    if len(coord_str) >= 7:
        coord_cambiada = float(coord_str[:2] + "." + coord_str[2:])
    elif len(coord_str) >= 6:
        coord_cambiada = float(coord_str[:1] + "." + coord_str[1:])
    return coord_cambiada

#----------------------------------------------------------------------------------------------------------------------------------

def percentile(n:int):
    ''' 
    Funcion para calcular varios percentiles al usar un group by.

    Input:
        n:int --> numero de percentil
    
    Output:
        percentile_:float
    '''
    def percentile_(x):
        return np.percentile(x, n)
    percentile_.__name__ = 'percentile_%s' % n
    return percentile_

#----------------------------------------------------------------------------------------------------------------------------------

def corregir_letras(texto:str):
    ''' 
    Funcion para remplazar letras.

    Input:
        texto:str
    
    Output:
        texto:str
    '''
    mapeo_letras = {'Ã­': 'í', 'Ã©': 'é', 'Ã¡': 'á', 'Ã±': 'ñ', 'Ã³':'ó'}
    for clave, valor in mapeo_letras.items():
        texto = texto.replace(clave, valor)
    return texto