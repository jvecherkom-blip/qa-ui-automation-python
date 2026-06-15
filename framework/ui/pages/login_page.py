from selenium.webdriver.common.by import By
from framework.ui.pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(
            "https://the-internet.herokuapp.com/login"
        )

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)

        user = self.driver.find_element(*self.USERNAME_INPUT).get_attribute("value")
        pwd = self.driver.find_element(*self.PASSWORD_INPUT).get_attribute("value")

        print("username field =", user)
        print("password field =", pwd)

        self.click(self.LOGIN_BUTTON)

    def get_success_message(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text