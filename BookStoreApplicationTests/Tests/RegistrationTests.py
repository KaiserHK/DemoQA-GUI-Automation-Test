from selenium import webdriver;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.common.exceptions import TimeoutException;
from selenium.webdriver.firefox.options import Options;
from selenium.webdriver.common.alert import Alert;

import pytest;
import requests;
from time import sleep;

from BookStoreApplicationTests.Objects.TestBase import TestBase;
from BookStoreApplicationTests.Objects.User import User;

from BookStoreApplicationTests.Pages.BookPage import BookPage;
from BookStoreApplicationTests.Pages.BookStoreApiPage import BookStoreApiPage;
from BookStoreApplicationTests.Pages.BookStoreNavigationPage import BookStoreNavigationPage;
from BookStoreApplicationTests.Pages.BookStorePage import BookStorePage;
from BookStoreApplicationTests.Pages.LoginPage import LoginPage;
from BookStoreApplicationTests.Pages.ProfilePage import ProfilePage;
from BookStoreApplicationTests.Pages.RegisterPage import RegisterPage;
from BookStoreApplicationTests.Pages.UserHeaderPage import UserHeaderPage;

class TestRegistration (TestBase):
    
    def test_NewUserRegisters(self):
        # Arrange
        user = User();

        # Act
        self.driver.get(self.registerPage.URL);
        self.registerPage.EnterFirstName(user.firstName);
        self.registerPage.EnterLastName(user.lastName);
        self.registerPage.EnterUsername(user.username);
        self.registerPage.EnterPassword(user.password);
        self.registerPage.WaitAndSwitchToCaptchaIframe();
        self.registerPage.captcha.WaitForElementClickable();
        self.registerPage.ClickCaptcha();
        sleep(10); # Tester must manually complete captcha
        self.driver.switch_to.parent_frame();
        self.registerPage.ClickRegisterButton();
        WebDriverWait(self.driver, 5.0).until(EC.alert_is_present());

        # Assert
        assert Alert(self.driver).text == "User Register Successfully.";
    
    def test_NewUserTriesToRegisterWithInvalidPassword(self):
        # Arrange
        user = User();
        invalidPassword = "123";

        # Act
        self.driver.get(self.registerPage.URL);
        self.registerPage.EnterFirstName(user.firstName);
        self.registerPage.EnterLastName(user.lastName);
        self.registerPage.EnterUsername(user.username);
        self.registerPage.EnterPassword(invalidPassword);
        self.registerPage.WaitAndSwitchToCaptchaIframe();
        self.registerPage.captcha.WaitForElementClickable();
        self.registerPage.ClickCaptcha();
        sleep(10); # Tester must manually complete captcha
        self.driver.switch_to.parent_frame();
        self.registerPage.ClickRegisterButton();
        self.registerPage.invalidPasswordWarningText.WaitForElement();

        # Assert
        self.registerPage.VerifyInvalidPasswordTextIsDisplayed();
    
    def test_NewUserTriesToRegisterWithoutCompletingCaptcha(self):
        # Arrange
        user = User();

        # Act
        self.driver.get(self.registerPage.URL);
        self.registerPage.EnterFirstName(user.firstName);
        self.registerPage.EnterLastName(user.lastName);
        self.registerPage.EnterUsername(user.username);
        self.registerPage.EnterPassword(user.password);
        self.registerPage.ClickRegisterButton();
        self.registerPage.verifyCaptchaText.WaitForElement();

        # Assert
        self.registerPage.VerifyCaptchaTextIsDisplayed();