from behave import *

@given('I navigated to register page')
def step_impl(context):
    print("Inside : I navigated to register page")

@when('I click on continue button')
def step_impl(context):
    print("Inside : I click on continue button")

@when('I enter details into all fields except email field')
def step_impl(context):
    print("Inside : I enter details into all fields except email field")

@when('I enter details into all fields')
def step_impl(context):
    print("Inside : I enter details into all fields")

@when('I enter details into mandatory fields')
def step_impl(context):
    print("Inside : I enter details into mandatory fields")

@when('I do not enter anything into all field')
def step_impl(context):
    print("Inside : I do not enter anything into all field")

@then('Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    print("Inside : Proper warning message informing about duplicate account should be displayed")

@then('Proper warning message for every mandatory field should be displayed')
def step_impl(context):
    print("Inside : I navigated to register pageProper warning message for every mandatory field should be displayed")

@then('Account should get created')
def step_impl(context):
    print("Inside : Account should get created")