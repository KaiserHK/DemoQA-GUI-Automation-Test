from selenium import webdriver;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.common.exceptions import TimeoutException;
from selenium.webdriver.firefox.options import Options;

from BookStoreApplicationTests.Objects.TestBase import TestBase;

import pytest;

from BookStoreApplicationTests.Pages.BookPage import BookPage;
from BookStoreApplicationTests.Pages.BookStoreApiPage import BookStoreApiPage;
from BookStoreApplicationTests.Pages.BookStoreNavigationPage import BookStoreNavigationPage;
from BookStoreApplicationTests.Pages.BookStorePage import BookStorePage;
from BookStoreApplicationTests.Pages.LoginPage import LoginPage;
from BookStoreApplicationTests.Pages.ProfilePage import ProfilePage;
from BookStoreApplicationTests.Pages.RegisterPage import RegisterPage;
from BookStoreApplicationTests.Pages.UserHeaderPage import UserHeaderPage;

class TestLogin (TestBase):

    def test_UserLogsIn(self):
        # Arrange
        username = "SCool";
        password = "ThisIsCool01!";

        # Act
        self.driver.get(self.loginPage.URL);
        self.loginPage.EnterUsername(username);
        self.loginPage.EnterPassword(password);
        self.loginPage.ClickLoginButton();
        self.profilePage.goToBookStoreButton.wait_for_element();

        #Assert
        self.profilePage.VerifyGoToBookStoreButtonIsDisplayed();
    
    def test_LoggedInUserViewsLoginPage(self):
        # Arrange
        username = "SCool";
        password = "ThisIsCool01!";

        # Act
        self.driver.get(self.loginPage.URL);
        self.loginPage.EnterUsername(username);
        self.loginPage.EnterPassword(password);
        self.loginPage.ClickLoginButton();
        self.profilePage.goToBookStoreButton.wait_for_element();
        self.driver.get(self.loginPage.URL);

        # Assert
        self.userHeaderPage.VerifyUsernameOfCurrentUser(username);
    
    def test_LoggedInUserViewsProfilePage(self):
        # Arrange
        username = "SCool";
        password = "ThisIsCool01!";

        # Act
        self.driver.get(self.loginPage.URL);
        self.loginPage.EnterUsername(username);
        self.loginPage.EnterPassword(password);
        self.loginPage.ClickLoginButton();
        self.profilePage.goToBookStoreButton.wait_for_element();

        # Assert
        self.userHeaderPage.VerifyUsernameOfCurrentUser(username);
    
    def test_LoggedInUserViewsBookStorePage(self):
        # Arrange
        username = "SCool";
        password = "ThisIsCool01!";

        # Act
        self.driver.get(self.loginPage.URL);
        self.loginPage.EnterUsername(username);
        self.loginPage.EnterPassword(password);
        self.loginPage.ClickLoginButton();
        self.profilePage.goToBookStoreButton.wait_for_element();
        self.driver.get(self.bookStorePage.URL);
        self.bookStorePage.nextButton.wait_for_element();

        # Assert
        self.userHeaderPage.VerifyUsernameOfCurrentUser(username);