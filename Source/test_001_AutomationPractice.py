from Drivers.chromedriver import driver
from Pages.Dashboard import Dashboard, Dresses
import pytest
from Pages.AccountPage import Account
from Pages.SignUpForm import Form
from Source.settings import Environment, Actions
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenario, given, when, then, parsers
import time
from Synchronization.Custom_wait import wait_and_click, wait_till_element_appears, wait_to_display, \
    wait_till_element_disappears
from selenium.webdriver.common.action_chains import ActionChains
actions = Actions()

@pytest.mark.run(order=1)
@scenario('../Features/test_001_Automation Practice.feature','To test the login process')
def test_login_page():
    pass

@pytest.mark.run(order=2)
@scenario('../Features/test_001_Automation Practice.feature','To test the Home Page')
def test_home_page():
    pass

@pytest.mark.run(order=3)
@scenario('../Features/test_001_Automation Practice.feature','To test DRESSES option')
def test_dresses():
    pass

@pytest.mark.run(order=4)
@scenario('../Features/test_001_Automation Practice.feature','To test List view in DRESSES option')
def test_list():
    pass

@pytest.mark.run(order=5)
@scenario('../Features/test_001_Automation Practice.feature','To test SUMMER DRESSES filter in DRESSES option')
def test_summer():
    pass


@given("Automation Practice website is opened")
def logging_in():
    driver.get(Environment.url)
    wait_till_element_appears("xpath", Dashboard.dresses, 0.1)


@when("User clicks Sign-in Page")
def username_password():
    wait_and_click("xpath", Dashboard.sign_in, 0.1)


@when("User clicks on Your Logo icon")
def logo():
    wait_and_click("xpath", Dashboard.logo, 0.1)


@when("Clicks Create Account")
def create_account():
    wait_till_element_appears("xpath", Account.new_email, 0.1)
    driver.find_element_by_xpath(Account.new_email).send_keys(Environment.email)
    wait_and_click("xpath", Account.create, 0.1)

@when("User selects List view")
def list_view():
    wait_and_click("xpath", Dresses.list, 0.1)
    count = 0
    while (len(driver.find_elements_by_xpath(Dresses.list_selected)) == 0):
        count = count + 1
        if (count == 500):
            wait_and_click("xpath", Dresses.list, 0.1)
            break

@when("User selects Summer dresses")
def summer():
    wait_till_element_disappears("xpath", Dresses.grid, 0.1)
    wait_till_element_appears("xpath", Dresses.grid, 0.1)
    time.sleep(6)
    driver.find_element_by_xpath(Dresses.summer_options).click()
    #wait_and_click("xpath", Dresses.summer_options, 0.1)

@when(parsers.parse("User clicks on {tab}"))
def dresses(tab):
    wait_till_element_appears("xpath", Dashboard.tabs.format(tab), 0.1)
    wait_and_click("xpath", Dashboard.dresses, 0.1)


@when("Enter the mandatory details in the form")
def details():
    wait_till_element_appears("id", Form.f_name, 0.1)
    driver.find_element_by_id(Form.f_name).send_keys(Environment.f_name)
    driver.find_element_by_id(Form.l_name).send_keys(Environment.l_name)
    driver.find_element_by_id(Form.password).send_keys(Environment.password)
    wait_till_element_appears("id", Form.company, 0.1)
    driver.find_element_by_id(Form.company).send_keys(Environment.company)
    driver.find_element_by_id(Form.address_1).send_keys(Environment.address_1)
    driver.find_element_by_id(Form.city).send_keys(Environment.city)
    actions.dropdown(Form.state, Environment.state)
    driver.find_element_by_id(Form.postcode).send_keys(Environment.postcode)
    driver.find_element_by_id(Form.mobile).send_keys(Environment.mobile)
    wait_and_click("xpath", Form.register, 0.1)


@then("New Account is created")
def new_acc():
    wait_till_element_appears("xpath", Account.my_account, 0.1)


@then(parsers.parse("{dress} page should open"))
def dresses_page(dress):
    wait_till_element_appears("xpath", Dashboard.women, 0.1)
    driver.find_element_by_xpath(Dashboard.women).send_keys(Keys.PAGE_DOWN)
    assert (len(driver.find_elements_by_xpath(Dresses.dresses.format(dress)))) > 0

@then("Checkboxes should not be selected")
def checkbox():
    assert (len(driver.find_elements_by_xpath(Dresses.checkbox))) == 0


@then("Items should be displayed in Grid View")
def checkbox():
    # driver.find_element_by_xpath(Dashboard.logo).send_keys(Keys.PAGE_DOWN)
    wait_till_element_appears("xpath", Dresses.grid, 0.1)
    wait_till_element_appears("xpath", Dresses.list, 0.1)
    assert driver.find_element_by_xpath(Dresses.grid).text == "Grid"


@then("Home Page should open")
def home():
    wait_till_element_appears("xpath", Dashboard.women, 0.1)
    assert (len(driver.find_elements_by_xpath(Dashboard.home_check))) == 0


@then("Popular tab should be selected")
def popular():
    driver.find_element_by_xpath(Dashboard.women).send_keys(Keys.PAGE_DOWN)
    wait_till_element_appears("xpath", Dashboard.popular, 0.1)
    assert (driver.find_element_by_xpath(Dashboard.active).text) == "POPULAR"


@then(parsers.parse("{tab} tab are displayed and enabled"))
def tabs(tab):
    tabs = [x.strip() for x in tab.split(',')]
    for i in tabs:
        assert (len(driver.find_elements_by_xpath(Dashboard.tabs.format(i)))) > 0


@then("Name is appearing in the page")
def name_check():
    name = driver.find_element_by_xpath(Account.acc_name).text
    name_2 = Environment.f_name+" "+Environment.l_name
    assert name == name_2

@then("Items should display in List view")
def list_view():
    wait_till_element_appears("xpath", Dresses.list_view, 0.1)
    assert (len(driver.find_elements_by_xpath(Dresses.list_view))) > 0


@then("Prices should be displayed for all results")
def prices():
    prices = len(driver.find_elements_by_xpath(Dresses.price))
    assert item_count() == int((prices/2))

@then("All results contain summer dress")
def count():
    summer_count = len(driver.find_elements_by_xpath(Dresses.summer))
    assert item_count() == summer_count


def item_count():
    items = driver.find_element_by_xpath(Dresses.items).text
    count = items.split()
    return (int(count[5]))