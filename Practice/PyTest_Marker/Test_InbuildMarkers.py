"""
skip will skip the testcase from the execution.
skipif will skip the testcase if condition is specified
xFail : if you already know that a particular testcase is going to fail.
        consider you raise a defect but that defect has not been fixed then u can you this marker.
"""
import pytest
import sys

def test_login():
    print("Login successful")

@pytest.mark.skip
def test_TC1():
    print("TC1 executed")

@pytest.mark.skipif(sys.version_info<(3,9), reason="Python version not supported")
def test_TC2():
    print("TC2 executed")

@pytest.mark.xfail()
def test_logout():
    print("Logout successful")