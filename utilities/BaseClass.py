import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import logging
import inspect


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verify_link_presence(self,text):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.LINK_TEXT,text)))

    def select_option_by_text(self,locator,text):
        sel=Select(locator)
        sel.select_by_visible_text(text)

    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)

        return logger