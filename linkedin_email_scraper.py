try:
    from selenium import webdriver
    from shutil import which
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.firefox.options import Options
except ModuleNotFoundError:
    print("Please download dependencies from requirement.txt")

firefox_options = Options()
firefox_options.add_argument('--headless')
firfox_path = which('geckodriver')
driver = webdriver.Firefox(executable_path=firfox_path)
driver.implicitly_wait(3)
driver.get("https://www.linkedin.com" )
driver.find_element_by_id('session_key').send_keys("abdeljalilbensoudane97@gmail.com")
driver.find_element_by_id('session_password').send_keys("Aurnowac9737")
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.get("https://www.linkedin.com/search/results/people/?keywords=maryland&origin=SWITCH_SEARCH_VERTICAL" )
