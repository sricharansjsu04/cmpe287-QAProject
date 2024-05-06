import pandas as pd
import json

def read_questions(file_path: str):
    df = pd.read_excel(file_path)
    filtered = df[['subkey', 'input', 'contextDict', 'expoutput']]
    filtered.loc[:, 'contextDict'] = filtered.loc[:, 'contextDict'].apply(lambda x: json.loads(x.replace("'", "\"")))
    filtered.loc[:, 'expoutput'] = filtered.loc[:, 'expoutput'].apply(lambda x: json.loads(x.replace("'", "\"")))
    return filtered.head(10)
