import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
# options.binary_location = "C:\\Users\\yahya\\AppData\\Local\\Programs\\Opera\\opera.exe"

options.add_argument("--user-data-dir=C:\\Users\\yahya\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data")

PATH = "chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(options=options, executable_path=PATH)
driver.get("https://codeforces.com/")
# enterButton = driver.find_element(By.XPATH, "//a[@href='/enter?back=%2F']")

# enterButton.click()


# user = "Solidhelium"
# pswd = "Yahmurmuj1"
# code = "977A"
# language = "Python 3.8.10"
# filePath = "C:\\Users\\yahya\\Desktop\\Competitive Coding\\DIV 3\\Round 1 - 479\\A-wrongSubtraction.py"

# loginHandle = driver.find_element(By.NAME, "handleOrEmail")
# loginHandle.send_keys(user)

# password = driver.find_element(By.NAME, "password")
# password.send_keys(pswd)

# time.sleep(2)

# login = driver.find_element(By.CLASS_NAME, "submit")
# login.click()

# time.sleep(2)

# problemset = driver.find_element(By.XPATH, "//a[@href='/problemset']")
# problemset.click()


# submit = driver.find_element(By.XPATH, "//a[@href='/problemset/submit']")
# submit.click()

# problemCode = driver.find_element(By.NAME, "submittedProblemCode")
# problemCode.send_keys(code)


# lang = Select(driver.find_element(By.NAME, "programTypeId"))
# lang.select_by_visible_text(language)

# file = driver.find_element(By.NAME, "sourceFile")
# file.send_keys(filePath)

# time.sleep(2)

# submitFile = driver.find_element(By.CLASS_NAME, "submit")
# submitFile.click()