# imports
import selenium
import webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServices
from webdriver_manager.chrome import ChromeDriverManager

# wedriver steup
driver = webdriver.Chrome(service=ChromeServices(ChromeDriverManager().install()))
driver.get("https://phptravels.com/demo")
driver.maximize_window()
print(driver.title)
assert driver.title == "Book Your Free Demo Now - Phptravels"
driver.quit()
