class BasePage(object):
    #url =  "https://www.linkedin.com/in/scott-anthony-gould-7a248651/detail/contact-info/"

    def __init__(self,driver,url) :
        self.driver = driver
        self.url = url
        
    def go(self):
        
        self.driver.get(self.url)