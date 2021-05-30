from selenium.webdriver.common.by import By
from .base_page import BasePage
from .base_element import BaseElement
from .pagination import Pagination

class LinksAccount(BasePage):
    def __init__(self, driver, url):
        self.links = []
        super().__init__(driver,url='https://www.linkedin.com/search/results/people/?keywords=maryland&origin=SWITCH_SEARCH_VERTICAL&page=1')

    def go(self):
        
        for i in range(1,10):
            self.url = 'https://www.linkedin.com/search/results/people/?keywords=maryland&origin=SWITCH_SEARCH_VERTICAL&page={i}'.format(i=i)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.driver.get(self.url)
            urls=self.links_account.urls_account
            self.links.append(urls)
            

            
     
        return super().go()
    
    def print_links(self):
         
        return self.links

        

    @property
    def links_account(self):
        locator = (By.XPATH,"//main[@id='main']/div/div/div[2]/ul/li/div/div/div/div/a")
        return BaseElement(driver=self.driver, by=locator[0],value=locator[1])
    
    
