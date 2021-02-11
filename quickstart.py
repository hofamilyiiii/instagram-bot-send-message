# imports
from instapy import InstaPy
from instapy import smart_run
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import random

# login credentials
insta_username = ''
insta_password = ''
# message string to send
message = ""

url = 'https://instagram.com/'

send_to_list = []
exclude_users = []

session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)

def url_name(url): 
        chrome.get(url)

        # adjust sleep if you want
        time.sleep(5.5) 

def login(username, your_password):
        # finds the username box 
        username_element = chrome.find_element_by_name("username")

        # sends the entered username 
        username_element.send_keys(insta_username)

        # finds the password box 
        password_element = chrome.find_element_by_name("password")

        # sends the entered password 
        password_element.send_keys(insta_password)

        # press enter after sending password
        password_element.send_keys(Keys.RETURN) 
        time.sleep(5.5)

def goto_message_page():
        # Find message button
        message_element = chrome.find_element_by_class_name('_862NM ') 
        message_element.click()
        time.sleep(5.5)

def click_not_now():
        not_now_element = chrome.find_element_by_class_name('HoLwm ')
        not_now_element.click()
        time.sleep(1)

def send_message():
        mbox = chrome.find_element_by_tag_name('textarea')
        mbox.send_keys(message)
        mbox.send_keys(Keys.RETURN)
        time.sleep(1.2)

with smart_run(session):
        """ Activity flow """
        # general settings
        send_to_list = session.pick_mutual_following(username=insta_username, live_match=False, store_locally=True)
        send_to_list = [x for x in send_to_list if x not in exclude_users]

chrome = webdriver.Chrome() # Optional argument, if not specified will search path.
time.sleep(1)
url_name(url)
login(insta_username, insta_password)
isFirst = True
for x in send_to_list:
        url_name(url + x)
        goto_message_page()
        if (isFirst): 
                click_not_now()
                isFirst = False
        send_message()        
chrome.close()