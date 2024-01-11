from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from BookStoreApplicationTests.Objects.Element import Element;

class ProfilePage:

    URL = "https://demoqa.com/profile";

    def __init__(self, driver):
        self.driver = driver;

        self.profileWrapperContainer = None;

        self.bookSearchInput = None;
        self.bookSearchButton = None;
        self.usernameValueLabel = None;
        self.logoutButton = None;

        self.collectionsTable = None;
        self.deleteRecordActionButton = None;

        self.previousButton = None;
        self.nextButton = None;
        self.pageNumberInput = None;
        self.totalPagesText = None;
        self.numberOfRowsDropdown = None;

        self.goToBookStoreButton = Element(driver, By.ID, "gotoStore");
        self.deleteAccountButton = None;
        self.deleteAllBooksButton = None;

        self.notLoggedInLabel = None;
        self.loginLink = None;
        self.registerLink = None;
    
    # Actions

    # Assertions
    def VerifyGoToBookStoreButtonIsDisplayed(self) -> None:
        assert self.goToBookStoreButton.is_displayed() == True;