def dataset_overview(df):
    """
    Print basic dataset information.
    """

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumn Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nFirst 5 Rows:")
    print(df.head())


def numerical_summary(df):
    """
    Print summary statistics for numerical variables.
    """

    print("\nNumerical Summary:")
    print(df.describe())


def categorical_summary(df):
    """
    Show counts for categorical variables.
    """

    print("\nCategorical Value Counts:")

    for column in df.select_dtypes(include="category").columns:
        print(f"\n{column}")
        print(df[column].value_counts())