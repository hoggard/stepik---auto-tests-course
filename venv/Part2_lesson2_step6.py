from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"
def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    y = calc(int(x))
    browser.find_element_by_id("answer").send_keys(y)
    button = browser.find_element_by_css_selector("body div.container form button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()