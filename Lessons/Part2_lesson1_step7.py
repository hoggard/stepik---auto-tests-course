from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("treasure").get_attribute("valuex")
    y = calc(int(x))
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("body div.container form button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()