from Automation import run_automation

if __name__ == '__main__':
    # Paths
    test_data_path = 'Input/Deliverable2B-testcases.xlsx'
    output_dir = './output'
    output_file = 'test_output.xlsx'

    run_automation(test_data_path, output_dir, output_file)
