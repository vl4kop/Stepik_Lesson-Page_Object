from pages.product_page import ProductPage


link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_product_add_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()

    page.should_be_button_add_to_cart()
    page.add_to_cart()

    page.solve_quiz_and_get_code()

    page.should_be_value()

    page.name_of_book()
    page.value_of_cart()



# pytest -v -s --tb=line --language=en test_product_page.py