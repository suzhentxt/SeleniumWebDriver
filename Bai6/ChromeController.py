from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def open_chrome(name_profile=None):

    #Mở profile sẵn có
    chrome_options = Options()

    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")

    if name_profile != None:
        chrome_options.add_argument("user-data-dir=C:/Users/Admin/AppData/Local/Google/Chrome/User Data")
        chrome_options.add_argument(f"--profile-directory={name_profile}")

    # chrome_options.add_experimental_option("detach", True)
    
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:4444")
    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    url = "https://www.tiktok.com/signup/phone-or-email/email"
    driver.get(url)

    # time.sleep(3)

    # elm = driver.find_element(by=By.XPATH, value="//input[@autocomplete='email']")
    # elm.click()

    elm = WebDriverWait(driver=driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='email']")))
    elm.send_keys("hello")