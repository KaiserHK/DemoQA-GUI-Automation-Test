from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;

class LoginPage:

    URL = "https://demoqa.com/login";

    userForm;
    welcomeHeader;

    usernameInput;
    passwordInput;
    loginButton;
    newUserButton;

    invalidUsernameOrPasswordText;

    alreadyLoggedInText;
    alreadyLoggedInProfileLink;

    def __init__(self, driver):
        self.driver = driver;
        

    #Actions
    def EnterUsername():
        pass;
    
    def EnterPassword():
        pass;
    
    def ClickLoginButton():
        pass;
    
    def ClickNewUserButton():
        pass;

    #Asserts
    def VerifyUsernameIsInvalid():
        pass;
    
    def VerifyPasswordIsInvalid():
        pass;