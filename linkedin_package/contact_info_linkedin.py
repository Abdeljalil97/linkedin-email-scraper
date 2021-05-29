from selenium.webdriver.common.by import By
from .base_page import BasePage
from .base_element import BaseElement

class ContactInfo(BasePage):
   #url = "https://www.linkedin.com/in/scott-anthony-gould-7a248651/detail/contact-info/"
   def __init__(self, driver, url):
        self.url = list(url)
        super().__init__(driver, url)
   def go(self):
        for url in self.url :
            link = url.split('?')
            print(link)
            link = link[0]
            url = "{a}/detail/contact-info/".format(a=link)
            print(url)
            self.driver.get(url)
        return super().go()
   @property
   def links_contact_infos(self):
        locator = (By.XPATH,"//section[@class='pv-profile-section pv-contact-info artdeco-container-card ember-view']") 
   
        return BaseElement(driver=self.driver, by=locator[0],value=locator[1])

   @property
   def emails(self):
      locator = (By.TAG_NAME,"html")
      return BaseElement(driver=self.driver, by=locator[0],value=locator[1])