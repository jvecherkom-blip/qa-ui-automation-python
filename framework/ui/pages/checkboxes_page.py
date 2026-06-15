from selenium.webdriver.common.by import By

from framework.ui.pages.base_page import BasePage


class CheckboxesPage(BasePage):

    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")

    def open(self):
        self.driver.get(
            "https://the-internet.herokuapp.com/checkboxes"
        )

    def get_checkboxes(self):
        return self.driver.find_elements(*self.CHECKBOXES)