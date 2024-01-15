from imports import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


class agentDetailMetro:


    def downloadData(dateInicio, dateFinal, pipkinsUser, pipkinsPassword):
        try:
            file = r'C:\DESARROLLOS/WEB_SCRAPPING\METRO\files\Report-ManualRTA.xlsx'
            os.remove(file)
        except:
            pass
        try:
            file = r'C:\DESARROLLOS/WEB_SCRAPPING\METRO\files\agentDetail.xlsx'
            os.remove(file)
        except:
            pass
        service = Service(executable_path='drivers/chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("window-size=1920x1080")
        options.add_experimental_option("prefs", {
            "download.default_directory": r"C:\DESARROLLOS\WEB_SCRAPPING\METRO\files"
        })
        driver = webdriver.Chrome(service=service, options=options)
        
        time.sleep(2)
        driver.get("https://www.workforcescheduling.com/onetouch") 
        driver.switch_to.frame("MAINWINDOW")
        time.sleep(2)
        user = driver.find_element(by=By.XPATH, value='//*[@id="StaffID"]')
        user.send_keys(pipkinsUser)
        password = driver.find_element(by=By.XPATH, value='//*[@id="Pin"]')
        password.send_keys(pipkinsPassword)
        login = driver.find_element(by=By.XPATH, value='//*[@id="login"]')
        login.click()
        time.sleep(10)
        driver.switch_to.default_content()
        driver.switch_to.frame("HEADER")
        reports = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td[2]')
        reports.click()
        time.sleep(4)
        manualRTA = driver.find_element(by=By.XPATH, value='//*[@id="outlookContainer"]/div[8]')
        manualRTA.click()
        time.sleep(4)
        driver.switch_to.default_content()
        driver.switch_to.frame("MAINWINDOW")
        dateOption = driver.find_element(by=By.XPATH, value='//*[@id="ContentMain_ReportPeriod_2"]')
        dateOption.click()
        time.sleep(4)
        agentDetail = driver.find_element(by=By.XPATH, value='//*[@id="ContentMain_ReportType_0"]')
        agentDetail.click()
        time.sleep(4)
        dateIni = driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ContentMain_DateRangeStart_DatePicker_dateInput"]')
        dateIni.click()
        dateIni.send_keys(dateInicio)
        dateFin = driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ContentMain_DateRangeEnd_DatePicker_dateInput"]')
        dateFin.click()
        dateFin.send_keys(dateFinal)
        position = driver.find_element(by=By.XPATH, value='//*[@id="ContentMain_MaintenanceOfficeTransfer_AvailableSelect"]/option[2]')
        driver.execute_script("arguments[0].scrollIntoView();", position)
        time.sleep(4)
        actions = ActionChains(driver)
        optionCol = driver.find_element(by=By.XPATH, value='//*[@id="ContentMain_MaintenanceOfficeTransfer_AvailableSelect"]/option[2]')
        actions.double_click(optionCol).perform()
        time.sleep(4)
        position = driver.find_element(by=By.XPATH, value='//*[@id="ContentMain_MaintenanceStaffGroupTransfer_AvailableSelect"]/option[5]')
        driver.execute_script("arguments[0].scrollIntoView();", position)
        time.sleep(4)
        optionTraining = driver.find_element(by=By.XPATH, value='//*[@id="ContentMain_MaintenanceStaffGroupTransfer_AvailableSelect"]/option[5]')
        actions.double_click(optionTraining).perform()
        time.sleep(4)
        toExcel = driver.find_element(by=By.XPATH, value='//*[@id="ContentMain_ExcelReport"]')
        driver.execute_script("arguments[0].scrollIntoView();", toExcel)
        time.sleep(4)
        toExcel.click()
        genReport = driver.find_element(by=By.XPATH, value='//*[@id="ContentMain_ViewReport"]')
        driver.execute_script("arguments[0].scrollIntoView();", genReport)
        time.sleep(4)
        genReport.click()
        time.sleep(20)
        driver.close()
        nombre_original = r'C:\DESARROLLOS/WEB_SCRAPPING\METRO\files\Report-ManualRTA.xlsx'
        nuevo_nombre = r'C:\DESARROLLOS\WEB_SCRAPPING\METRO\files\agentDetail.xlsx'

        os.rename(nombre_original, nuevo_nombre)


    def downloadData2(dateInicio, dateFinal, pipkinsUser, pipkinsPassword):
        try:
            file = r'C:\DESARROLLOS/WEB_SCRAPPING\METRO\files\Report-ManualRTA.xlsx'
            os.remove(file)
        except:
            pass
        try:
            file = r'C:\DESARROLLOS/WEB_SCRAPPING\METRO\files\agentDetail.xlsx'
            os.remove(file)
        except:
            pass
        service = Service(executable_path='drivers/chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("window-size=1920x1080")
        options.add_experimental_option("prefs", {
            "download.default_directory": r"C:\DESARROLLOS\WEB_SCRAPPING\METRO\files"
        })
        driver = webdriver.Chrome(service=service, options=options)
        
        time.sleep(2)
        driver.get("https://www.workforcescheduling.com/onetouch") 
        driver.switch_to.frame("MAINWINDOW")
        time.sleep(2)
        user = driver.find_element(by=By.XPATH, value='//*[@id="StaffID"]')
        user.send_keys(pipkinsUser)
        password = driver.find_element(by=By.XPATH, value='//*[@id="Pin"]')
        password.send_keys(pipkinsPassword)
        login = driver.find_element(by=By.XPATH, value='//*[@id="login"]')
        login.click()
        time.sleep(10)
        driver.switch_to.default_content()
        driver.switch_to.frame("HEADER")
        reports = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td[2]')
        reports.click()
        time.sleep(4)
        manualRTA = driver.find_element(by=By.XPATH, value='//*[@id="outlookContainer"]/div[8]')
        manualRTA.click()
        time.sleep(4)
        driver.switch_to.default_content()
        driver.switch_to.frame("MAINWINDOW")
        dateOption = driver.find_element(by=By.XPATH, value='//*[@id="ContentMain_ReportPeriod_2"]')
        dateOption.click()
        time.sleep(4)
        agentDetail = driver.find_element(by=By.XPATH, value='//*[@id="ContentMain_ReportType_0"]')
        agentDetail.click()
        time.sleep(4)
        dateIni = driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ContentMain_DateRangeStart_DatePicker_dateInput"]')
        dateIni.click()
        dateIni.send_keys(dateInicio)
        dateFin = driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ContentMain_DateRangeEnd_DatePicker_dateInput"]')
        dateFin.click()
        dateFin.send_keys(dateFinal)
        position = driver.find_element(by=By.XPATH, value='//*[@id="ContentMain_MaintenanceDepartmentTransfer_AvailableSelect"]/option[7]')
        driver.execute_script("arguments[0].scrollIntoView();", position)
        time.sleep(4)
        actions = ActionChains(driver)
        optionCol = driver.find_element(by=By.XPATH, value='//*[@id="ContentMain_MaintenanceDepartmentTransfer_AvailableSelect"]/option[7]')
        actions.double_click(optionCol).perform()
        time.sleep(4)
        toExcel = driver.find_element(by=By.XPATH, value='//*[@id="ContentMain_ExcelReport"]')
        driver.execute_script("arguments[0].scrollIntoView();", toExcel)
        time.sleep(4)
        toExcel.click()
        genReport = driver.find_element(by=By.XPATH, value='//*[@id="ContentMain_ViewReport"]')
        driver.execute_script("arguments[0].scrollIntoView();", genReport)
        time.sleep(4)
        genReport.click()
        time.sleep(20)
        driver.close()
        nombre_original = r'C:\DESARROLLOS/WEB_SCRAPPING\METRO\files\Report-ManualRTA.xlsx'
        nuevo_nombre = r'C:\DESARROLLOS\WEB_SCRAPPING\METRO\files\agentDetail.xlsx'

        os.rename(nombre_original, nuevo_nombre)


    def getData(path):

        filename = path
        workbook = load_workbook(filename)

        # Get the first sheet.
        worksheet = workbook.worksheets[0]

        
        row_list = []
        for r in worksheet.rows:
            column = [cell.value for cell in r]
            row_list.append(column)

        date = row_list[5][1]
        date = datetime.strptime(date, '%m-%d-%Y')
       
        df = pd.read_excel(path, skiprows=4)

        renameColumns = {'Agent:':'AGENT',
                         'Date':'DATE',
                         'Event':'EVENT',
                         'Clock In':'CLOCK_IN',
                         'Clock Out':'CLOCK_OUT',
                         'Paid Duration\n (hh:mm:ss)':'DURATION'}
        df = df.rename(columns=renameColumns)
        df = df.dropna(subset=['DURATION'])
        df = df[df.DURATION != 'Paid Duration\n (hh:mm:ss)']
        df = df[df.DURATION != 'Duration']
        df = df[df.CLOCK_IN != '--']
        df['DATE'] = date
        df['AGENT'] = df['AGENT'].replace(' ', pd.NA)
        df['AGENT'].fillna(method='ffill', inplace=True)
        df[['AGENT_NAME', 'ID_AGENT']] = df['AGENT'].str.split('-', expand=True)
        # Convertir la columna 'Time' a datetime
        df['CLOCK_IN'] = pd.to_datetime(df['CLOCK_IN'])
        df['CLOCK_OUT'] = pd.to_datetime(df['CLOCK_OUT'])
        # Formatear la hora en el formato de 24 horas de MySQL
        df['CLOCK_IN'] = df['CLOCK_IN'].dt.strftime('%H:%M:%S')
        df['CLOCK_OUT'] = df['CLOCK_OUT'].dt.strftime('%H:%M:%S')
        return df
    
    def setData(connectionD, dataframe):

        sqlCreate = """CREATE TABLE IF NOT EXISTS `tb_agent_detail_metro` (
                    `AGENT` varchar(128) NOT NULL,
                    `DATE` date NOT NULL,
                    `EVENT` varchar(32) DEFAULT NULL,
                    `CLOCK_IN` time NOT NULL,
                    `CLOCK_OUT` time NOT NULL,
                    `DURATION` time DEFAULT NULL,
                    `AGENT_NAME` varchar(128) DEFAULT NULL,
                    `ID_AGENT` int NOT NULL,
                    PRIMARY KEY (`DATE`,`ID_AGENT`,`CLOCK_IN`,`CLOCK_OUT`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                    """
        sqlCreateTmp = """CREATE TABLE IF NOT EXISTS `tb_agent_detail_metro_tmp` (
                    `AGENT` varchar(128) NOT NULL,
                    `DATE` date NOT NULL,
                    `EVENT` varchar(32) DEFAULT NULL,
                    `CLOCK_IN` time NOT NULL,
                    `CLOCK_OUT` time NOT NULL,
                    `DURATION` time DEFAULT NULL,
                    `AGENT_NAME` varchar(128) DEFAULT NULL,
                    `ID_AGENT` int NOT NULL
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                    """
        
        executeQuery(sqlCreate, connectionD)
        executeQuery(sqlCreateTmp, connectionD)

        to_sql(dataframe, "tb_agent_detail_metro_tmp", connectionD, "append", None, 10000)

        sqlReplace = """REPLACE INTO tb_agent_detail_metro
                        SELECT * FROM tb_agent_detail_metro_tmp"""
        
        executeQuery(sqlReplace, connectionD)

        sqlDropTmp = """DROP TABLE IF EXISTS tb_agent_detail_metro_tmp"""

        executeQuery(sqlDropTmp, connectionD)




if __name__ == "__main__":

    date = date.today()-timedelta(days=3)


    while date <= date.today():
        datestr = date.strftime('%m-%d-%Y')

        dateIni = datestr
        dateFin = datestr
        agentDetailMetro.downloadData(dateIni, dateFin)

        path = r"C:\DESARROLLOS\WEB_SCRAPPING\METRO\files\agentDetail.xlsx"



        try:
            df = agentDetailMetro.getData(path)

            with open(r'var/json/conManager.json', 'r') as file:
                dataCon = json.load(file)

        
            ip_destino, port_destino, user_destino, password_destino, bbdd_destino = (
                dataCon[0]["ip"],
                dataCon[0]["port"],
                dataCon[0]["user"],
                dataCon[0]["password"],
                dataCon[0]["bbdd"]
            )



            sqlEngine_destino = mysql_connection(ip_destino, port_destino, user_destino, password_destino, bbdd_destino)
            connection_destino = sqlEngine_destino.connect()

            agentDetailMetro.setData(connection_destino, df)
        except:
            print(f"Descarga del día {date} Vacía")
        date = date +timedelta(days = 1)





