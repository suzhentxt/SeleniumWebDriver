from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import random
import requests

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
        
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:4444")
        self.driver = webdriver.Chrome(options=chrome_options)

        url = "https://account.alibabacloud.com/register/intl_register.htm?spm=a2c45.11132017.9219519220.2.278c79f4lf0P7d"
        self.driver.get(url)

    def get_temp_email(self):
        response = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1')
        return response.json()[0]

    def reg_web(self):

        try:
            # Chuyển vào iframe chứa nút "Next"
            self.driver.switch_to.frame(WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.TAG_NAME,"iframe"))))
            # iframe = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "alibaba-register-box")))
            # self.driver.switch_to.frame('alibaba-register-box')   

            # Tìm và click vào nút "Next" sau khi đã chuyển vào iframe
            next_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Next"]')))
            next_button.click()
            print("Clicked on the 'Next' button successfully.")
            
            # Chuyển lại về nội dung chính sau khi thao tác xong
            self.driver.switch_to.default_content()

        except Exception as e:
            print(f"Failed to click on the 'Next' button: {e}")
