from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait
from .base_element import BaseElement

class Pagination(BaseElement):
    def click(self):
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #urls = self.links_account.urls_account
        #print(urls)
        while self.web_element :
            
            for element in self.web_element:
                element.click()
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.find()
                return super().click()

    @property
    def links_account(self):
        locator = (By.XPATH,"//main[@id='main']/div/div/div[2]/ul/li/div/div/div/div/a")
        return BaseElement(driver=self.driver, by=locator[0],value=locator[1])