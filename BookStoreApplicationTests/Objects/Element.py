from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;

class Element:
    def __init__(self, driver, byFlag, locator: str):
        self.element = lambda byFlag, locator : driver.find_element(byFlag, locator);
        self.byFlag = byFlag;
        self.locator = locator;
    
    # Actions
    def clear(self) -> None:
        self.element(self.byFlag, self.locator).clear();
    
    def send_keys(self, string: str) -> None:
        self.element(self.byFlag, self.locator).send_keys(string);
    
    def click(self) -> None:
        self.element(self.byFlag, self.locator).click();
    
    # Assertions
    def is_displayed(self) -> bool:
        try:
            return self.element(self.byFlag, self.locator).is_displayed();
        except:
            print("Error accessing element.");
            return False;