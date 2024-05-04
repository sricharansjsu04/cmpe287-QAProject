from appium import webdriver
from appium.options.android import UiAutomator2Options
from os import path

def get_driver():
    desired_capabilities = {
        'platformName': 'Android',
        'deviceName': 'Nexus_S',
        'appPackage': 'co.appnation.geniechat',
        'automationName': 'UiAutomator2',
        'newCommandTimeout': 3600,
        'ensureWebviewsHavePages': True,
        'connectHardwareKeyboard': True,
        'app': path.abspath('/Users/geethikavadlamudi/Downloads/ai-chat-and-chatbot-genie-6-1-1.apk')
    }
    driver = webdriver.Remote('http://localhost:4723', options=UiAutomator2Options().load_capabilities(desired_capabilities))
    return driver

def close_driver(driver):
    driver.quit()
