from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
class LoginPage:

    URL = "https://demoqa.com/login";

    userFormId: str = "userForm";

    usernameInputId: str = "userName";
    passwordInputId: str = "password";
    loginButtonId: str = "login";
    newUserButtonId: str = "newUser";

    invalidUsernameOrPasswordTextId: str = "name";
    alreadyLoggedInTextId: str = "loading-label";
    alreadyLoggedInProfileLinkLinkText: str = "profile";

    def __init__(self, driver):
        self.driver = driver;
        
        self.userForm = driver.find_element(By.ID, self.userFormId);

        self.usernameInput = driver.find_element(By.ID, self.usernameInputId);
        self.passwordInput = driver.find_element(By.ID, self.passwordInputId);
        self.loginButton = driver.find_element(By.ID, self.loginButtonId);
        self.newUserButton = driver.find_element(By.ID, self.newUserButtonId);

        self.invalidUsernameOrPasswordTextTest = lambda id : driver.find_element(By.ID, id);
        #invalidUsernameOrPasswordText = driver.find_element(By.ID, self.invalidUsernameOrPasswordTextId);
        #alreadyLoggedInText = driver.find_element(By.ID, self.alreadyLoggedInTextId);
        #alreadyLoggedInProfileLink = driver.find_element(By.LINK_TEXT, self.alreadyLoggedInProfileLinkLinkText);
        
    #Actions
    def EnterUsername(self, username: str) -> None:
        self.usernameInput.clear();
        self.usernameInput.send_keys(username);
        #add wait
    
    def EnterPassword(self, password: str) -> None:
        usernameInput.clear();
        usernameInput.send_keys(password);
        #add wait
    
    def ClickLoginButton(self):
        loginButton.click();
        #add wait
    
    def ClickNewUserButton(self):
        newUserButton.click();
        #add wait

    #Asserts
    def VerifyUsernameIsInvalid(self):
        pass;
    
    def VerifyPasswordIsInvalid(self):
        pass;
