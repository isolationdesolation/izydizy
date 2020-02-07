# Created by Анечка at 06.02.2020
Feature: Landos

  Scenario: When phone entered incorrectly error notification appears
    When open the main page
    And open menu
    And choose menu block
    And scroll down
    And enter email
    And enter name
    And enter surname
    And enter incorrect phone number
    And enter city
    And enter info
    And press rule button
    And press send button
    Then see the error notification
