from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from BookStoreApplicationTests.Objects.Element import Element;

class UserHeaderPage:

    def __init__(self, driver):
        self.driver = driver;

        self.loginButton = Element(driver, By.ID, "login");
        self.username = Element(driver, By.ID, "userName-value");
        self.logoutButton = Element(driver, By.ID, "submit");
    
    # Actions

    # Assertions
    def VerifyUsernameOfCurrentUser(self, expectedUsername: str) -> None:
        assert self.username.GetText() == expectedUsername;