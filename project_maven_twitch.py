# USAGE
# python3 project_maven_twitch.py 

# import openvpn_api.VPN
# v = openvpn_api.VPN('139.28.218.75 443', 443)

# import pyautogui 
# pyautogui.FAILSAFE = False

import sys
import os
import random
import string
import time
import datetime
import pickle
import pyperclip as pc
from multiprocessing import Pool
from PIL import Image 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

cwd = os.getcwd()
screenshot_dir = cwd + "/criminal_screenshots"
# tw_login_dir = cwd + "/tw_logins"
if os.path.isdir(screenshot_dir):
    pass
else: 
    os.makedirs(screenshot_dir)

# pickle this with IO for easiest database-equivalent
criminal_suspects = {
  'https://twitch.tv/' : ['pokimanelol'],
  'https://twitter.com/' : ['pokimanelol'],
  'https://facebook.com/' : ['pokimane'],
  'https://www.reddit.com/r/' : ['pokimane'],
  'https://www.pornhub.com/video/search?search=' : ['pokimane'],
  'https://www.linkedin.com/in/' : [ None ]
}

def remove_whitespace(string): 
    string = string.replace(" ", "-")
    string = string.replace("/", "")
    string = string.replace(".", "")
    return string.replace(":", "-")

# USE socks5 to mask all types of traffic
# PROXY = "23.23.23.23:3128" # IP:PORT or HOST:PORT
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# chrome_options.add_extension(cwd + "/Extensions/ublock_1.29.2_0.crx")
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_argument("--headless")

def screenshot_criminal_suspects():
    with webdriver.Chrome(options=chrome_options) as driver:
        # actions = ActionChains(driver)
        driver.set_window_size(1920,8640) #4320 #2160
        for key in criminal_suspects:
            for val in criminal_suspects[key]: 
                if val != None:
                    url = key + val
                else:
                    pass
                print(url)
                driver.get(url)
                time.sleep(3)
                current_utc = datetime.datetime.utcnow()
                utc_str = str(current_utc)
                utc_str_nws = remove_whitespace(utc_str)
                url_nws = remove_whitespace(url)
                print(utc_str_nws)
                driver.save_screenshot( "criminal_screenshots/" + url_nws + utc_str_nws + ".png")

if __name__ == '__main__':
    screenshot_criminal_suspects()