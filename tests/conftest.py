import pytest
from api.posts_api import create_post
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def post_payload():
    return {
        "title": "fixture title",
        "body": "fixture body",
        "userId": 1
    }

@pytest.fixture
def created_post(post_payload):
    response = create_post(post_payload)
    return response

@pytest.fixture(params=[
    {
        "title": "title 1",
        "body": "body 1",
        "userId": 1
    },
    {
        "title": "title 2",
        "body": "body 2",
        "userId": 2
    }
])
def post_payload(request):
    return request.param

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()