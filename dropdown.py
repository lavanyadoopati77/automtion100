from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\\Users\\doopati\\Desktop\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

drp_country=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))
#for options1 in drp_country.options:
 #   print(options1.text)

#print(len(drp_country.options))
drp_country.select_by_visible_text("India")
