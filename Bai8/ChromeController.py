from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import random

class RegTikTokController():

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

        url = "https://www.tiktok.com/signup/phone-or-email/email"
        self.driver.get(url)

    def reg_tiktok(self):
        
        # Nhập ngày tháng năm sinh
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Month. Double-tap for more options']"))).click()
        month = random.choice(range(12))
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.ID, f"Month-options-item-{month}"))).click()

        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Day. Double-tap for more options']"))).click()
        day = random.choice(range(28))
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.ID, f"Day-options-item-{day}"))).click()

        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Year. Double-tap for more options']"))).click()
        year = random.choice(range(1990,2000))
        id_year = 2022 - year
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.ID, f"Year-options-item-{id_year}"))).click()

        # Nhập mail
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='email']"))).send_keys("trinhcnt@gmail.com")
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='new-password']"))).send_keys("@trinh12323")

    def watch_video(self, number_video):
        self.driver.get("https://www.tiktok.com/foryou")
        
        likes = WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_all_elements_located((By.XPATH, "//span@[data-e2e='like-icon']")))

        for video in number_video:
            time.sleep(random.choice(range(10,50)))