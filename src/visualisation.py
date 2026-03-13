import matplotlib.pyplot as plt
import seaborn as sns


def plot_age_distribution(df):

    plt.figure()

    sns.histplot(df["age"], bins=20)

    plt.title("Age Distribution of Patients")

    plt.savefig("visuals/age_distribution.png")

    plt.close()


def plot_cholesterol_vs_age(df):

    plt.figure()

    sns.scatterplot(x=df["age"], y=df["chol"])

    plt.title("Cholesterol vs Age")

    plt.savefig("visuals/cholesterol_vs_age.png")

    plt.close()


def plot_heart_disease_by_sex(df):

    plt.figure()

    sns.countplot(x="sex", hue="target", data=df)

    plt.title("Heart Disease by Sex")

    plt.savefig("visuals/heart_disease_by_sex.png")

    plt.close()


def plot_correlation_heatmap(corr):

    plt.figure()

    sns.heatmap(corr, annot=True)

    plt.title("Feature Correlation Heatmap")

    plt.savefig("visuals/correlation_heatmap.png")

    plt.close()