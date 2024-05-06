from Automation import run_genie_automation
from ChatOnAutomation import run_chatOn_automation

if __name__ == '__main__':
    # Paths
    test_data_path = 'Input/Deliverable2B-testcases.xlsx'
    output_dir = './output'
    output_file = 'test_output.xlsx'

    # run_genie_automation(test_data_path, output_dir, output_file)
    run_chatOn_automation(test_data_path, output_dir, output_file)
