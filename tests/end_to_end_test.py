import time

import pytest

from page_objects.home_page import HomePage
from utilities.BaseClass import BaseClass

@pytest.mark.smoke
class TestOne(BaseClass):
    def test_end_2_end(self,setup):
        log=self.getLogger()
        driver = self.driver
        home_page = HomePage(driver=driver)
        # click on shop link in the navbar
        checkout_page = home_page.shop_items()
        log.info("Click on shop button")

        # searching among the products
        log.info("Get all products ")
        products = checkout_page.get_product_titles()
        for product in products:
            product_name = checkout_page.get_single_product_title(product)
            if product_name.text == "Blackberry":
                checkout_page.get_add_cart_button(product).click()
                log.info("Blackberry phone is added to cart")

        # checkout

        checkout_page.get_checkout_button().click()
        log.info("Clicked checkout button")
        confirm_page=checkout_page.get_second_checkout_button()
        log.info("Clicked checkout button on confirmation page")

        # entering country details
        confirm_page.get_input_country_field().send_keys("ind")
        log.info("Searching for the country to check availability")
        self.verify_link_presence("India")
        confirm_page.get_country_name().click()
        log.info("Selecting India after searching")

        # clicking on the checkbox
        confirm_page.get_checkbox()
        log.info("Accepting terms and conditions")

        # clicking purchase button
        confirm_page.get_purchase_button().click()
        log.info("Clicked Purchase button")

        # assertion
        assert "Success" in confirm_page.get_success_msg().text
