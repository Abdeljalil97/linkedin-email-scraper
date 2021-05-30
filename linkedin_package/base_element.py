from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from tld import get_tld

class BaseElement(object):
    def __init__(self,driver,value, by):
        self.driver = driver
        self.value = value
        self.by = by
        self.locator = (self.by,self.value)
        self.web_element = None
        self.find()

    def find(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_any_elements_located(locator=self.locator)
        )
        
        self.web_element=element
        return None
    def click(self):
        element = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable(locator=self.locator)
        )
        element.click()
        return None
    @property
    def text(self):
        for text in self.web_element : 
            text = text.text
            return text
    def inpt(self,text):
        element = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable(locator=self.locator)
        )
        element.send_keys(str(text))
        return None

    @property
    def contact_info_links(self):
        
        links = self.web_element
        urls = []
        for link in links :
            link=link.get_attribute("href")
            
            if link : 
                
                
                urls.append(link)

        return urls
    @property
    def fetch_emails(self):
        element = WebDriverWait(self.driver, 4).until(
            EC.presence_of_element_located(locator=self.locator)
        )
        email_regex = re.compile(r"[-.a-z]+@[^@\s\.]+\.[.a-z]{2,3}")
        html = self.driver.page_source
        body_emails = email_regex.findall(html)
        emails = [email for email in body_emails if \
            get_tld('https://' + email.split('@')[-1], fail_silently=True)]
        return emails
    @property
    def urls_account(self):
        #links = self.web_element.find_elements_by_tag_name('a')
        links = self.web_element

        urls = []
        for link in links :
            link=link.get_attribute("href")
            start='https://www.linkedin.com/in/'
            if link and (start in link)  :
                link = link.split('?')
                link = link[0]
                link = "{a}/detail/contact-info/".format(a=link)  
                urls.append(link)

        return urls