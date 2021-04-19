from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(executable_path='C:/Users/NButala/Downloads/chromedriver_win32/chromedriver.exe')
    return driver

def pytest_configure(config):
    config._metadata['Project Name']='nop Commerce'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='Nachiket'
