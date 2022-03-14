from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

chromedriver = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.thsrc.com.tw/')
driver.maximize_window()
cookie = driver.find_element(By.CLASS_NAME, 'swal2-confirm')
cookie.click()

location01 = driver.find_element(By.ID, 'select_location01')
Select(location01).select_by_visible_text('桃園')

location02 = driver.find_element(By.ID, 'select_location02')
Select(location02).select_by_visible_text('台北')

# 怎麼選日曆，還需要查證
# depart_date = driver.find_element(By.ID, 'Departdate01')
# time.sleep(2)
# js = "$('input[id=c-date1]').removeAttr('readonly')"
# driver.execute_script(js)
# depart_date.send_keys("2022/03/16")


start_search = driver.find_element(By.ID, 'start-search')

start_search.click()


