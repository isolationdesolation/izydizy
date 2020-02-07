import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from .Pages.home_page import HomePage
from .Pages.landos_page import LandosPage

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)

    yield driver
    driver.quit()


@pytest.fixture()
def home_page(driver):
    home_page = HomePage(driver, 4)
    return home_page



@pytest.fixture()
def landos_page(driver):
    landos_page = LandosPage(driver,15)
    return landos_page