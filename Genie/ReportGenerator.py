import pandas as pd
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def safe_json_loads(s):
    try:
        # Replace single quotes with double quotes to correct the JSON formatting
        corrected_json = s.replace("'", '"')
        return json.loads(corrected_json.strip())  # Attempt to load the corrected JSON string
    except ValueError as e:
        print(f"JSON parsing error: {e} for JSON: {s}")  # Debugging output
        return {}  # Return empty dictionary if JSON is invalid

def compare_dicts(d1, d2):
    if d1 == d2:
        return 'pass'
    elif d1.get('Keyword match') == d2.get('Keyword match') or d1.get('Category match') == d2.get('Category match'):
        return 'partial'
    else:
        return 'fail'

def process_excel(file_path):
    df = pd.read_excel(file_path)
    print("DataFrame loaded:", df.head())  # Print the first few rows to verify content

    df['result'] = df.apply(lambda row: compare_dicts(safe_json_loads(row['expout']), safe_json_loads(row['aiout'])), axis=1)
    df['score'] = df['result'].map({'pass': 1, 'partial': 0.5, 'fail': 0})

    total_pass = (df['result'] == 'pass').sum()
    total_partial = (df['result'] == 'partial').sum()
    total_fail = (df['result'] == 'fail').sum()
    test_score = df['score'].sum()

    with PdfPages('output/results_visualization.pdf') as pdf:
        plt.figure(figsize=(8, 6))
        results = ['Pass', 'Partial', 'Fail']
        counts = [total_pass, total_partial, total_fail]
        plt.bar(results, counts, color=['green', 'yellow', 'red'])
        plt.title('Test Results')
        plt.xlabel('Result Type')
        plt.ylabel('Count')
        plt.grid(True)
        pdf.savefig()
        plt.close()

        text_str = f"Total Passes: {total_pass}\nTotal Partials: {total_partial}\nTotal Fails: {total_fail}\nTest Score: {test_score}"
        plt.figure(figsize=(8, 6))
        plt.text(0.01, 0.5, text_str, wrap=True)
        plt.axis('off')
        pdf.savefig()
        plt.close()

    output_path = file_path.replace('_updated.xlsx', '_results.xlsx')
    df.to_excel(output_path, index=False)
    print(f"Done. Saved results to {output_path} and PDF to 'output/results_visualization.pdf'")
    print(f"Total Passes: {total_pass}, Total Partials: {total_partial}, Total Fails: {total_fail}, Test Score: {test_score}")

    return df

# Example usage
file_path = 'output/test_output_updated.xlsx'
df = process_excel(file_path)