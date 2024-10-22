import pytest

from page_objects.home_page import HomePage
from test_data.homepage_data import HomePageData
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select

class TestHomePage(BaseClass):

    @pytest.mark.sanity
    def test_form_submission(self,getData):
        log = self.getLogger()
        home_page = HomePage(driver=self.driver)

        log.info("Opened home page")
        # for name
        home_page.get_name().send_keys(getData[0][0])
        log.info("Entered Name "+getData[0][0])
        # for email
        home_page.get_email().send_keys(getData[0][1])
        log.info("Entered Email "+ getData[0][1])
        #  for password
        home_page.get_password().send_keys(getData[0][2])
        log.info("Entered Password "+ getData[0][2])
        #  for checkbox
        home_page.get_checkbox().click()
        log.info("Clicked on checkbox ")

        #  static dropdown automation
        self.select_option_by_text(home_page.get_dropdown(),getData[0][3])
        log.info("Entered Gender "+ getData[0][3])

        home_page.get_radio().click()
        log.info("Clicked on radio button")

        # submit button
        home_page.get_submit_button().click()
        log.info("Submitted the form")

        successText = home_page.get_success_msg().text

        assert "Success" in successText
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData())
    def getData(self,request):
        return  request.param,
