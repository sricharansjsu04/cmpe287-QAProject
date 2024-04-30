from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': 'your_device_name',
    'appPackage': 'com.openai.chatgpt',
    'appActivity': 'com.openai.chatgpt.MainActivity',  # Assuming this is the main activity
    'automationName': 'UiAutomator2'  # Use UiAutomator2 for better compatibility
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)

# Start the app and go to the gallery
# Update these XPaths and IDs based on the actual UI elements in your app
el6 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.LinearLayout[@content-desc='Gallery']/android.widget.ImageView")
el6.click()
driver.swipe(512, 1144, 541, 504, 800)  # Adjust the coordinates based on the actual screen size
els2 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.LinearLayout[@resource-id='ChatGpt:id/gallery_option']")
els2.click()
el2 = driver.find_element(by=AppiumBy.ID, value="ChatGpt:id/next_button")
el2.click()
el7 = driver.find_element(by=AppiumBy.ID, value="ChatGpt:id/message_input")
el7.send_keys("I feel bad")
el8 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Send")
el8.click()

# Get the result
els4 = driver.find_elements(by=AppiumBy.XPATH, value="//android.widget.LinearLayout[@resource-id='ChatGpt:id/message_container']//android.widget.TextView")
