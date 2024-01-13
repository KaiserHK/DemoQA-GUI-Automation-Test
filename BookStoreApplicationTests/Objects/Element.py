from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.common.exceptions import TimeoutException;

class Element:
    def __init__(self, driver, byFlag, locator: str):
        self.driver = driver;
        self.element = lambda byFlag, locator : driver.find_element(byFlag, locator);
        self.byFlag = byFlag;
        self.locator = locator;
    
    # Actions
    def Clear(self) -> None:
        self.element(self.byFlag, self.locator).clear();
    
    def SendKeys(self, string: str) -> None:
        self.element(self.byFlag, self.locator).send_keys(string);
    
    def Click(self) -> None:
        self.element(self.byFlag, self.locator).click();
    
    def WaitForElement(self, delay: float = 5.0) -> None:
        self.WaitFor(EC.presence_of_element_located((self.byFlag, self.locator)), delay);
    
    def WaitForElementClickable(self, delay: float = 5.0) -> None:
        self.WaitFor(EC.element_to_be_clickable((self.byFlag, self.locator)), delay);
    
    def WaitForIframeAndSwitch(self, delay: float = 5.0) -> None:
        self.WaitFor(EC.frame_to_be_available_and_switch_to_it((self.byFlag, self.locator)), delay);
    
    def WaitFor(self, condition, delay: float) -> None:
        wait = WebDriverWait(self.driver, delay);
        wait.until(condition);
    
    # Getters
    def GetText(self) -> str:
        return self.element(self.byFlag, self.locator).text;
    
    # Assertions
    def IsDisplayed(self) -> bool:
        try:
            return self.element(self.byFlag, self.locator).is_displayed();
        except:
            print("Error accessing element.");
            return False;