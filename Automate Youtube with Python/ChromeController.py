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

        # chrome_options.add_experimental_option("detach", True)
        
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:4444")
        self.driver = webdriver.Chrome(options=chrome_options)

        url = "https://www.youtube.com/"
        self.driver.get(url)

    def watch_video(self, searchtext):
        # WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='off']"))).click()
    
        search_box = WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='off']")))
        search_box.send_keys(searchtext)
    
        search_button = WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.ID, "search-icon-legacy")))
        search_button.click()

        first_video = WebDriverWait(driver=self.driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH, "//ytd-video-renderer[1]//a[@id='video-title']")))
        first_video.click()