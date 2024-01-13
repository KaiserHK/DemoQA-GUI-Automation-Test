from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from BookStoreApplicationTests.Objects.Element import Element;

class RegisterPage:
    
    URL = "https://demoqa.com/register";

    def __init__(self, driver):
        self.driver = driver;

        self.firstNameInput = Element(driver, By.ID, "firstname");
        self.lastNameInput = Element(driver, By.ID, "lastname");
        self.usernameInput = Element(driver, By.ID, "userName");
        self.passwordInput = Element(driver, By.ID, "password");

        self.captchaIframe = Element(driver, By.XPATH, "//iframe[@title='reCAPTCHA']");
        self.captcha = Element(driver, By.CSS_SELECTOR, "span#recaptcha-anchor");
        self.captchaSpinner = Element(driver, By.CSS_SELECTOR, "div.recaptcha-checkbox-spinner");
        self.registerButton = Element(driver, By.ID, "register");
    
    def EnterFirstName(self, firstName: str) -> None:
        self.firstNameInput.clear();
        self.firstNameInput.send_keys(firstName);
    
    def EnterLastName(self, lastName: str) -> None:
        self.lastNameInput.clear();
        self.lastNameInput.send_keys(lastName);
    
    def EnterUsername(self, username: str) -> None:
        self.usernameInput.clear();
        self.usernameInput.send_keys(username);
    
    def EnterPassword(self, password: str) -> None:
        self.passwordInput.clear();
        self.passwordInput.send_keys(password);
    
    def ClickCaptcha(self) -> None:
        self.captcha.click();
    
    def ClickRegisterButton(self) -> None:
        self.registerButton.click();
    
    def WaitAndSwitchToCaptchaIframe(self) -> None:
        self.captchaIframe.wait_for_frame_and_switch_to_it();