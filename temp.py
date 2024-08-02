#main.py
from ChromeController import RegTikTokController


auto = RegTikTokController()

auto.open_chrome()

auto.watch_video(number_video=5)


#ChromeController.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
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
            chrome_options.add_argument("user-data-dir=C:\\Users\\ADMIN\\AppData\\Local\\Google\\Chrome\\User Data")
            chrome_options.add_argument(f"--profile-directory={name_profile}")
        # chrome_options.add_experimental_option("detach", True)
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # chrome_options.add_argument()

        self.driver = webdriver.Chrome(options=chrome_options)
        
    
    def reg_tiktok(self):
        
        self.driver.get("https://www.tiktok.com/signup/phone-or-email/email")
        
        # Nhập ngày tháng sinh
        
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH,"//div[@aria-label='Tháng. Nhấn đúp để xem tùy chọn khác']"))).click()
        
        month = random.choice(range(12))
        
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.ID,f"Month-options-item-{month}"))).click()
        
        
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH,"//div[@aria-label='Ngày. Nhấn đúp để xem tùy chọn khác']"))).click()
        
        day = random.choice(range(28))
        
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.ID,f"Day-options-item-{day}"))).click()
        
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH,"//div[@aria-label='Năm. Nhấn đúp để xem tùy chọn khác']"))).click()
        
        year = random.choice(range(1990,2000))
        
        id_year = 2022 - year
        
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.ID,f"Year-options-item-{id_year}"))).click()
        
        # Nhập mail
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='email']"))).send_keys("longnv@hiworld.com.vn")
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='new-password']"))).send_keys("@long123321")
    
    
    def watch_video(self, number_video):
        self.driver.get("https://www.tiktok.com/foryou")
        
        likes =  WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_all_elements_located((By.XPATH,"//span[@data-e2e='like-icon']")))
        
        print("Số nút like tìm được: ", len(likes))
        
        pos = 0
        
        for i in range(number_video):
            
            # vòng lặp thứ 1: pos = 0
            # vòng lặp thứ 2: pos = 600
            # vòng lặp thứ 2: pos = 1200
            # ActionChains(driver=self.driver).move_to_element(likes[i])
            
            time.sleep(random.choice(range(2,5)))
            
            if random.choices(["like", "không like"]) == "like":
                
                print("randome vào like")
            
                likes[i].click()
                time.sleep(1)
            
            self.driver.execute_script(f"window.scrollTo({pos}, {pos + 600})")
            
            pos = pos + 600
            
            