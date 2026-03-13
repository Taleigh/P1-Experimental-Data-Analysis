from src.data_loader import load_dataset
from src.data_cleaning import clean_dataset
from src.eda_analysis import dataset_overview
from src.statistics import correlation_matrix
from src.visualisation import plot_age_distribution

def main():

    df = load_dataset("data/heart_disease.csv")

    df = clean_dataset(df)

    dataset_overview(df)

    correlation_matrix(df)

    plot_age_distribution(df)

if __name__ == "__main__":
    main()