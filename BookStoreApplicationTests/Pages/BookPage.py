from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;

class BookPage:

    URL = "https://demoqa.com/books?book=9781449331818";

    usernameText;
    logoutButton;

    ISBNLabel;
    ISBNText;
    titleLabel;
    titleText;
    subTitleLabel;
    subTitleText;
    authorLabel;
    authorText;
    publisherLabel;
    publisherText;
    totalPagesLabel;
    totalPagesText;
    descriptionLabel;
    descriptionText;
    websiteLabel;
    websiteText;

    backToBookStoreButton;
    addToYourCollectionButton;

    def __init__(self):
        pass;
    