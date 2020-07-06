import pytest
from Drivers.chromedriver import driver
from Pages.Dashboard import Dashboard
import time
from Synchronization.Custom_wait import wait_and_click, wait_till_element_appears


@pytest.fixture(scope="function", autouse=True)
def post_function():
    yield driver
    wait_till_element_appears("xpath", Dashboard.dresses, 0.1)

@pytest.fixture(scope="session", autouse=True)
def posttest():
    yield driver
    driver.quit()