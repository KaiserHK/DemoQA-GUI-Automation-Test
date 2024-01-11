Feature: Login

    Background:
        Given a user who has navigated to the login page
        And the user is registered

    Scenario: User logs in
        Given the user entered valid credentials
        When the user clicks the login button
        Then the user will be logged in
    
    Scenario: Logged in user views login page
        Given the user is logged in
        When the user navigates to the login page
        Then the user will see his username
        And the user will see the logout button
        And the user will see the already logged in text
        And the user will see the profile page link
    
    Scenario: Logged in user views profile page
        Given the user is logged in
        When the user navigates to the profile page
        Then the user will see his username
        And the user will see the logout button
    
    Scenario: Logged in user views book store page
        Given the user is logged in
        When the user navigates to the book store page
        Then the user will see his username
        And the user will see the logout button