from selenium import webdriver;
import pytest;
from BookStoreApplicationTests.Pages.LoginPage import LoginPage;

# Add browser availability checking
driver = webdriver.Firefox();


class TestRegistration:
    def test_LoginPage(self):
        driver.get("https://demoqa.com/login");
        loginPage = LoginPage(driver);
        loginPage.EnterUsername("SomeName");

class TestLogin:
    pass;

class TestLogout:
    pass;
