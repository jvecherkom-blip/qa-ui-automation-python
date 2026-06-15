from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_google_search(driver):
    driver.get("https://www.google.com")
    accept = driver.find_elements(By.ID, "L2AGLb")
    if accept:
        accept[0].click()

    wait = WebDriverWait(driver, 10)

    search_input = wait.until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )

    search_input.send_keys("python pytest")
    search_input.send_keys(Keys.RETURN)

    assert "python" in driver.title.lower()