import os
from selenium import webdriver
from shutil import which
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from linkedin_package.linkedin_email_scraper import LoginLinkedin
from linkedin_package.contact_info_linkedin import ContactInfo
from linkedin_package.links_account import LinksAccount


firefox_options = Options()
firefox_options.add_argument('--headless')
firfox_path = which('geckodriver')
driver = webdriver.Firefox(executable_path=firfox_path)
email = "abdeljalilbensoudane97@gmail.com"
passwrod = "Aurnowac9737"
linkedine_scraper=LoginLinkedin(driver=driver,url = "https://www.linkedin.com")
linkedine_scraper.go()
linkedine_scraper.input_email.inpt(text=email )
linkedine_scraper.input_password.inpt(text=passwrod )
#assert linkedine_scraper.sign_in.text == "Sign in"
linkedine_scraper.sign_in.click()
for i in range(1,12) :
    url = 'https://www.linkedin.com/search/results/people/?keywords=maryland&origin=SWITCH_SEARCH_VERTICAL&page={i}'.format(i=i)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.get(url)

driver.quit()