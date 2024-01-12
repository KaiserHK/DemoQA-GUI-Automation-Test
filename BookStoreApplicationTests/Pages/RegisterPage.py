from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;

class RegisterPage:
    
    URL = "https://demoqa.com/register";

    def __init__(self, driver):
        self.driver = driver;