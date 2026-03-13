import pandas as pd
import numpy as np


def clean_dataset(df):
    """
    Perform basic cleaning on the dataset.
    """

    # Replace '?' with NaN
    df = df.replace("?", np.nan)

    # Convert numeric columns
    numeric_columns = [
        "age","trestbps","chol","thalach","oldpeak","ca"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Convert categorical columns
    categorical_columns = [
        "sex","cp","fbs","restecg","exang","slope","thal","target"
    ]

    for col in categorical_columns:
        df[col] = df[col].astype("category")

    # Drop rows with missing values
    df = df.dropna()

    return df