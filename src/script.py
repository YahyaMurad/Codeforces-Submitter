from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def submission(problem_code, user, pswd, file_path, language):
    code = problem_code[:-1]
    letter = problem_code[-1]

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