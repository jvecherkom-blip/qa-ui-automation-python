from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_google_search(driver):
    driver.get("https://www.google.com")

    search_input = driver.find_element(By.NAME, "q")
    search_input.send_keys("python pytest")
    search_input.send_keys(Keys.RETURN)

    assert "python" in driver.title.lower()