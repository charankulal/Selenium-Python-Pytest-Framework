from selenium.webdriver.common.by import By

from page_objects.checkout_page import CheckoutPage


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    shop = (By.XPATH,"//a[normalize-space()='Shop']")

    name = (By.CSS_SELECTOR,"input[name='name']")

    email = (By.NAME,"email")

    password = (By.XPATH,"//input[@id='exampleInputPassword1']")

    checkbox = (By.XPATH,"//input[@id='exampleCheck1']")

    dropdown = (By.XPATH, "//select[@id='exampleFormControlSelect1']")

    radio = (By.XPATH, "//input[@id='inlineRadio1']")

    submit_button = (By.XPATH, "//input[@value='Submit']")

    success_msg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        return CheckoutPage(self.driver)

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_dropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def get_radio(self):
        return self.driver.find_element(*HomePage.radio)

    def get_submit_button(self):
        return self.driver.find_element(*HomePage.submit_button)

    def get_success_msg(self):
        return self.driver.find_element(*HomePage.success_msg)