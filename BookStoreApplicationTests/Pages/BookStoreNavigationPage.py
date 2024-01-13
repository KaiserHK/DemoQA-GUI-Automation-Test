from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from BookStoreApplicationTests.Objects.Element import Element;

class BookStoreNavigationPage:

    def __init__(self, driver):
        self.driver = driver;

        self.bookStoreApplicationMenuHeader = None;
        self.loginMenuButton = Element(driver, By.ID, "item-0");
        self.bookStoreMenuButton = None;
        self.profileMenuButton = None;
        self.bookStoreApiMenuButton = None;
    
    # Actions
    def ClickLoginPageMenuButton(self):
        self.loginMenuButton.Click();
    
    # Assertions
