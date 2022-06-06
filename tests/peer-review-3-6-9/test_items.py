from selenium.webdriver.common.by import By


def test_cart_button_visibility(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

    cart_button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')

    assert cart_button.is_displayed(), "Cart element is not present on the page."
