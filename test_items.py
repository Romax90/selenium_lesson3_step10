from selenium.webdriver.common.by import By
import time


def test_lesson3_6_step10(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    button = browser.find_element(By.CLASS_NAME, 'btn-lg.btn-primary.btn-add-to-basket')
    button_text= button.text

    assert button_text, f'Страница товара на сайте {link} не содержит кнопки добавления в корзину'