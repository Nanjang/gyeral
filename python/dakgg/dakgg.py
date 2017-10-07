from selenium import webdriver
import time

driver = webdriver.PhantomJS('d:/phantomjs.exe')
driver.implicitly_wait(3)
driver.get('https://dak.gg/profile/octopus7')
print(driver.page_source)
time.sleep(1)