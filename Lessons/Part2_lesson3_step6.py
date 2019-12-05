from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector("body form button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id("input_value").text
    y = calc(int(x))
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_css_selector("body form button").click()

finally:
    time.sleep(10)
    browser.quit()