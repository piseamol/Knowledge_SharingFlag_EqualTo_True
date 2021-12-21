"""
Created Custom marker
To run Smoke Test suite use this command: pytest Test_Marker.py -m Smoke
To run Regression Test suite use this command: pytest Test_Marker.py -m Regression
To run Smoke or Regression Test suite use this command: pytest Test_Marker.py -m "Smoke or Regression"
To run Smoke And Regression Test suite use this command: pytest Test_Marker.py -m "Smoke and Regression"
"""
import pytest

@pytest.mark.Smoke
def test_login():
    print("Login successful")

@pytest.mark.Smoke
def test_TC1():
    print("TC1 executed")

@pytest.mark.Regression
def test_TC2():
    print("TC2 executed")

@pytest.mark.Regression
def test_TC3():
    print("TC3 executed")

@pytest.mark.Regression
def test_TC4():
    print("TC4 executed")

@pytest.mark.Smoke
def test_logout():
    print("Logout successful")