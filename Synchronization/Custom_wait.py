from Drivers.chromedriver import driver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 30)

def wait_and_click(locator_type, element, polling_interval):
    if locator_type == "id":
        while (len(driver.find_elements_by_id(element))==0):
            time.sleep(polling_interval)
        driver.find_element_by_id(element).click()
    elif locator_type == "xpath":
        while (len(driver.find_elements_by_xpath(element))==0):
            time.sleep(polling_interval)
        driver.find_element_by_xpath(element).click()

def wait_till_element_appears(locator_type, element, polling_interval):
    if locator_type == "id":
        while (len(driver.find_elements_by_id(element))==0):
            time.sleep(polling_interval)
    elif locator_type == "xpath":
        while (len(driver.find_elements_by_xpath(element))==0):
            time.sleep(polling_interval)

def wait_till_element_disappears(locator_type, element, polling_interval):
    if locator_type == "id":
        while (len(driver.find_elements_by_id(element))>0):
            time.sleep(polling_interval)
    elif locator_type == "xpath":
        while (len(driver.find_elements_by_xpath(element))>0):
            time.sleep(polling_interval)

def wait_to_display(element):
    wait.until(EC.visibility_of_any_elements_located(By.XPATH, element))