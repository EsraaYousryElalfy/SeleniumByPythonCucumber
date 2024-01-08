from sympy import symbols, solve
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServices
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Starts driver before test
driver = webdriver.Chrome(service=ChromeServices(ChromeDriverManager().install()))
driver.get("https://phptravels.com/demo")
driver.maximize_window()
# Just an example we can add a wait: driver.implicitly_wait(1000)
print(driver.title)

# Starts the test
# 1- First name text-box
FirstNameTextBox: WebElement = driver.find_element(by=By.XPATH, value="//input[@placeholder='First Name']")
assert FirstNameTextBox.is_displayed()
FirstNameTextBox.send_keys("TestFirstNameTxtBox")
assert FirstNameTextBox.get_attribute("value") == "TestFirstNameTxtBox"
driver.implicitly_wait(2000)

# 2- Last name text-box
LastNameTextBox: WebElement = driver.find_element(by=By.XPATH, value="//input[@placeholder='Last Name']")
assert LastNameTextBox.is_displayed()
LastNameTextBox.send_keys("TestLastNameTxtBox")
assert LastNameTextBox.get_attribute("value") == "TestLastNameTxtBox"
driver.implicitly_wait(2000)

# 3- Business name text-box
BusinessNameTextBox: WebElement = driver.find_element(by=By.XPATH, value="//input[@placeholder='Business Name']")
assert BusinessNameTextBox.is_displayed()
BusinessNameTextBox.send_keys("TestBusinessNameTxtBox")
assert BusinessNameTextBox.get_attribute("value") == "TestBusinessNameTxtBox"
driver.implicitly_wait(2000)

# 4- Email text-box
EmailTextBox: WebElement = driver.find_element(by=By.XPATH, value="//input[@placeholder='Email']")
assert EmailTextBox.is_displayed()
EmailTextBox.send_keys("EmailTxtBox@test.com")
assert EmailTextBox.get_attribute("value") == "EmailTxtBox@test.com"
driver.implicitly_wait(2000)

# 5- solve the equation
EquationTxt: WebElement = driver.find_element(by=By.CSS_SELECTOR, value="div h4")
EquationTxtList = list(EquationTxt.text.replace(" ", "", 3))
x = symbols('EquationTxtList')
sol = solve(x)
firstValue = x[0]
secondValue = x[2]
sign = x[1]
print(firstValue)
print(secondValue)
print(sign)
value = ""
def switch(sign):
    if sign == "+":
        value =firstValue + secondValue
        print(value)
        return value

    if sign == "-":
        value = firstValue - secondValue
        print(value)
        return value
    else:
        raise Exception("Invalid sign")


# 6- Checks equation result
ResultTextBox: WebElement = driver.find_element(by=By.XPATH, value="//input[@placeholder='Result ?']")
ResultTextBox.send_keys(value)
assert ResultTextBox.get_attribute("value") == value

# 7- Clicks on Submit button
SubmitButton: WebElement = driver.find_element(by=By.XPATH, value="//button[text()='Submit']")
SubmitButton.click()

# 8- check that submit button worked successfully

# https://tutorialsninja.com/demo/

# after test
driver.quit()