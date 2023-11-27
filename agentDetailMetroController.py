from agentDetailMetro import *

Metro = agentDetailMetro


def agentDetailMetroController(interval):

    date_ = date.today()-timedelta(days=interval)

    with open(r'var/json/conManager.json', 'r') as file:
        dataCon = json.load(file)

    userPipkins, passwordPipkins = (
        dataCon[3]["user"],
        dataCon[3]["password"]
    )

    while date_ <= date.today():
        datestr = date_.strftime('%m-%d-%Y')

        dateIni = datestr
        dateFin = datestr
        Metro.downloadData(dateIni, dateFin, userPipkins, passwordPipkins)

        path = r"C:\DESARROLLOS\WEB_SCRAPPING\METRO\files\agentDetail.xlsx"

        try:
            df = Metro.getData(path)

        
            ip_destino, port_destino, user_destino, password_destino, bbdd_destino = (
                dataCon[0]["ip"],
                dataCon[0]["port"],
                dataCon[0]["user"],
                dataCon[0]["password"],
                dataCon[0]["bbdd"]
            )

            sqlEngine_destino = mysql_connection(ip_destino, port_destino, user_destino, password_destino, bbdd_destino)
            connection_destino = sqlEngine_destino.connect()
            Metro.setData(connection_destino, df)


        except:
            print(f"Descarga del día {date_} Vacía")
        date_ = date_ +timedelta(days = 1)