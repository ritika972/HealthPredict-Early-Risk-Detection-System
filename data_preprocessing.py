import pandas as pd

def load_data(file_path):

    df = pd.read_csv(file_path)

    df.drop_duplicates(inplace=True)

    df.fillna(df.mean(numeric_only=True), inplace=True)

    return df