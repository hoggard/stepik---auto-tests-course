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
    time.sleep(10)
    answer = math.log(int(time.time()))
    browser.find_element_by_id("ember1636").send_keys(answer)
    browser.find_element_by_css_selector("#ember1480 div section div div.attempt__inner div.attempt__actions button.submit-submission").click()
    assert WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#ember1603 pre"), "Correct!")
    ) , "Тест из урока" 'lesson' "провален"
    time.sleep(10)