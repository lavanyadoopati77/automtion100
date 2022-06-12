import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\\Users\\doopati\\Desktop\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

driver.find_element(By.ID,"name").send_keys("lavanya")
driver.find_element(By.ID,"phone").send_keys("123456789")
driver.find_element(By.ID,"email").send_keys("lavanyadoopati@gmail.com")
driver.find_element(By.CLASS_NAME,"form-control").send_keys("jskdhKDasds")
driver.find_element(By.XPATH,"//input[@id='female']").click()
time.sleep(5)
drp1=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and contains(@id,'day')]")
print(len(drp1))
for i in drp1:
    i.click()

drop1=Select(driver.find_element(By.XPATH,"//select[@class='custom-select']"))
drop1.select_by_visible_text("Norway")

drp=driver.find_elements(By.XPATH,"//label[@class='custom-control-label']")
print(len(drp))
for j in drp:
    j.click()
print(i.is_selected())
print(j.is_selected())


driver.find_element(By.XPATH,"//input[@class='custom-file-input']").send_keys("C:\\Users\\doopati\\Desktop\\Automation Test Engineer.docx")
