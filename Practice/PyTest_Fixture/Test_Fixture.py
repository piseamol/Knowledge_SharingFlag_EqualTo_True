"""
Fixture is used when your testcase needs a suite setup and suite teardown
Then you can use fixture concept.
e.g login and logout: no need to add same code in each testcase... in such cases use fixture concept.
"""
import pytest

@pytest.fixture
def setup():
    print("Login")
    yield
    print("Logout")

def test_TC1(setup):
    print("TC1 executed")

def test_TC2(setup):
    print("TC2 executed")

def test_TC3(setup):
    print("TC3 executed")