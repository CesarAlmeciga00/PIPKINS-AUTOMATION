#############################################################################################################
#                                  @AUTOR: CESAR ALMÉCIGA                      	                        	#
#                                  @PROCESO: TRANSFORMACIÓN JSON A SQL (FILAS Y COLUMNAS)                   #
#                                  @DESCRIPCIÓN: LÓGICA DE LECTURA, ESTRUCTURACIÓN                          #
#                                  TRANSFORMACIÓN Y TRANSPOSICIÓN DE INFORMACIÓN JSON                       #
#                                  A FORMATO SQL                                                            #
#############################################################################################################


# LIBRERIAS E IMPORTES
import pymysql
from urllib.parse import quote
from sqlalchemy import create_engine
import os
import pandas as pd
import json
import ast
import csv
from io import StringIO
pd.io.json._json.loads = lambda s, *a, **kw: json.loads(s)
# monkeypatch using faster simplejson module
import simplejson
pd.io.json._json.loads = lambda s, *a, **kw: simplejson.loads(s)
# normalising (unnesting) at the same time (for nested jsons)
pd.io.json._json.loads = lambda s, *a, **kw: pd.json_normalize(simplejson.loads(s))
import multiprocessing
import os
import time
from datetime import date
from datetime import datetime
from datetime import timedelta
import locale
from sqlConnect import *
import pydoc
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import numpy as np
import dask.dataframe as dd
import logging
import json
import inspect
from functools import wraps
from openpyxl import load_workbook







# Configura el nivel de log global (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Crea una instancia del logger
logger = logging.getLogger(__name__)



dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)

# Función para calcular el tiempo de ejecución de una operación
def calcular_tiempo(proceso):
    def decorator(func):
        def wrapper(*args, **kwargs):
            
            with open(r'var/json/conManager.json', 'r') as file:
                dataCon = json.load(file)


            ip_destino, port_destino, user_destino, password_destino, bbdd_destino = (
                dataCon[2]["ip"],
                dataCon[2]["port"],
                dataCon[2]["user"],
                dataCon[2]["password"],
                dataCon[2]["bbdd"]
            )

            try:
                dfOrigen = func(*args, **kwargs)
                cantidad_registros = len(dfOrigen)
            except:
                pass
            engine = mysql_connection(ip_destino, port_destino, user_destino, password_destino, bbdd_destino)
            connection_destino = engine.connect()
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                end_time = time.time()
                execution_time = end_time - start_time
                mensaje = f"ERROR EXEC {proceso} {func.__name__}: {str(e)}"
                tiempo = f"{execution_time:.6f}"
                logger.error(mensaje)
                # Registrar el log en la tabla con el nombre del proceso
                log_data = {
                    'timestamp': pd.Timestamp.now(),
                    'nivel': 'EXEC',
                    'status': 'ERROR',
                    'mensaje': mensaje,
                    'tiempo_ejecucion':tiempo,
                    'proceso': proceso
                }
                with engine.connect() as conn:
                    conn.execute("INSERT INTO tb_auditoria_procesos_python (timestamp, nivel, status, mensaje, tiempo_ejecucion, proceso) VALUES (%(timestamp)s, %(nivel)s, %(status)s, %(mensaje)s, %(tiempo_ejecucion)s, %(proceso)s)", log_data)
                raise
            else:
                end_time = time.time()
                execution_time = end_time - start_time
                mensaje = f"SUCCESS EXEC {proceso} {func.__name__}"
                tiempo = f"{execution_time:.6f}"
                logger.debug(mensaje)
                # Registrar el log en la tabla con el nombre del proceso
                log_data = {
                    'timestamp': pd.Timestamp.now(),
                    'nivel': 'EXEC',
                    'status': 'SUCCESS',
                    'mensaje': mensaje,
                    'total_data': cantidad_registros,
                    'tiempo_ejecucion':tiempo,
                    'proceso': proceso
                }
                with engine.connect() as conn:
                    conn.execute("INSERT INTO tb_auditoria_procesos_python (timestamp, nivel, status, mensaje, total_rows, tiempo_ejecucion, proceso) VALUES (%(timestamp)s, %(nivel)s, %(status)s, %(mensaje)s, %(total_data)s, %(tiempo_ejecucion)s, %(proceso)s)", log_data)
                return result
        return wrapper
    return decorator



def get_num_cores():
    return multiprocessing.cpu_count()

def get_num_threads():
    return os.cpu_count()

def read_sql_file(path):
    # Leer el archivo SQL
    with open(path, 'r') as file:
        sql_create = file.read()
    
    return sql_create