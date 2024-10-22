from selenium.webdriver.common.by import By

from page_objects.confirm_page import ConfirmPage


class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver

    product_titles = (By.XPATH,"//div[@class='card h-100']")

    product_name = (By.XPATH,"div/h4/a")

    product_button = (By.XPATH,"div/button")

    checkout_button = (By.XPATH,"(//a[@class='nav-link btn btn-primary'])[1]")

    second_checkout_button = (By.XPATH,"//button[normalize-space()='Checkout']")


    def get_product_titles(self):
        return self.driver.find_elements(*CheckoutPage.product_titles)

    def get_single_product_title(self,product):
        return product.find_element(*CheckoutPage.product_name)

    def get_add_cart_button(self, product ):
        return product.find_element(*CheckoutPage.product_button)

    def get_checkout_button(self):
        return self.driver.find_element(*CheckoutPage.checkout_button)

    def get_second_checkout_button(self):
        self.driver.find_element(*CheckoutPage.second_checkout_button).click()
        return ConfirmPage(self.driver)