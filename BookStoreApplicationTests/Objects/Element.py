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
    def clear(self) -> None:
        self.element(self.byFlag, self.locator).clear();
    
    def send_keys(self, string: str) -> None:
        self.element(self.byFlag, self.locator).send_keys(string);
    
    def click(self) -> None:
        self.element(self.byFlag, self.locator).click();
    
    def wait_for_element(self, delay: float = 5.0) -> None:
        wait = WebDriverWait(self.driver, delay);
        wait.until(EC.presence_of_element_located((self.byFlag, self.locator)));
    
    def wait_for_element_clickable(self, delay: float = 5.0) -> None:
        wait = WebDriverWait(self.driver, delay);
        wait.until(EC.element_to_be_clickable((self.byFlag, self.locator)));
    
    def wait_for_frame_and_switch_to_it(self, delay: float = 5.0) -> None:
        wait = WebDriverWait(self.driver, delay);
        wait.until(EC.frame_to_be_available_and_switch_to_it((self.byFlag, self.locator)));
    
    def wait_for_element_is_not_displayed(self, delay: float = 5.0) -> None:
        wait = WebDriverWait(self.driver, delay);
        wait.until(EC.invisibility_of_element_located((self.byFlag, self.locator)));
    
    # Getters
    def get_text(self) -> str:
        return self.element(self.byFlag, self.locator).text;
    
    # Assertions
    def is_displayed(self) -> bool:
        try:
            return self.element(self.byFlag, self.locator).is_displayed();
        except:
            print("Error accessing element.");
            return False;