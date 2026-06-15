import pytest
from framework.ui.pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username,password,expected_text",
    [
        pytest.param(
            "tomsmith",
            "SuperSecretPassword!",
            "You logged into a secure area!",
            id="valid_login"
        ),
        pytest.param(
            "wrong",
            "SuperSecretPassword!",
            "Your username is invalid!",
            id="invalid_username"
        ),
        pytest.param(
            "tomsmith",
            "wrong",
            "Your password is invalid!",
            id="invalid_password"
        )
    ]
)

def test_successful_login(driver,username, password, expected_text):
    page = LoginPage(driver)

    page.open()
    page.login("tomsmith", "SuperSecretPassword!")

    message = page.get_success_message()

    assert "You logged into a secure area!" in message

