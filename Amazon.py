from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select
import urllib3
from selenium.common import exceptions
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def Link_Page():
    global driver
    path = "W:\\Registration BackOffice\\chromedriver_win32 (2)\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get('http://www.amazon.com/')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.close()
    act = ActionChains(driver)

def Login_Page():
    act.move_to_element(driver.find_element_by_id("nav-link-accountList")).perform()
    driver.find_element_by_xpath("//span[contains(@class,'nav-action-inner')]").click()
    driver.find_element_by_id("ap_email").send_keys("niditshah@yahoo.com")
    driver.find_element_by_xpath("//input[@type = 'password']").send_keys("1215@Nidit")
    driver.find_element_by_id("signInSubmit").click()
# act.move_to_element(driver.find_element_by_css_selector("#nav-xshop > a:nth-child(4)")).click()
# driver.find_element_by_css_selector("#nav-xshop > a:nth-child(4)").click()
# driver.find_element_by_xpath("//span[contains(@class,'a-button-text a-declarative')]").click()
# myselect = Select(driver.find_element_by_class_name("a-dropdown-link")).select_by_index("0")


def Scrap_
user_agent = UserAgent()

main_url = 'https://www.amazon.com/?ref_=nav_ya_signin&'
page = requests.get(main_url,headers = {'user-agent': user_agent.chrome})
soup = BeautifulSoup(page.content,'lxml')

base_url = 'http://www.amazon.com'

all_divs = soup.find_all('div',class_='nav-a')

for div in all_divs:
    print(base_url + div.a['href'])



