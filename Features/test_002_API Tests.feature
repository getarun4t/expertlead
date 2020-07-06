# Created by arunsasi at 2020-07-03
Feature: To test few API test cases

  Scenario: Testing a POST API request for login URI
    When POST request is sent to the login URI along with the payload
    Then Response status should be 200
    And Response should contain a token

  Scenario: Testing a POST API request for users URI
    When POST request is sent to the users URI along with the payload
    Then Response status should be 201
    And Response should contain name, job, id, createdAt

  Scenario: Testing a GET API request for users URI
    When GET request is sent to the users 3 URI along with the paylond
    Then Response status should be 200
    And Email id in the response should end with @reqres.in
