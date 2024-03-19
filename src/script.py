from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

problem_code = "4A"
code = problem_code[:-1]
letter = problem_code[-1]

user = "USERNAME"
pswd = "PASSWORD"

file_path = "C:/Users/yahya/OneDrive/Desktop/Codeforces-Submitter/test.py"
language = "PyPy 3.9.10 (7.3.9, 64bit)"

driver = webdriver.Chrome()
driver.get(f"https://codeforces.com/problemset/problem/{code}/{letter}")

enter_button = driver.find_element(By.XPATH, f"//a[@href='/enter?back=%2Fproblemset%2Fproblem%2F{code}%2F{letter}']")
enter_button.click()

username = driver.find_element(By.XPATH, "(//span[text()='×']/following::input)[5]")
username.send_keys(user)

password = driver.find_element(By.XPATH, "(//label[text()='Password']/following::input)[1]")
password.send_keys(pswd)

login_button = driver.find_element(By.XPATH, "//input[@value='Login']")
login_button.click()

sleep(5)

language_selector = Select(driver.find_element(By.NAME, "programTypeId"))
language_selector.select_by_visible_text(language)

choose_file = driver.find_element(By.XPATH, "//input[@type='file']")
choose_file.send_keys(file_path)

submit_solution = driver.find_element(By.XPATH, "(//input[@type='submit'])[3]")
submit_solution.click()

while True:
    pass
# options = Options()
# options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
# # options.binary_location = "C:\\Users\\yahya\\AppData\\Local\\Programs\\Opera\\opera.exe"

# options.add_argument("--user-data-dir=C:\\Users\\yahya\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data")

# PATH = "chromedriver_win32/chromedriver.exe"

# driver = webdriver.Chrome(options=options, executable_path=PATH)
# driver.get("https://codeforces.com/")
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