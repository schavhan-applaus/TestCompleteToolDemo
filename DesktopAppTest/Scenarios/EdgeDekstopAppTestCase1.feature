Feature: Edge Browser Desktop Application Testing
  As a user, I want to test various functionalities and properties of the Edge browser desktop application.

  Scenario: Verify Dark mode functionality
    Given I launch the Edge browser application
    When I navigate to the "edge://settings/" URL
    When I click on the Appearance option using OCR
    And I click on the Mode option using OCR
    When I select the Dark mode option
    Then Dark mode should be selected
    Then I close the browser window

  Scenario: Verify Light mode functionality
    Given I launch the Edge browser application
    When I navigate to the "edge://settings/" URL
    When I click on the Appearance option using OCR
    And I click on the Mode option using OCR
    When I select the Light mode option
    Then Light mode should be selected
    Then I close the browser window
