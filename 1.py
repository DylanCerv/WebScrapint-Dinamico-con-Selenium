from selenium import webdriver
from selenium.webdriver.support.ui import Select

webSite = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = 'C:/Users/maria/Desktop/Python/DataScienceYT (Frank Andrade)/Web Scraping Dinamico con Selenium/chromedriver.exe'


driver = webdriver.Chrome(path)
driver.get(webSite)


allMatchesBotton = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
# allMatchesBotton = driver.find_element(by=By.XPATH,'//label[@analytics-event="All matches"]')
allMatchesBotton.click()

dropDownList = Select(driver.find_element_by_id('country'))
dropDownList.select_by_visible_text('Spain')