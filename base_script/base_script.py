from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from os import path
import time

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': 'Nexus_S',
    'appPackage': 'ai.chat.gpt.bot',
    'appActivity': 'com.aiby.chat.MainActivity',  # Assuming this is the main activity
    'automationName': 'UiAutomator2',  # Use UiAutomator2 for better compatibility,
    'newCommandTimeout': 3600,
    'connectHardwareKeyboard': True,
    'app': path.abspath('/Users/geethikavadlamudi/Downloads/ChatOn - AI Chat Bot Assistant_1.39.374-396_apkcombo.com.apk')
}

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# options = AppiumOptions()
# options.load_capabilities({
# 	"appium:platformName": "Android",
# 	"appium:deviceName": "Nexus_S",
# 	"appium:appPackage": "ai.chat.gpt.bot",
# 	"appium:appActivity": "com.aiby.chat.MainActivity",
# 	"appium:automationName": "UiAutomator2",
# 	"appium:newCommandTimeout": 3600,
#     "app": path.abspath('/Users/geethikavadlamudi/Downloads/ChatOn - AI Chat Bot Assistant_1.39.374-396_apkcombo.com.apk')
# 	"appium:connectHardwareKeyboard": True
# })

# driver = webdriver.Remote("http://127.0.0.1:4723", options=options)


driver = webdriver.Remote('http://localhost:4723', options=UiAutomator2Options().load_capabilities(desired_capabilities))

# Start the app and go to the gallery
# Update these XPaths and IDs based on the actual UI elements in your app
# el6 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.LinearLayout[@content-desc='Gallery']/android.widget.ImageView")
# el6.click()
driver.swipe(512, 1144, 541, 504, 800)  # Adjust the coordinates based on the actual screen size
time.sleep(5)
el1 = driver.find_element(by=AppiumBy.ID, value="ai.chat.gpt.bot:id/continueButton")
el1.click()
el1.click()
el1.click()
el1.click()
el2 = driver.find_element(by=AppiumBy.ID, value="ai.chat.gpt.bot:id/close")
el2.click()
el3 = driver.find_element(by=AppiumBy.ID, value="ai.chat.gpt.bot:id/inputEditText")
el3.send_keys("most popular transportation in coastal places of big countries in Asia like mumbai in india")
el4 = driver.find_element(by=AppiumBy.ID, value="ai.chat.gpt.bot:id/sendButton")
el4.click()
el5 = driver.find_element(by=AppiumBy.ID, value="ai.chat.gpt.bot:id/sendButton")
el5.click()
# Get the result
el6 = driver.find_element(by=AppiumBy.ID, value="ai.chat.gpt.bot:id/message_text_view")
print("\n\n\n\n\n\n\n......*********    ",el6,"    ********...........\n\n\n\n\n\n\n\n\n")
el6.click()
driver.quit()
# els4 = driver.find_elements(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='ai.chat.gpt.bot:id/message_text_view']")
