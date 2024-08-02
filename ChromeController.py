from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

def open_chrome(name_profile=None):

    #Mở profile sẵn có
    chrome_options = Options()
    # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")

    if name_profile != None:
        chrome_options.add_argument("user-data-dir = C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument(f"--profile-directory = {name_profile}")
    # chrome_options.add_argument("user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data")
    # chrome_options.add_argument(f"--profile-directory=Profile 1")

    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options = chrome_options)
    # service = Service(executable_path='D:\\Xius\\Dev\\Tool\\SeriesAutoChrome\\chromedriver.exe')
    # options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    driver.get("https://www.tiktok.com/")
