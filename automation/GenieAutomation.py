from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
import time


def navigate_back(driver: WebDriver):
    # el2 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
    #                           value="new UiSelector().className(\"android.view.View\").instance(6)")
    # el2.click()
    wait = WebDriverWait(driver, 2)
    el2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                 "new UiSelector().className(\"android.view.View\").instance(6)")))

    el2.click()


def setting_up(driver: WebDriver):
    time.sleep(2)
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue")
    el2.click()
    time.sleep(1)
    try:
        el3 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
        el3.click()
    except:
        pass


def send_question(driver: WebDriver, question: str):
    wait = WebDriverWait(driver, 2)
    el4 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.FrameLayout//android.widget.EditText")))
    # el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout//android.widget.EditText")
    el4.click()
    # el5 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout//android.widget.EditText")
    el5 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.FrameLayout//android.widget.EditText")))
    el5.send_keys(question)
    # try:
    #     el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
    #                               value="new UiSelector().className(\"android.widget.Button\").instance(1)")
    # except:  # try again after a second
    #     time.sleep(1)
    #     el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
    #                               value="new UiSelector().className(\"android.widget.Button\").instance(1)")
    el6 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                 "new UiSelector().className(\"android.widget.Button\").instance(1)")))
    el6.click()
    time.sleep(2)
    el9 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.FrameLayout/android.widget.LinearLayout//android.widget.ImageView[@index='2']")
    captured_text = el9.get_attribute("content-desc")
    if not captured_text or captured_text == 'null':  # try again after 3 seconds if value is null
        time.sleep(3)
        el9 = driver.find_element(by=AppiumBy.XPATH,
                                  value="//android.widget.FrameLayout/android.widget.LinearLayout//android.widget.ImageView[@index='2']")
        captured_text = el9.get_attribute("content-desc")
        if not captured_text or captured_text == 'null':  # try again after 5 seconds if value is null
            time.sleep(5)
            el9 = driver.find_element(by=AppiumBy.XPATH,
                                      value="//android.widget.FrameLayout/android.widget.LinearLayout//android.widget.ImageView[@index='2']")
            captured_text = el9.get_attribute("content-desc")
            # if result is still null, will be recorded as null
    # input_field = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout//android.widget.EditText")
    # input_field.send_keys(question)


def send_question_ongoing(driver: WebDriver, question: str):
    time.sleep(1)
    wait = WebDriverWait(driver, 2)
    el4 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.FrameLayout//android.widget.EditText")))
    # el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout//android.widget.EditText")
    el4.click()
    # el5 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout//android.widget.EditText")
    el5 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.FrameLayout//android.widget.EditText")))
    filler_question = "what are the overall transportation preferences around the globe?"
    print(filler_question)
    el5.send_keys(filler_question)
    # try:
    #     el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
    #                               value="new UiSelector().className(\"android.widget.Button\").instance(1)")
    # except:  # try again after a second
    #     time.sleep(1)
    #     el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
    #                               value="new UiSelector().className(\"android.widget.Button\").instance(1)")
    el6 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                 "new UiSelector().className(\"android.widget.Button\").instance(1)")))
    el6.click()
    time.sleep(2)
    # el12 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout//android.widget.EditText")
    el12 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.FrameLayout//android.widget.EditText")))
    el12.click()
    # el13 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout//android.widget.EditText")
    el13 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.FrameLayout//android.widget.EditText")))
    el13.send_keys(question)
    # try:
    #     el14 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
    #                             value="new UiSelector().className(\"android.widget.Button\").instance(3)")
    # except:  # try again after a second
    #     time.sleep(1)
    #     el14 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
    #                             value="new UiSelector().className(\"android.widget.Button\").instance(3)")
    el14 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                 "new UiSelector().className(\"android.widget.Button\").instance(3)")))
    if el14.get_attribute('content-desc') == "Share":
        el14 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().className(\"android.widget.Button\").instance(4)")))
    el14.click()
    time.sleep(2)
    el9 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.FrameLayout/android.widget.LinearLayout//android.widget.ImageView[@index='0']")
    captured_text = el9.get_attribute("content-desc")
    if not captured_text or captured_text == 'null':  # try again after 3 seconds if value is null
        time.sleep(3)
        el9 = driver.find_element(by=AppiumBy.XPATH,
                                  value="//android.widget.FrameLayout/android.widget.LinearLayout//android.widget.ImageView[@index='0']")
        captured_text = el9.get_attribute("content-desc")
        if not captured_text or captured_text == 'null':  # try again after 5 seconds if value is null
            time.sleep(5)
            el9 = driver.find_element(by=AppiumBy.XPATH,
                                      value="//android.widget.FrameLayout/android.widget.LinearLayout//android.widget.ImageView[@index='0']")
            captured_text = el9.get_attribute("content-desc")
            # if result is still null, will be recorded as null
    # input_field = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout//android.widget.EditText")
    # input_field.send_keys(question)


def get_response(driver: WebDriver):
    # response = driver.find_element(by=AppiumBy.XPATH,value="//android.widget.FrameLayout//android.widget.TextView").text
    el9 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.FrameLayout/android.widget.LinearLayout//android.widget.ImageView[@index='2']")
    captured_text = el9.get_attribute("content-desc")
    return captured_text


def get_response_ongoing(driver: WebDriver):
    # response = driver.find_element(by=AppiumBy.XPATH,value="//android.widget.FrameLayout//android.widget.TextView").text
    el9 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.FrameLayout/android.widget.LinearLayout//android.widget.ImageView[@index='0']")
    captured_text = el9.get_attribute("content-desc")
    return captured_text
