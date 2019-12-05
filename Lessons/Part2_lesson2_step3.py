from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    z = str(int(x) + int(y))
    print(x,y,z)
    sum_select = Select(browser.find_element_by_id("dropdown"))
    sum_select.select_by_value(z)
    browser.find_element_by_css_selector("body div.container form button").click()

finally:
    time.sleep(10)
    browser.quit()