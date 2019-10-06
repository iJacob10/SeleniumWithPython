
from selenium import webdriver
import time

#To highlight a Web Element via Selenium with Python
# Reference : https://www.youtube.com/watch?v=3ud7TIqpA_0

driver = webdriver.Chrome('C:/Users/jacobiyl/Downloads/chromedriver_win77/chromedriver.exe')  # Optional argument, if not specified will search path.

#Navigate to browser
driver.get('https://docs.microsoft.com/en-us/visualstudio/data-tools/walkthrough-creating-a-simple-wcf-service-in-windows-forms?view=vs-2017')
driver.maximize_window()
time.sleep(5)

#To find an element the web page by scrolling page down
searchButton = driver.find_element_by_xpath("//button[@class='button feedback-sign-in-button has-text-wrap']")
driver.execute_script("arguments[0].scrollIntoView(true)",searchButton)
print("Scrolled to page '",searchButton.text,"' button")
time.sleep(5)

#To highlight a Web Element
driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",searchButton, "background:yellow; color: Red; border:4px dotted solid yellow;")
print("Highlighted '",searchButton.text,"'.")

#Click on the Web Element button
searchButton.click()

print("Navigated to new page :", driver.current_url)
time.sleep(5) # Let the user actually see something!
driver.quit()

''' OUTPUT:
Scrolled to page  'This page' button
Highlighted ' This page '.
Navigated to new page : https://github.com/login?client_id=Iv1.d31913c6812a3ef4&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3DIv1.d31913c6812a3ef4%26redirect_uri%3Dhttps%253A%252F%252Fdocs.microsoft.com%252Fapi%252Fgithubauth%252Fauthorized%26state%3D1ad4b8f4031bf72ada8039c8d52bcb88425457d4237b868bbd46dae7677769adeb07b65ee8a5c5c53ba41142ed80f47f2343e7dd9f03c93f1e513eeda1cfe0fae7334cbe700e0f8a9797a96a51cc267c6bc3322128ef41868640f731f9d63b93a1d7daa5cac9032ea26167f124e778ce3c98337036ba3e3fe6024f31cc17333b1176f4ea279236ffbc6d0b65abad8364a347b80bf282a0267e42e7ac3dc4576a3b37baced14c9a084e92999c8c2545b43e1a5afc0ec3c0a7e0767b3aef2732ac27af1cd80370e161a73e5bdaf552ab7a3957c8db865962a9206fbfee92bfcc5766472980b017fc
'''