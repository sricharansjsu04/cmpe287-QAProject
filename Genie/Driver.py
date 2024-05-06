from appium import webdriver
from appium.options.android import UiAutomator2Options
from os import path

def get_driver(app_package: str, app_path: str):

    desired_capabilities = {
        'platformName': 'Android',
        'deviceName': 'Nexus_S',
        'appPackage': app_package,
        'automationName': 'UiAutomator2',
        'newCommandTimeout': 3600,
        'ensureWebviewsHavePages': True,
        'connectHardwareKeyboard': True,
        'app': path.abspath(app_path)
    }
    driver = webdriver.Remote('http://localhost:4723', options=UiAutomator2Options().load_capabilities(desired_capabilities))
    return driver

def close_driver(driver : webdriver.webdriver.WebDriver):
    driver.quit()
