
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#To highlight a Web Element via Selenium with Python

driver = webdriver.Chrome('C:/Users/jacobiyl/Downloads/chromedriver_win77/chromedriver.exe')  # Optional argument, if not specified will search path.
actions = ActionChains(driver)

#Navigate to browser
driver.get('https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop/related?hl=en')
driver.maximize_window()
time.sleep(5)

#To find an element the web page and click on the element to Open in new tab
searchHyperlink = driver.find_element_by_xpath("(//a[@href='http://www.getpostman.com'])[1]")
clicked = 0
if(searchHyperlink.is_enabled()):
        searchHyperlink.click()
        print("Click :"+searchHyperlink.text+" Hyperlink")
        time.sleep(5)
        clicked =1
else:
        print('Could not Click :' + searchHyperlink.text + " Hyperlink")

#Switch between Tabs
if(clicked == 1):
    {
        print("Moved to new tab"):
        actions.send_keys(Keys.CONTROL + Keys.TAB)
    }
time.sleep(5)

driver.quit()
