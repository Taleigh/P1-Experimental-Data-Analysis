from src.data_loader import load_dataset
from src.data_cleaning import clean_dataset
from src.eda_analysis import dataset_overview, numerical_summary, categorical_summary
from src.statistics import correlation_matrix, heart_disease_by_sex, average_values_by_diagnosis
from src.visualisation import (
    plot_age_distribution,
    plot_cholesterol_vs_age,
    plot_heart_disease_by_sex,
    plot_correlation_heatmap
)


def main():

    # Load dataset
    df = load_dataset("data/heart_disease.csv")

    # Clean dataset
    df = clean_dataset(df)

    # Exploratory analysis
    dataset_overview(df)
    numerical_summary(df)
    categorical_summary(df)

    # Statistical analysis
    corr = correlation_matrix(df)
    heart_disease_by_sex(df)
    average_values_by_diagnosis(df)

    # Visualisations
    plot_age_distribution(df)
    plot_cholesterol_vs_age(df)
    plot_heart_disease_by_sex(df)
    plot_correlation_heatmap(corr)


if __name__ == "__main__":
    main()