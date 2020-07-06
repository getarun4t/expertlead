from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#For Docker Run
options = webdriver.ChromeOptions()
URL = 'http://localhost:4444/wd/hub'
options.add_argument("--incognito")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--no-sandbox")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-gpu")

driver = webdriver.Remote(command_executor=URL,
                          desired_capabilities=options.to_capabilities())

#For Local Run
# options = webdriver.ChromeOptions()
# options.add_argument("--incognito")
# chromedriver = '/usr/local/bin/chromedriver'
# driver = webdriver.Chrome(chromedriver, chrome_options=options)
# driver.maximize_window()