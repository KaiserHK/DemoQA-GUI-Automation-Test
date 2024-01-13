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
        self.registerPage.captcha.wait_for_element_clickable();
        self.registerPage.ClickCaptcha();
        sleep(10); # Tester must manually complete captcha
        self.driver.switch_to.parent_frame();
        self.registerPage.ClickRegisterButton();
        WebDriverWait(self.driver, 5.0).until(EC.alert_is_present());
        
        # cookieFile = open("./../Objects/CaptchaCookie.txt", "r");
        # cookie = cookieFile.readline();
        # print(cookie);
        # cookieFile.close();
        # if (cookie == ""):
        #     self.registerPage.ClickCaptcha();
        #     sleep(10);
        #     cookieFile = open("./../Objects/CaptchaCookie.txt", "w+");
        #     cookie = self.driver.get_cookie("_GRECAPTCHA");
        #     print(cookie["value"]);
        #     cookieFile.writelines(cookie["value"]);
        #     cookieFile.close();
        # else:
        #     self.driver.add_cookie({'name' : '_GRECAPTCHA', 'value' : cookie});
        #     self.registerPage.ClickCaptcha();
        #     self.registerPage.captchaSpinner.wait_for_element_is_not_displayed();

        # Assert
        assert Alert(self.driver).text == "User Register Successfully.";
    
    def test_NewUserTriesToRegisterWithInvalidPassword(self):
        # Arrange
        # Act
        # Assert
        pass;
    
    def test_NewUserTriesToRegisterWithoutCompletingCaptcha(self):
        # Arrange
        # Act
        # Assert
        pass;