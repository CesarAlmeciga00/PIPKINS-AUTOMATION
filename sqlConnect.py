    #############################################################################################################
#                                  @AUTOR: CESAR ALMÉCIGA                      	                        	#
#                                  @PROCESO: FUNCIONES SQL                  					            #                                                     									                        #
#                                  @DESCRIPCIÓN: FUNCIONES BÁSICAS SQL PARA OPTIMIZACIÓN                    #
#                                  Y REUTILIZACIÓN DE CÓDIGO                                                #
#############################################################################################################

# LIBRERIAS E IMPORTES
from sqlalchemy import create_engine
import mysql.connector
from urllib.parse import quote
import pandas as pd




# FUNCIÓN DE CONEXIÓN 
def mysql_connection(ip, port, user, password, bbdd):
    sql = create_engine('mysql+pymysql://' + user +':' + quote(password) + '@' + ip + ':' + port + '/' + bbdd, pool_recycle=9600)
    return sql

def mssql_connection(ip, user, password, bbdd):
    sql = create_engine('mssql+pyodbc://' + user + ':' + quote(password) + '@' + ip + '/' + bbdd + '?driver=SQL+Server&charset=utf8&fast_executemany=True')
    return sql

# FUNCIÓN DE INSERCIÓN
def to_sql(dataframe, tableName, connection, type, index, chunksize):
    dataframe.to_sql(name=tableName, con=connection, if_exists = type, index=index, chunksize=chunksize)

# FUNCIÓN DE LECTURA
def queryRead(sql, connection):
    dataframe = pd.read_sql(sql, connection)
    return dataframe
    
# FUNCIÓN DE EJECUCIÓN
def executeQuery(sql, connection):
    connection.execute(sql)