from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;

class BookStorePage:

    URL = "https://demoqa.com/books";

    searchBoxInput;
    searchBoxButton;
    usernameValue;
    loginButton;
    logoutButton;

    bookStoreTable;
    previousButton;
    nextButton;
    pageNumberInput;
    totalPagesText;
    numberOfRowsDropdown;

    def __init__(self):
        pass;