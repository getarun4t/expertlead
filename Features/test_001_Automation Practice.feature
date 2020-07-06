# Created by arunsasi at 2020-07-03
Feature: Automation Practice website
  This feature file is designed to test the Automation Practice website

  Scenario: To test the login process
    Given Automation Practice website is opened
    When User clicks Sign-in Page
    And Clicks Create Account
    And Enter the mandatory details in the form
    Then New Account is created
    And Name is appearing in the page

  Scenario: To test the Home Page
    Given Automation Practice website is opened
    When User clicks on Your Logo icon
    Then Home Page should open
    And Women,Dresses,T-shirts tab are displayed and enabled
    And Popular tab should be selected

  Scenario: To test DRESSES option
    Given Automation Practice website is opened
    When User clicks on Your Logo icon
    And User clicks on Dresses
    Then Dresses page should open
    And Checkboxes should not be selected
    And Items should be displayed in Grid View

  Scenario: To test List view in DRESSES option
    Given Automation Practice website is opened
    When User clicks on Your Logo icon
    And User clicks on Dresses
    And User selects List view
    Then Items should display in List view
    And Prices should be displayed for all results

  Scenario: To test SUMMER DRESSES filter in DRESSES option
    Given Automation Practice website is opened
    When User clicks on Your Logo icon
    And User clicks on Dresses
    And User selects Summer dresses
    Then Summer Dresses page should open
    And All results contain summer dress

