import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
 

#Chrome 의 드라이버 저장 위치 
ff_driver = webdriver.Chrome()#Firefox()
ff_driver.get("https://www.google.co.kr/")

# 웹드라이브


