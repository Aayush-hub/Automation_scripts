from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.get("https://github.com")
time.sleep(4)
login = chrome.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
login.click()
user = chrome.find_element_by_xpath('//*[@id="login_field"]')
inp = input("Enter username: ")
user.send_keys(inp)
passwrd = chrome.find_element_by_xpath('//*[@id="password"]')
passw = getpass()
passwrd.send_keys(passw)
submit = chrome.find_element_by_xpath('//*[@id="login"]/div[4]/form/input[14]')
submit.click()
