from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;

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
        self.nextButton = None;
        self.pageNumberInput = None;
        self.totalPagesText = None;
        self.numberOfRowsDropdown = None;