from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

from Driver import get_driver, close_driver
from ParseMaster import read_questions
from OutputGenerator import initialize_output, save_response, finalize_output
import time


def run_automation(test_data_path, output_dir, output_file):
    driver = get_driver()
    questions = read_questions(test_data_path)
    responses = []

    writer = initialize_output(output_dir, output_file)  # Initialize output file

    for i in range(0, len(questions), 5):  # Process in batches of 10
        driver = get_driver()  # Get a new driver instance
        setting_up(driver)
        # Process each question in the current batch
        for question in questions[i:i + 5]:
            send_question(driver, question)
            print(get_response(driver))
            navigate_back(driver)

        close_driver(driver)

    # close_driver(driver)
    save_response(writer, responses)  # Save all responses to the Excel file
    finalize_output(writer)
def navigate_back(driver):
    # el2 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
    #                           value="new UiSelector().className(\"android.view.View\").instance(6)")
    # el2.click()
    wait = WebDriverWait(driver, 2)
    el2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                 "new UiSelector().className(\"android.view.View\").instance(6)")))

    el2.click()

def setting_up(driver):
    time.sleep(2)
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue")
    el2.click()
    time.sleep(1)
    el3 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
    el3.click()

def send_question(driver, question):

    el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout//android.widget.EditText")
    el4.click()
    el5 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout//android.widget.EditText")
    el5.send_keys(question)
    el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                              value="new UiSelector().className(\"android.widget.Button\").instance(1)")
    el6.click()
    time.sleep(2)
    el9 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.FrameLayout/android.widget.LinearLayout//android.widget.ImageView[@index='2']")
    captured_text = el9.get_attribute("content-desc")
    # input_field = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout//android.widget.EditText")
    # input_field.send_keys(question)


def get_response(driver):
    # response = driver.find_element(by=AppiumBy.XPATH,value="//android.widget.FrameLayout//android.widget.TextView").text
    el9 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.FrameLayout/android.widget.LinearLayout//android.widget.ImageView[@index='2']")
    captured_text = el9.get_attribute("content-desc")
    return captured_text
