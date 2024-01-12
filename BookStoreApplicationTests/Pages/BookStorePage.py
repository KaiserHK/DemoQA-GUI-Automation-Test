from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from BookStoreApplicationTests.Objects.Element import Element;

class BookStorePage:

    URL = "https://demoqa.com/books";

    def __init__(self, driver):
        self.driver = driver;

        self.searchBoxInput = None;
        self.searchBoxButton = None;
        self.usernameValue = None;
        self.loginButton = None;
        self.logoutButton = None;

        self.bookStoreTable = None;
        self.previousButton = None;
        self.nextButton = Element(driver, By.XPATH, "//button[@class='-btn' and text()='Next']");
        self.pageNumberInput = None;
        self.totalPagesText = None;
        self.numberOfRowsDropdown = None;