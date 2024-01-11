from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;

class BookPage:

    URL = "https://demoqa.com/books?book=9781449331818";

    def __init__(self, driver):
        self.driver = driver;

        self.usernameText = None;
        self.logoutButton = None;

        self.ISBNLabel = None;
        self.ISBNText = None;
        self.titleLabel = None;
        self.titleText = None;
        self.subTitleLabel = None;
        self.subTitleText = None;
        self.authorLabel = None;
        self.authorText = None;
        self.publisherLabel = None;
        self.publisherText = None;
        self.totalPagesLabel = None;
        self.totalPagesText = None;
        self.descriptionLabel = None;
        self.descriptionText = None;
        self.websiteLabel = None;
        self.websiteText = None;

        self.backToBookStoreButton = None;
        self.addToYourCollectionButton = None;
    