import unittest
from selenium import webdriver
import time

class FirstTestCase(unittest.TestCase):
    def test_first_page(self1):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector("body div.first_block div.form-group.first_class input")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector("body div.first_block div.form-group.second_class input")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector("body div.first_block div.form-group.third_class input")
            input3.send_keys("petrov@mail.ru")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
            time.sleep(1)

        # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            self1.assertEqual(welcome_text , "Congratulations! You have successfully registered!")
        finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
        # закрываем браузер после всех манипуляций
            browser.quit()
    def test_second_page(self2):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector("body div.first_block div.form-group.first_class input")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector("body div.first_block div.form-group.second_class input")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector("body div.first_block div.form-group.third_class input")
            input3.send_keys("petrov@mail.ru")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            self2.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

if __name__ == '__main__':
    unittest.main()
