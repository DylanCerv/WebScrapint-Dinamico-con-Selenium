from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

#############################
# Configuracion del entorno #
#############################
webSite = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = '' # COLOCAR EL DIRECTIO DE LA CARPETA DONDE SE ENCUENTRA EL EJECUTABLE 'chromedriver.exe' [ejemplo 'C:/Users/dylan/Desktop/WebScraping/driver/chromedriver.exe']


#################################
# Codigo para extraer los datos #
#################################
driver = webdriver.Chrome(path)
driver.get(webSite)

allMatchesBotton = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
allMatchesBotton.click()
box = driver.find_element_by_class_name('panel-body')
dropDownList = Select(box.find_element_by_id('country'))
dropDownList.select_by_visible_text('Spain')
time.sleep(5)
matches = driver.find_elements_by_css_selector('tr')

all_matches = []
for match in matches:
    all_matches.append(match.text) #Almacenar los valores en la lista

driver.quit()

# #############################
# ######### DataFrame #########
# #############################

df = pd.DataFrame({'goals': all_matches})
print(df)
df.to_csv('partidos.csv', index = False) #RUTA Y NOMBRE DEL ARCHIVO CSV QUE SE VA A CREAR