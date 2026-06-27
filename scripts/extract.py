import pandas as pd

def extract_data(file_path):
    """
    Extract dataset from CSV file.
    """

    print("\n========== EXTRACT ==========")

    df = pd.read_csv(file_path)

    print("Dataset Loaded Successfully!")
    print(f"Shape: {df.shape}")

    return df