from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from BookStoreApplicationTests.Objects.Element import Element;

class LoginPage:

    URL = "https://demoqa.com/login";

    def __init__(self, driver):
        self.driver = driver;

        self.userForm = Element(driver, By.ID, "userForm");

        self.usernameInput = Element(driver, By.ID, "userName");
        self.passwordInput = Element(driver, By.ID, "password");
        self.loginButton = Element(driver, By.ID, "login");
        self.newUserButton = Element(driver, By.ID, "newUser");
        
        self.invalidUsernameOrPasswordText = Element(driver, By.ID, "name");
        self.alreadyLoggedInProfileLink = Element(driver, By.ID, "loading-label");
        self.alreadyLoggedInProfileLinkLinkText = Element(driver, By.LINK_TEXT, "profile");
        
    #Actions
    def EnterUsername(self, username: str) -> None:
        self.usernameInput.clear();
        self.usernameInput.send_keys(username);
        #add wait
    
    def EnterPassword(self, password: str) -> None:
        self.passwordInput.clear();
        self.passwordInput.send_keys(password);
        #add wait
    
    def ClickLoginButton(self):
        self.loginButton.click();
        #add wait
    
    def ClickNewUserButton(self):
        self.newUserButton.click();
        #add wait

    #Asserts
    def VerifyUsernameIsInvalid(self):
        pass;
    
    def VerifyPasswordIsInvalid(self):
        pass;
