from behave import *
from selenium import webdriver

@given('I navigated to login page')
def step_impl(context):
    print("Inside : I navigated to login page")


@when('I enter valid email \"([^\"]*)\" and valid password \"([^\"]*)\"')
def step_impl(context):
    print("Inside : I enter valid email and valid password")


@when('I enter invalid email \"([^\"]*)\" and valid password \"([^\"]*)\"')
def step_impl(context):
    print("Inside : I enter invalid email and valid password")


@when('I enter valid email \"([^\"]*)\" and invalid password \"([^\"]*)\"')
def step_impl(context):
    print("Inside : I enter valid email and invalid password")


@when('I enter invalid email \"([^\"]*)\" and invalid password \"([^\"]*)\"')
def step_impl(context):
    print("Inside : I enter invalid email and invalid password")


@when('I click on login button')
def step_impl(context):
    print("Inside : I click on login button")


@then('I should get login')
def step_impl(context):
    print("Inside : I should get login")


@then('I should get proper warning message \"([^\"]*)\"')
def step_impl(context):
    print("Inside : I should get proper warning message")
