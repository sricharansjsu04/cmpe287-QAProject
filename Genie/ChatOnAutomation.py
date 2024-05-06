from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from Driver import get_driver, close_driver
from ParseMaster import read_questions
from OutputGenerator import initialize_output, save_response, finalize_output
import time
from datetime import datetime


def run_chatOn_automation(test_data_path, output_dir, output_file) -> int:
    driver = None
    questions = read_questions(test_data_path)
    responses = []

    writer = initialize_output(output_dir, output_file)  # Initialize output file
    rate_available = 0  # how many questions we can still ask; if not enough is available, we force a reset
    exceptions = 0  # track number of exceptions that forced a driver reset
    start_time = datetime.now()
    print("Starting automation at " + str(start_time) + "...")
    for i in range(0, len(questions)):
        question = questions.iloc[i]
        print(question)
        completed = False
        while not completed:
            try:
                # if question['contextDict']['State'] == 'Ongoing': # run cases depending on
                #     # Get a new driver instance and initialize rates
                #     if driver: close_driver(driver)
                #     driver = get_driver(1)
                #     setting_up_chatOn(driver)
                # else:
                if driver: close_driver(driver)
                driver = get_driver(1)
                setting_up_chatOn(driver)
                send_chatOn_question(driver, question['input'])
            except Exception as e:
                print(e)


def setting_up_chatOn(driver: WebDriver):
    time.sleep(2)
    el1 = driver.find_element(AppiumBy.ID, 'ai.chat.gpt.bot:id/continueButton')
    el1.click()
    el1.click()
    el1.click()
    el1.click()
    el2 = driver.find_element(AppiumBy.ID, 'ai.chat.gpt.bot:id/close')
    el2.click()


def send_chatOn_question(driver: WebDriver, question: str):
    wait = WebDriverWait(driver, 2)
    el4 = wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="ai.chat.gpt.bot:id/inputEditText"]')))
    el4.click()
    el5 = wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="ai.chat.gpt.bot:id/inputEditText"]')))
    el5.send_keys(question)
    el6 = wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, '//android.widget.Button[@resource-id="ai.chat.gpt.bot:id/sendButton"]')))
    el6.click()
    driver.hide_keyboard()
    time.sleep(4)
    el7 = driver.find_element(AppiumBy.XPATH,
                              '//android.widget.TextView[@resource-id="ai.chat.gpt.bot:id/message_text_view"]')
    captured_text = el7.get_attribute("text")
