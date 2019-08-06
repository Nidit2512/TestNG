from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

path = "W:\\Registration BackOffice\\chromedriver_win32 (2)\\chromedriver.exe"
driver = webdriver.Chrome(executable_path= path)

driver.get('http://www.Facebook.com')
driver.maximize_window()

driver.find_element_by_xpath("//*[@id ='email']").send_keys("nidit_102@yahoo.com")
driver.find_element_by_xpath("//*[@id ='pass']").send_keys("1215@Nidit")
driver.find_element_by_xpath("//input[@value = 'Log In']").click()

driver.get('https://www.facebook.com/events/birthdays/')

feed = "Happy Birtday"

driver.find_element_by_xpath("//*[@class = 'enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']")




