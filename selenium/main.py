import undetected_chromedriver as uc
from time import sleep
import os

username = 'alagupandiyaraj45@gmail.com'
password ='Alagupandi4510'

driver =uc.Chrome("chromedriver.exe")

driver.delete_all_cookies()

driver.get('https://www.gmail.com')
sleep(2)

driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
sleep(2)

driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
sleep(2)

driver.get('https://gmail.com')
sleep(2)