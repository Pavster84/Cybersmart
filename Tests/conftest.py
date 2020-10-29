import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_name == "firefox":
        pass
        # firefox path
    elif browser_name == "ie":
        pass
        # IE path
    driver.get("https://hudson-poutine-83447.herokuapp.com/")
    driver.maximize_window()

    request.cls.driver = driver # sent to class object
    yield
    driver.close()
