Feature: New user registration

    Background:
        Given a user who is not registered
        And the user has navigated to the registration page

    Scenario: A new user registers
        Given a user inputs his valid information
        And the user completes the CAPTCHA
        When the user clicks the register button
        Then the user will see a successful alert message
    
    Scenario: A new user tries to register with invalid password
        Given a user inputs his valid information
        And the user completes the CAPTCHA
        But the user inputs an invalid password
        When the user clicks the register button
        Then the user will not be registered
        And the user will see the password requirements text
    
    Scenario: A new user tries to register without completing the CAPTCHA
        Given a user inputs his valid information
        But the user does not complete the CAPTCHA
        When the user clicks the register button
        Then the user will not be registered
        And the user will see the verify CAPTCHA text