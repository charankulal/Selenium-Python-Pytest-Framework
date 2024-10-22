from selenium.webdriver.common.by import By

class ConfirmPage:

    def __init__(self,driver):
        self.driver =  driver

    input_country_field = (By.XPATH,"//input[@id='country']")

    select_country_name = (By.XPATH,"//a[normalize-space()='India']")

    checkbox = (By.XPATH,"//label[@for='checkbox2']")


    purchase_button = (By.XPATH,"//input[@value='Purchase']")

    success_msg = (By.XPATH,"//div[@class='alert alert-success alert-dismissible']")

    def get_input_country_field(self):
        return self.driver.find_element(*ConfirmPage.input_country_field)

    def get_country_name(self):
        return self.driver.find_element(*ConfirmPage.select_country_name)

    def get_checkbox(self):
        self.driver.find_element(*ConfirmPage.checkbox).click()

    def get_purchase_button(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    def get_success_msg(self):
        return self.driver.find_element(*ConfirmPage.success_msg)