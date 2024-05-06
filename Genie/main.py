from Automation import run_automation
import GenieAutomation
from ChatOnAutomation import run_chatOn_automation

if __name__ == '__main__':
    # Paths
    test_data_path = 'Input/Deliverable2B-testcases-for-testing.xlsx'
    output_dir = './output'
    output_file = 'test_output.xlsx'
    app_package = 'co.appnation.geniechat'
    app_path = '../ai-chat-and-chatbot-genie-6-1-1.apk'
    # app_package = 'ai.chat.gpt.bot'
    # app_path = '../ChatOn - AI Chat Bot Assistant_1.40.348-398_apkcombo.com.apk'

    if app_package == 'ai.chat.gpt.bot':
        run_chatOn_automation(test_data_path, output_dir, output_file, app_package, app_path)
    elif app_package == 'co.appnation.geniechat':
        run_automation(test_data_path, output_dir, output_file, app_package, app_path, GenieAutomation.navigate_back, GenieAutomation.setting_up, GenieAutomation.send_question, GenieAutomation.get_response, GenieAutomation.send_question_ongoing, GenieAutomation.get_response_ongoing)
    else:
        print('Invalid app package')
