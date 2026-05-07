import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from framework.api.clients.booking_client import BookingClient

client = BookingClient()

@pytest.fixture
def auth_token():
    auth_data = {
        "username": "admin",
        "password": "password123"
    }
    response = client.create_token(auth_data)
    return response.json()["token"]

@pytest.fixture
def created_booking(booking_data):
    response = client.create_booking(booking_data)
    return response.json()


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def booking_data():
    return {
        "firstname": "Anna",
        "lastname": "Smith",
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Breakfast"
    }