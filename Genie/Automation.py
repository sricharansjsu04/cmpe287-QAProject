from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from Driver import get_driver, close_driver
from ParseMaster import read_questions
from OutputGenerator import initialize_output, save_response, finalize_output
import time
from datetime import datetime


def run_genie_automation(test_data_path, output_dir, output_file) -> int:
    driver = None
    questions = read_questions(test_data_path)
    responses = []

    writer = initialize_output(output_dir, output_file)  # Initialize output file
    rate_available = 0 # how many questions we can still ask; if not enough is available, we force a reset
    exceptions = 0 # track number of exceptions that forced a driver reset
    start_time = datetime.now()
    print("Starting automation at " + str(start_time) + "...")
    for i in range(0, len(questions)):
        question = questions.iloc[i]
        print(question)
        completed = False
        null_count = 0
        while not completed:
            try:
                if question['contextDict']['State'] == 'Ongoing': # run cases depending on
                    if rate_available < 2:
                        # Get a new driver instance and initialize rates
                        if driver: close_driver(driver)
                        driver = get_driver(0)
                        setting_up(driver)
                        rate_available = 5
                    send_question_ongoing(driver, question['input'])
                    rate_available -= 2
                    response = get_response_ongoing(driver)
                else:
                    if rate_available < 1:
                        # Get a new driver instance and initialize rates
                        if driver: close_driver(driver)
                        driver = get_driver(0)
                        setting_up(driver)
                        rate_available = 5
                    send_question(driver, question['input'])
                    rate_available -= 1
                    response = get_response(driver)
                navigate_back(driver)
                print(response)
                if not response or response == 'null' and null_count < 5: # yes, literally 'null' somehow happens
                    null_count += 1
                    continue
                responses.append({'Index': question.name, 'subkey': question['subkey'], 'expout': question['expoutput'], 'Response': response})
                completed = True
            except Exception as e: # exception happened, restart driver and try again
                print(e)
                exceptions += 1
                attempts_left = 25 # allow 25 attempts
                while attempts_left > 0:
                    try:
                        print(e)
                        if driver: close_driver(driver)
                        driver = get_driver(0)
                        setting_up(driver)
                        rate_available = 5
                        break
                    except:
                        attempts_left -= 1
                if attempts_left == 0:
                    save_response(writer, responses)  # Save all responses to the Excel file
                    print("Failed to reset driver. Exiting.")
                    end_time = datetime.now()
                    diff = end_time - start_time
                    avg = diff / len(responses)
                    print("Automation ended at " + str(end_time) + " after " + str(diff) + " seconds.")
                    print("Average time per case (seconds): " + str(avg))
                    print("Total cases: " + str(len(responses)))
                    print("Exceptions: " + str(exceptions))
                    exit(1)
    if driver: close_driver(driver)
    save_response(writer, responses)  # Save all responses to the Excel file
    # finalize_output(writer)
    print("Done. Saved responses to " + output_file)
    end_time = datetime.now()
    diff = end_time - start_time
    avg = diff / len(responses)
    print("Automation ended at " + str(end_time) + " after " + str(diff) + " seconds.")
    print("Average time per case (seconds): " + str(avg))
    print("Total cases: " + str(len(responses)))
    print("Exceptions: " + str(exceptions))
    return exceptions

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
