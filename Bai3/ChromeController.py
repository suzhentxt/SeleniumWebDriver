from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def open_chrome(name_profile=None):

    #Mở profile sẵn có
    chrome_options = Options()

    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")

    if name_profile != None:
        chrome_options.add_argument("user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument(f"--profile-directory={name_profile}")

    chrome_options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()

    url = "https://www.tiktok.com"
    driver.get(url)
