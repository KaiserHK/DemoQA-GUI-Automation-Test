from selenium import webdriver;
import pytest;
from BookStoreApplicationTests.Pages.LoginPage import LoginPage;
from BookStoreApplicationTests.Pages.ProfilePage import ProfilePage;

# Add browser availability checking and/or create Driver class to wrap driver
driver = webdriver.Firefox();
driver.implicitly_wait(5);

class TestRegistration:

    def test_LoginToBookStore(self):
        # Arrange
        loginPage = LoginPage(driver);
        profilePage = ProfilePage(driver);
        url = loginPage.URL;
        username = "SCool";
        password = "ThisIsCool01!";

        # Act
        driver.get(url);
        loginPage.EnterUsername(username);
        loginPage.EnterPassword(password);
        loginPage.ClickLoginButton();

        #Assert
        assert profilePage.VerifyIsGoToBookStoreButtonIsDisplayed() == True;


class TestLogin:
    pass;

class TestLogout:
    pass;
