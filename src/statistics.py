import pandas as pd


def correlation_matrix(df):
    """
    Compute correlation matrix for numerical features.
    """

    corr = df.corr(numeric_only=True)

    print("\nCorrelation Matrix:")
    print(corr)

    return corr


def heart_disease_by_sex(df):
    """
    Compare heart disease prevalence by sex.
    """

    summary = pd.crosstab(df["sex"], df["target"])

    print("\nHeart Disease by Sex:")
    print(summary)

    return summary


def average_values_by_diagnosis(df):
    """
    Compare mean clinical measurements by diagnosis.
    """

    summary = df.groupby("target").mean(numeric_only=True)

    print("\nAverage Clinical Values by Diagnosis:")
    print(summary)

    return summary