# USAGE
# python3 twitch.py 

# import openvpn_api.VPN
# v = openvpn_api.VPN('139.28.218.75 443', 443)

import pyautogui 
pyautogui.FAILSAFE = False

import sys
import os
from multiprocessing import Pool
import datetime
import urllib
import math
import random
import string
import time
import pickle
import pyperclip as pc
import requests
import json
from PIL import Image 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print(sys.argv)
argv_len = len(sys.argv)

location_url = 'http://ipinfo.io/json'
response = urllib.request.urlopen(location_url)
location_data = json.load(response)

IP=location_data['ip']
org=location_data['org']
city = location_data['city']
country=location_data['country']
region=location_data['region']

print('Your IP detail\n ')
print('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))

cwd = os.getcwd()
tw_login_dir = cwd + "/tw_logins"
if os.path.isdir(tw_login_dir):
    pass
else: 
    os.makedirs(tw_login_dir)

captcha_training_dir = cwd + "/captcha_train"
if os.path.isdir(captcha_training_dir):
    pass
else: 
    os.makedirs(captcha_training_dir)

def remove_whitespace(string): 
    string = string.replace(" ", "-")
    string = string.replace("/", "")
    string = string.replace(".", "")
    return string.replace(":", "-")

def get_random_string(min_length, max_length):
    random_characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(random_characters) for i in range(random.randint(min_length, max_length)))
    return random_string

def get_email_message(max_length):
    message = """\
    Subject: Greetings pokimane fraud + other crimes facilitators ....

    #kidslivesmatter #simplivesmatter ..... """ + get_random_string(1, max_length)
    return message

def send_mail():
    import smtplib
    import ssl
    from getpass import getpass
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = sys.argv[4]  # Enter your address
    receiver_email = "jeff.bezos@amazon.com", "support@twitch.tv", "security@twitch.tv", "legal@twitch.tv", "emmett@twitch.tv", "feedback@twitch.tv", "partnerhelp@twitch.tv", "press@twitch.tv", "developer_support@twitch.tv", "hana.tija@unitedtalent.com", "partnersupport@twitch.tv", "devpayments@twitch.tv"  # Enter receiver address
    password = getpass()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        for i in range(1, random.randint(2, 10)):
            new_message = get_email_message(200)
            server.sendmail(sender_email, receiver_email, new_message)
            time.sleep(1)
            print("I've sent", i, "number of emails already!")

months = ['January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December']

def get_user_name():
    user_name_characters = string.ascii_letters + string.digits
    user_name = ''.join(random.choice(user_name_characters) for i in range(random.randint(12, 16)))
    return user_name

def get_user_password():
    user_password_characters = string.ascii_letters + string.digits + string.punctuation
    user_password = ''.join(random.choice(user_password_characters) for i in range(random.randint(16, 20)))
    return user_password

webdriver.Chrome(executable_path='bin/chromedriver')

#PROXY = "proxy.torguard.io:1090" # IP:PORT or HOST:PORT
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--user-data-dir=" + cwd + "/Default/")
# chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_extension(cwd + "/Extensions/ublock_1.29.2_0.crx")
# chrome_options.add_extension(cwd + "/Extensions/selenium_3.17.0.0.crx")
# ADD PROXY SETTINGS TO MAKE VIEWBOTS
#chrome_options.add_argument('--proxy-server=%s' % PROXY)
# chrome_options.add_argument("--headless");


def twitch_browser():
    with webdriver.Chrome(options=chrome_options) as driver:
        # actions = ActionChains(driver)
        driver.set_window_size(1600,900)
        driver.set_window_position(50, 50)

        def make_account():
            driver.get("https://twitch.tv")
            twitch_main = driver.current_window_handle
            time.sleep(0.25)

            # GET TEMP MAIL (look into using a server)
            driver.execute_script("window.open();")
            driver.switch_to_window(driver.window_handles[1])
            driver.get("https://temp-mail.org/en/")
            temp_mail = driver.current_window_handle
            time.sleep(3)
            driver.find_element_by_css_selector('.btn-rds:nth-child(1) > svg').click()
            email = pc.paste() 
            print(email)
            time.sleep(0.25)
            
            # BACK TO TWITCH TO MAKE ACCT
            driver.switch_to.window(twitch_main)
            time.sleep(0.25)
            driver.find_element_by_css_selector('.tw-core-button--primary:nth-child(1) > .tw-align-items-center > .tw-flex-grow-0').click()
            time.sleep(0.25)
            name = get_user_name()
            driver.find_element_by_xpath("//input[@id='signup-username']").send_keys(name)
            password = get_user_password()
            driver.find_element_by_xpath("//input[@id='password-input']").send_keys(password)
            driver.find_element_by_xpath("//input[@id='password-input-confirmation']").send_keys(password)
            driver.find_element_by_css_selector('.tw-pd-r-3').click()
            birth_month = random.choice(months)
            Select(driver.find_element_by_css_selector('.tw-pd-r-3')).select_by_visible_text(birth_month)
            birth_day = random.randint(1, 28)
            driver.find_element_by_xpath("//div[2]/div[2]/div/input").send_keys(birth_day)
            birth_year = random.randint(1968, 1990)
            driver.find_element_by_xpath("//div[3]/div/input").send_keys(birth_year)
            user_email = email
            driver.find_element_by_xpath("//div[4]/div/div[2]/input").send_keys(user_email)
            time.sleep(2)
            driver.find_element_by_css_selector('.tw-mg-t-2 > .tw-align-items-center').click()
            time.sleep(6)
            pyautogui.click(x=845, y=635)
            time.sleep(1.5)
            current_utc = datetime.datetime.utcnow()
            utc_str = str(current_utc)
            utc_str_nws = remove_whitespace(utc_str)
            driver.save_screenshot("captcha_train/captcha_" + utc_str_nws + ".png")
            def get_captcha_screenshot():
                time.sleep(1.5)
                pyautogui.click(x=750, y=575)
                time.sleep(0.25)
                pyautogui.click(x=845, y=640)
                time.sleep(1.5)
                current_utc = datetime.datetime.utcnow()
                utc_str = str(current_utc)
                utc_str_nws = remove_whitespace(utc_str)
                driver.save_screenshot("captcha_train/captcha_" + utc_str_nws + ".png")

            get_captcha_screenshot()
            get_captcha_screenshot()
            get_captcha_screenshot()
            get_captcha_screenshot()
            get_captcha_screenshot()

            # JUST GETTING CAPTCHA TRAINING DATA SO QUITTING DRIVER
            quit()


            #CAPTCHA INCOMPLETE
            time.sleep(60) # MANUAL captcha 

            # VERIFY EMAIL
            time.sleep(2)
            driver.switch_to.window(temp_mail)
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 250)") 
            time.sleep(1)
            driver.find_element_by_css_selector('li:nth-child(2) > .col-box:nth-child(1)').click()
            time.sleep(3)
            driver.find_element_by_css_selector('li:nth-child(2) .inboxSubject > .viewLink').click()
            driver.execute_script("window.scrollTo(0, 700)") 
            time.sleep(3)
            driver.find_element_by_css_selector('td > a').click()
            time.sleep(2)

            def save_user_login():
                login_dict = {
                    "user_name": name,
                    "user_password": password,
                    "user_birth_month": birth_month,
                    "user_birth_day": birth_day,
                    "user_birth_year": birth_year,
                    "user_email": user_email
                }
                pickle.dump( login_dict, open("tw_logins/" + name + ".login", "wb" ))
                time.sleep(1)

            save_user_login()

            # BACK TO TWITCH
            time.sleep(0.5)
            driver.switch_to.window(original_window)
            time.sleep(2)
            driver.refresh()
            time.sleep(0.5)

        def follow_streamer(streamer, tab_number):
            url = "https://twitch.tv/" + streamer
            driver.switch_to_window(driver.window_handles[tab_number])
            driver.get(url)
            time.sleep(3)
            driver.find_element_by_css_selector('.tw-font-size-4:nth-child(2)').click()
            time.sleep(3)
            driver.find_element_by_css_selector('.follow-btn__follow-btn > .tw-border-radius-medium > .tw-align-items-center > .tw-align-items-center').click()
            time.sleep(3)
            driver.find_element_by_css_selector('.chat-input').click()
            time.sleep(0.5)
            driver.find_element_by_css_selector('.tw-core-button--large:nth-child(1)').click()
            time.sleep(0.5)
            time.sleep(600)
            for i in range(random.randint(5, 100)):
                driver.find_element_by_css_selector('.chat-input').click()
                time.sleep(0.5)
                random_chat = get_random_string(5, 20)
                driver.find_element_by_css_selector('.chat-input').type(random_chat)
                time.sleep(0.5)
                driver.find_element_by_css_selector('.chat-input').send_keys(Keys.RETURN)
                time.sleep(2)

        make_account()
        time.sleep(5)
        
        time.sleep(60000)
        driver.quit()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        send_mail()
        twitch_browser()
    else:
        twitch_browser()

# THIS IS INCOMPLETE
# You can easily change any part of this to be more flexible or to another service

# Currently it just makes an account with tempmail, you need to do the captcha manually, and it verifies the email for you,
# then saves the login info for future use

# Currently this script uses tempmail as default email if you don't specify a server (TOIMPLEMENT)
# I'll add user controls for whom to watch or whom to spam
# Manual kubernetes chat mode
# AI mode where it just lives in the cloud or from wherever you launch it
# STREAMER mode
# Site-crossover modes
# LONG-TERM twitch user becomes human or robot modes

# FOR CAPTCHA
# use machine learning (manual tf.nn.conv2d or equivalent, tag feet/legs then autoencode, 
# autofeature extract then choose feet, or find correct rotation first then use autoencoder to
# train number of rotation neural net from training examples which would find the parallel feet
# huristic without announcing to you) to find coordinates of feet then make them parallel
# to top and bottom of the circle when spun to the lower half; there should be 2 parallel
# points, one in the upper half of circle when spun and one in the lower

# This is mere skeleton code; you want to use selenium-only for mouse and keyboard actions
# so you can run this containerized in headless while spoofing head mode and add appropriate
# proxy, VPN, or header spoofing to a production-level app

# Additionally you want an email server rather than doing it manually, train a neural net 
# (I tried and failed to manually write 2 convolutional filters) to solve captcha, and use
# burner services (see the Burner app on Android Studio emulator for example) to get past auth

# Think about chaining together websites in this form of automation

# The other form anti-pokimane application to find zero days

# CYCLE this with settings file or command line interface