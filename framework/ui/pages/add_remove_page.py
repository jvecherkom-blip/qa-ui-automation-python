from selenium.webdriver.common.by import By

from framework.ui.pages.base_page import BasePage


class AddRemovePage(BasePage):

    ADD_BUTTON = (By.XPATH, "//button[text()='Add Element']")
    DELETE_BUTTONS = (By.CLASS_NAME, "added-manually")

    def open(self):
        self.driver.get(
            "https://the-internet.herokuapp.com/add_remove_elements/"
        )

    def add_element(self):
        self.click(self.ADD_BUTTON)

    def get_delete_buttons(self):
        return self.driver.find_elements(*self.DELETE_BUTTONS)
    