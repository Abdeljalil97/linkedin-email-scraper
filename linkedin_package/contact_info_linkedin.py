from selenium.webdriver.common.by import By
from .base_page import BasePage
from .base_element import BaseElement

class ContactInfo(BasePage):
     #url = "https://www.linkedin.com/in/scott-anthony-gould-7a248651/detail/contact-info/"
     def __init__(self, driver, url):
          
          self.links = []
          super().__init__(driver, url)
     def go(self):
          for urls in self.url :
               for url in urls:
                    if url : 
                         print(url)
                         self.driver.get(url)
                         contact_info = self.links_contact_infos.contact_info_links
                         self.links.append(contact_info)
                         
          return super().go()
     def get_info_contact(self):
     
          return self.links
     @property
     def links_contact_infos(self):
          locator = (By.XPATH,"//section[@class='pv-profile-section pv-contact-info artdeco-container-card ember-view']") 
     
          return BaseElement(driver=self.driver, by=locator[0],value=locator[1])

     @property
     def emails(self):
          locator = (By.TAG_NAME,"html")
          return BaseElement(driver=self.driver, by=locator[0],value=locator[1])