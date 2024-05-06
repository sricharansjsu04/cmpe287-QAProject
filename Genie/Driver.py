from appium import webdriver
from appium.options.android import UiAutomator2Options
from os import path

def get_driver(application):
    if application == 0:
        device_name = 'Nexus_S'
        app_package = 'co.appnation.geniechat'
        app_path = '/Users/geethikavadlamudi/Downloads/ai-chat-and-chatbot-genie-6-1-1.apk'
    elif application == 1:
        device_name = 'sdk_gphone64_x86_64'
        app_package = 'ai.chat.gpt.bot'
        app_path = '/Users/nguyenbui/Downloads/ChatOn.apk'

    desired_capabilities = {
        'platformName': 'Android',
        'deviceName': 'Nexus_S',
        'appPackage': 'co.appnation.geniechat',
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
