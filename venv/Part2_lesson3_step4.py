from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element_by_css_selector("body form button")
    button1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id("input_value").text
    y = calc(int(x))
    browser.find_element_by_id("answer").send_keys(y)
    button_submit = browser.find_element_by_css_selector("body form button")
    button_submit.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
