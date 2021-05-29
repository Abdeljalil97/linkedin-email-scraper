from selenium.webdriver.common.by import By
from .base_page import BasePage
from .base_element import BaseElement

class LinksAccount(BasePage):
    
    @property
    def links_account(self):
        locator = (By.XPATH,"//main[@id='main']/div/div/div[2]/ul/li/div/div/div/div/a")
        return BaseElement(driver=self.driver, by=locator[0],value=locator[1])