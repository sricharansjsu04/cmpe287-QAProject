import pandas as pd
import os


def initialize_output(output_dir, output_file):
    full_path = os.path.join(output_dir, output_file)

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Check if the file exists and remove it if it does
    if os.path.exists(full_path):
        os.remove(full_path)

    # Create a new Excel writer
    writer = pd.ExcelWriter(full_path, engine='xlsxwriter')
    return writer


def save_response(writer, responses):
    df = pd.DataFrame(responses, columns=['Question', 'Response'])
    df.to_excel(writer, index=False, sheet_name='Results')
    writer.save()


def finalize_output(writer):
    writer.close()
