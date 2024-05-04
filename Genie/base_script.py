from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from os import path
import time

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': 'Nexus_S',
    'appPackage': 'co.appnation.geniechat',
    # 'appActivity': 'com.aiby.chat.MainActivity',  # Assuming this is the main activity
    'automationName': 'UiAutomator2',  # Use UiAutomator2 for better compatibility,
    'newCommandTimeout': 3600,
    'ensureWebviewsHavePages': True,
    'connectHardwareKeyboard': True,
    'app': path.abspath('/Users/geethikavadlamudi/Downloads/ai-chat-and-chatbot-genie-6-1-1.apk')
}


driver = webdriver.Remote('http://localhost:4723', options=UiAutomator2Options().load_capabilities(desired_capabilities))

# Start the app and go to the gallery
# Update these XPaths and IDs based on the actual UI elements in your app
# el6 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.LinearLayout[@content-desc='Gallery']/android.widget.ImageView")
# el6.click()
driver.swipe(512, 1144, 541, 504, 800)  # Adjust the coordinates based on the actual screen size
time.sleep(2)

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue")
el1.click()
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue")
el2.click()
time.sleep(1)
el3 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
el3.click()
el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout//android.widget.EditText")
el4.click()
el5 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout//android.widget.EditText")
el5.send_keys("what is the most popular transportation in china?")
el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.Button\").instance(1)")
el6.click()
time.sleep(2)
el9 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout/android.widget.LinearLayout//android.widget.ImageView[@index='2']")
captured_text = el9.get_attribute("content-desc")

print(el9.get_attribute("content-desc"))
driver.quit()
# el9 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout/android.widget.LinearLayout//android.widget.ImageView[@index='2']")
# captured_text = el9.get_attribute("content-desc")
#
# print(captured_text)


