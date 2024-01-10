from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;

class ProfilePage:

    URL = "https://demoqa.com/profile";
    
    profileWrapperContainer;

    bookSearchInput;
    bookSearchButton;
    usernameValueLabel;
    logoutButton;

    collectionsTable;
    deleteRecordActionButton;

    previousButton;
    nextButton;
    pageNumberInput;
    totalPagesText;
    numberOfRowsDropdown;

    goToBookStoreButton;
    deleteAccountButton;
    deleteAllBooksButton;

    notLoggedInLabel;
    loginLink;
    registerLink;


    def __init__(self, driver):
        self.driver = driver;