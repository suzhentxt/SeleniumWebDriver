from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import random

class RegWebController():

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
        
        # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:4444")
        self.driver = webdriver.Chrome(options=chrome_options)

        url = "https://account.alibabacloud.com/register/intl_register.htm?spm=a2c45.11132017.9219519220.2.278c79f4lf0P7d"
        self.driver.get(url)

    def reg_web(self):
        
        # Chọn next
        WebDriverWait(driver=self.driver, timeout=30).until(EC.visibility_of_element_located((By.CLASS_NAME, "entity__btn-next"))).click()
        
