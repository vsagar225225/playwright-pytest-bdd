# step_defs/test_example.py
import pytest
from pytest_bdd import scenarios, given, then
from pages.home_page import HomePage

# Link feature file to step definitions
scenarios('../features/example.feature')

# Step Definitions
@pytest.fixture
def homepage(page):
    return HomePage(page)

@given("the user opens the homepage")
def open_homepage(homepage):
    homepage.navigate()

@then('the page title should be "Example Domain"')
def check_title(homepage):
    assert homepage.get_title() == "Example Domain"
