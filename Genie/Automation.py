from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from datetime import datetime
from typing import Callable
import traceback

from Driver import get_driver, close_driver
from ParseMaster import read_questions
from OutputGenerator import initialize_output, save_response, finalize_output


def run_automation(test_data_path: str, output_dir: str, output_file: str, app_package: str, app_path: str, navigate_back: Callable[[WebDriver], None], setting_up: Callable[[WebDriver], None], send_question: Callable[[WebDriver, str], None], get_response: Callable[[WebDriver], str], send_question_ongoing: Callable[[WebDriver, str], None], get_response_ongoing: Callable[[WebDriver], str]) -> int:
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
                if 'State' in question['contextDict'] and question['contextDict']['State'] == 'Ongoing': # run cases depending on
                    if rate_available < 2:
                        # Get a new driver instance and initialize rates
                        if driver: close_driver(driver)
                        driver = get_driver(app_package, app_path)
                        setting_up(driver)
                        rate_available = 5
                    send_question_ongoing(driver, question['input'])
                    rate_available -= 2
                    response = get_response_ongoing(driver)
                else:
                    if rate_available < 1:
                        # Get a new driver instance and initialize rates
                        if driver: close_driver(driver)
                        driver = get_driver(app_package, app_path)
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
            except Exception: # exception happened, restart driver and try again
                print(traceback.format_exc())
                exceptions += 1
                attempts_left = 25 # allow 25 attempts
                while attempts_left > 0:
                    try:
                        if driver: close_driver(driver)
                        driver = get_driver(app_package, app_path)
                        setting_up(driver)
                        rate_available = 5
                        break
                    except:
                        print(traceback.format_exc())
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
