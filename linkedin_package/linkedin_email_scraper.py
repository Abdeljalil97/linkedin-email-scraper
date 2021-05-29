from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage

class LoginLinkedin(BasePage) : 
    
    
    
    
    
    @property
    def input_email(self):
        locator = (By.ID, 'session_key')
        return BaseElement(driver=self.driver, by=locator[0],value=locator[1])
    
    @property
    def input_password(self):
        locator = (By.ID, 'session_password')
        return BaseElement(driver=self.driver, by=locator[0],value=locator[1])
    @property
    def sign_in(self):
        locator = (By.XPATH, "//button[@type='submit']")
        return BaseElement(driver=self.driver, by=locator[0],value=locator[1])
