from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random

class RegYoutubeController():

    def __init__(self) -> None:
        pass    

    def open_chrome(self, name_profile=None):

       # Mở profile sẵn có
        chrome_options = Options()

        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")

        if name_profile != None:
            chrome_options.add_argument("user-data-dir=C:/Users/Admin/AppData/Local/Google/Chrome/User Data")
            chrome_options.add_argument(f"--profile-directory={name_profile}")

        chrome_options.add_experimental_option("detach", True)
        
        driver = webdriver.Chrome(options=chrome_options)

        driver.maximize_window()

        url = "https://account.alibabacloud.com/register/intl_register.htm?spm=a2c45.11132017.9219519220.2.278c79f4lf0P7d"
        driver.get(url)

    