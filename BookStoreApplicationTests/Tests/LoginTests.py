from selenium import webdriver;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.common.exceptions import TimeoutException;
from selenium.webdriver.firefox.options import Options;

from BookStoreApplicationTests.Objects.TestBase import TestBase;
from BookStoreApplicationTests.Objects.User import User;

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
        user = User();
        user.RegisterUserViaApi();

        # Act
        self.driver.get(self.loginPage.URL);
        self.loginPage.EnterUsername(user.username);
        self.loginPage.EnterPassword(user.password);
        self.loginPage.ClickLoginButton();
        self.profilePage.goToBookStoreButton.WaitForElement();

        #Assert
        self.profilePage.VerifyGoToBookStoreButtonIsDisplayed();
    
    def test_LoggedInUserViewsLoginPage(self):
        # Arrange
        user = User();
        user.RegisterUserViaApi();

        # Act
        self.driver.get(self.loginPage.URL);
        self.loginPage.EnterUsername(user.username);
        self.loginPage.EnterPassword(user.password);
        self.loginPage.ClickLoginButton();
        self.profilePage.goToBookStoreButton.WaitForElement();
        self.driver.get(self.loginPage.URL);

        # Assert
        self.userHeaderPage.VerifyUsernameOfCurrentUser(user.username);
    
    def test_LoggedInUserViewsProfilePage(self):
        # Arrange
        user = User();
        user.RegisterUserViaApi();

        # Act
        self.driver.get(self.loginPage.URL);
        self.loginPage.EnterUsername(user.username);
        self.loginPage.EnterPassword(user.password);
        self.loginPage.ClickLoginButton();
        self.profilePage.goToBookStoreButton.WaitForElement();

        # Assert
        self.userHeaderPage.VerifyUsernameOfCurrentUser(user.username);
    
    def test_LoggedInUserViewsBookStorePage(self):
        # Arrange
        user = User();
        user.RegisterUserViaApi();

        # Act
        self.driver.get(self.loginPage.URL);
        self.loginPage.EnterUsername(user.username);
        self.loginPage.EnterPassword(user.password);
        self.loginPage.ClickLoginButton();
        self.profilePage.goToBookStoreButton.WaitForElement();
        self.driver.get(self.bookStorePage.URL);
        self.bookStorePage.nextButton.WaitForElement();

        # Assert
        self.userHeaderPage.VerifyUsernameOfCurrentUser(user.username);