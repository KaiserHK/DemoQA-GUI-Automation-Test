from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from BookStoreApplicationTests.Objects.Element import Element;

class BookStoreApiPage:

    URL = "";
    
    def __init__(self, driver):
        self.driver = driver;