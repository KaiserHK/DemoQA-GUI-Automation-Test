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
        
        self.invalidPasswordWarningText = Element(driver, By.XPATH, "//p[contains(., 'Passwords must have at least one non alphanumeric character, one digit')]");
        self.verifyCaptchaText = Element(driver, By.XPATH, "//p[text()='Please verify reCaptcha to register!']");

    # Actions
    def EnterFirstName(self, firstName: str) -> None:
        self.firstNameInput.Clear();
        self.firstNameInput.SendKeys(firstName);
    
    def EnterLastName(self, lastName: str) -> None:
        self.lastNameInput.Clear();
        self.lastNameInput.SendKeys(lastName);
    
    def EnterUsername(self, username: str) -> None:
        self.usernameInput.Clear();
        self.usernameInput.SendKeys(username);
    
    def EnterPassword(self, password: str) -> None:
        self.passwordInput.Clear();
        self.passwordInput.SendKeys(password);
    
    def ClickCaptcha(self) -> None:
        self.captcha.Click();
    
    def ClickRegisterButton(self) -> None:
        self.registerButton.Click();
    
    def WaitAndSwitchToCaptchaIframe(self) -> None:
        self.captchaIframe.WaitForIframeAndSwitch();
    
    # Assertions
    def VerifyInvalidPasswordTextIsDisplayed(self) -> None:
        assert self.invalidPasswordWarningText.IsDisplayed();
    
    def VerifyCaptchaTextIsDisplayed(self) -> None:
        assert self.verifyCaptchaText.IsDisplayed();