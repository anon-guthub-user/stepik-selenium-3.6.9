from selenium.webdriver.common.by import By


def test_cart_visibility(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

    # User find_elements to find the cart so that it returns an array of elements.
    cart = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')

    # Assert that the list is not empty.
    assert cart.is_displayed(), "Cart element is not present on the page."
