import pandas as pd

def load_dataset(filepath):
    """
    Load the heart disease dataset and assign column headers.
    """

    columns = [
        "age",
        "sex",
        "cp",
        "trestbps",
        "chol",
        "fbs",
        "restecg",
        "thalach",
        "exang",
        "oldpeak",
        "slope",
        "ca",
        "thal",
        "target"
    ]

    df = pd.read_csv(filepath, names=columns)

    return df