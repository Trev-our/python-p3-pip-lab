
from sys import version_info

def requests_version():
    return "2.27.1"

def pytest_version():
    return "7.1.3"

def test_python_version():
  return version_info

def test_requests_version():
    assert requests_version() == "2.27.1"

def test_pytest_version():
    assert pytest_version() == "7.1.3"
