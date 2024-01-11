from selenium import webdriver;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.common.exceptions import TimeoutException;
from selenium.webdriver.firefox.options import Options;

import pytest;

from BookStoreApplicationTests.Pages.LoginPage import LoginPage;
from BookStoreApplicationTests.Pages.RegisterPage import RegisterPage;
from BookStoreApplicationTests.Pages.ProfilePage import ProfilePage;
from BookStoreApplicationTests.Pages.BookStoreNavigationPage import BookStoreNavigationPage;
from BookStoreApplicationTests.Pages.BookStorePage import BookStorePage;
from BookStoreApplicationTests.Pages.BookPage import BookPage;
from BookStoreApplicationTests.Pages.BookStoreApiPage import BookStoreApiPage;

class TestLogin:

    @pytest.fixture(autouse=True)
    def Driver(self):
        options = Options();
        options.page_load_strategy = "eager";
        self.driver = webdriver.Firefox(options=options);
        yield;
        self.driver.quit();

    def test_UserLogsIn(self):
        # Arrange
        driver = self.driver;
        loginPage = LoginPage(driver);
        profilePage = ProfilePage(driver);
        username = "SCool";
        password = "ThisIsCool01!";

        # Act
        driver.get(loginPage.URL);
        loginPage.EnterUsername(username);
        loginPage.EnterPassword(password);
        loginPage.ClickLoginButton();
        profilePage.goToBookStoreButton.wait_for_element();

        #Assert
        profilePage.VerifyGoToBookStoreButtonIsDisplayed();
    
    def test_LoggedInUserViewsLoginPage(self):
        # Arrange
        driver = self.driver;
        loginPage = LoginPage(driver);
        profilePage = ProfilePage(driver);
        bookStoreNavigationPage = BookStoreNavigationPage(driver);

        username = "SCool";
        password = "ThisIsCool01!";

        # Act
        driver.get(loginPage.URL);
        loginPage.EnterUsername(username);
        loginPage.EnterPassword(password);
        loginPage.ClickLoginButton();
        profilePage.goToBookStoreButton.wait_for_element();
        driver.get(loginPage.URL);

        # Assert
        loginPage.VerifyUsernameOfCurrentUser(username);
    
    def test_LoggedInUserViewsProfilePage(self):
        # Arrange
        # Act
        # Assert
        pass;
    
    def test_LoggedInUserViewsBookStorePage(self):
        # Arrange
        # Act
        # Assert
        pass;