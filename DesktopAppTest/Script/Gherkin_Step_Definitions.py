from HelperFunctions import (
    launch_edge_browser, navigate_to_url, click_On_Appearance_Option,
    click_On_Mode_Option, set_Light_Mode, set_Dark_Mode,
    is_Dark_Mode_Selected, is_Light_Mode_Selected,
    close_browser_window
)

@given("I launch the Edge browser application")
def step_impl():
    launch_edge_browser()

@when("I navigate to the {arg} URL")
def step_impl(url):
    navigate_to_url(url)

@when("I click on the Appearance option using OCR")
def step_impl():
    click_On_Appearance_Option()

@when("I click on the Mode option using OCR")
def step_impl():
    click_On_Mode_Option()

@when("I select the Light mode option")
def step_impl():
    set_Light_Mode()

@when("I select the Dark mode option")
def step_impl():
    set_Dark_Mode()

@then("Dark mode should be selected")
def step_impl():
    is_Dark_Mode_Selected()

@then("Light mode should be selected")
def step_impl():
    is_Light_Mode_Selected()

@then("I close the browser window")
def step_impl():
    close_browser_window()
