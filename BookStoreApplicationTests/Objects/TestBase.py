from selenium import webdriver;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.common.exceptions import TimeoutException;
from selenium.webdriver.firefox.options import Options;

import pytest;

from BookStoreApplicationTests.Pages.BookPage import BookPage;
from BookStoreApplicationTests.Pages.BookStoreApiPage import BookStoreApiPage;
from BookStoreApplicationTests.Pages.BookStoreNavigationPage import BookStoreNavigationPage;
from BookStoreApplicationTests.Pages.BookStorePage import BookStorePage;
from BookStoreApplicationTests.Pages.LoginPage import LoginPage;
from BookStoreApplicationTests.Pages.ProfilePage import ProfilePage;
from BookStoreApplicationTests.Pages.RegisterPage import RegisterPage;
from BookStoreApplicationTests.Pages.UserHeaderPage import UserHeaderPage;

class TestBase:

    @pytest.fixture(autouse=True)
    def defineDriver(self):
        options = Options();
        options.page_load_strategy = "eager";
        self.driver = webdriver.Firefox(options=options);
        self.definePages();
        yield;
        self.driver.quit();
    
    def definePages(self):
        self.loginPage = LoginPage(self.driver);
        self.registerPage = RegisterPage(self.driver);
        self.profilePage = ProfilePage(self.driver);
        self.bookStoreNavigationPage = BookStoreNavigationPage(self.driver);
        self.bookStorePage = BookStorePage(self.driver);
        self.bookPage = BookPage(self.driver);
        self.bookStoreApiPage = BookStoreApiPage(self.driver);
        self.userHeaderPage = UserHeaderPage(self.driver);