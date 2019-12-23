import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    time.sleep(5)
    answer = str(math.log(int(time.time())))
    print(answer)
    browser.find_element_by_tag_name("textarea").send_keys(answer)
    browser.find_element_by_class_name("submit-submission").click()
    time.sleep(5)
    a = browser.find_element_by_class_name("smart-hints__hint").text()
    assert a == "Correct!", "задание решено неверно"
    time.sleep(10)