from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium подождать 12 секунд и нажать на кнопку, когда цена уменьшится до 100
    price=WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.ID,"price"),'100'))
    button =browser.find_element (By.ID, "book")
    button.click()

    # код для считывания X и рассчета Y
    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value').text
    y = calc(x_element)

    # вставляем получившееся значение в поле ввода
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(str(y))

    # Нажимаем кнопку
    button1 = browser.find_element(By.XPATH, "//button[@type='submit']")
    button1.click()

finally:
    # вывести ответ
    print(browser.switch_to.alert.text.split(': ')[-1])
    # закрываем браузер после всех манипуляций
    browser.quit()