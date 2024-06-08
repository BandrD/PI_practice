import pandas as pd


def preprocess_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df = df.dropna()
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    preprocess_data('data/raw/data.csv', 'data/processed/data.csv')
