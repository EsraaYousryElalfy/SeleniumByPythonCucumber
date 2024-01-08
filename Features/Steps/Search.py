from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServices
from webdriver_manager.chrome import ChromeDriverManager

@given('I got navigated to home page')
def step_impl(context):
    print("Inside : I navigated to home page")
    driver = webdriver.Chrome(service=ChromeServices(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    print(driver.title)
    assert driver.title == ""



@when('I enter valid product \"([^\"]*)\" into search field')
def step_impl(context):
    print("Inside : I enter valid product")


@when('I enter invalid product \"([^\"]*)\" into search field')
def step_impl(context):
    print("Inside : I enter invalid product")

@when('I do not enter anything into search box field')
def step_impl(context):
    print("Inside : I do not enter anything into search box field")

@when('I click on search button')
def step_impl(context):
    print("Inside : I click on search button")


@then('Valid products should get displayed in search results')
def step_impl(context):
    print("Inside : I should get valid products displayed in search results")


@then('Proper message \"([^\"]*)\" should get displayed in search results')
def step_impl(context):
    print("Inside : I should get proper message displayed in search results as ")