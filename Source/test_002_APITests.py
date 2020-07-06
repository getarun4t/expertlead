from pytest_bdd import scenario, when, then, parsers
from Source.settings import API

api1 = API()

@scenario('../Features/test_002_API Tests.feature','Testing a POST API request for login URI')
def test_post_login():
    pass

@scenario('../Features/test_002_API Tests.feature','Testing a POST API request for users URI')
def test_post_users():
    pass

@scenario('../Features/test_002_API Tests.feature','Testing a GET API request for users URI')
def test_get_users():
    pass

@when("POST request is sent to the login URI along with the payload")
def login():
    payload = {"email": "eve.holt@reqres.in","password": "cityslicka"}
    api1.post_api("https://reqres.in/api/login", payload)


@when("POST request is sent to the users URI along with the payload")
def users():
    payload = {"name": "Arun Sasi", "job": "QA Automation Engineer"}
    api1.post_api("https://reqres.in/api/users", payload)


@when("GET request is sent to the users 3 URI along with the paylond")
def get_user():
    api1.get_api("https://reqres.in/api/users/3")


@then(parsers.parse("Response status should be {code}"))
def response(code):
    assert api1.resp.status_code == int(code)

@then("Response should contain a token")
def response_id():
    assert api1.json_text['token']
    print(api1.json_text['token'])


@then("Response should contain name, job, id, createdAt")
def response_user():
    assert api1.json_text['name']
    assert api1.json_text['job']
    assert api1.json_text['id']
    assert api1.json_text['createdAt']
    print(api1.json_text['id'])

@then("Response should contain a token")
def response_id():
    assert api1.json_text['token']
    print(api1.json_text['token'])

@then(parsers.parse("Email id in the response should end with {expected}"))
def response_id(expected):
    email = str(api1.json_text['data']['email'])
    domain = email.split("@")
    assert str("@"+domain[1]) == str(expected)
