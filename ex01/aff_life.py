import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def aff_life(country: str, path: str):
    """
    Loads the dataset and displays the life expectancy projection
    for the given country.
    """
    df = load(path)
    if df is None:
        return
    try:
        country_data = df.query("country == @country")  # Select rows where country is equal to my variable country
        if country_data.empty:
            print(f"Error: country {country} not found in dataset")
            return

        years = country_data.columns[1:]
        years = years.astype(int)
        values = country_data.values[0, 1:]

        plt.xticks(np.arange(1800, 2100, 40))
        plt.plot(years, values)
        plt.title(f"{country} Life Expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()

    except Exception as e:
        print(f"Error while plotting: {e}")


def main():
    """Main function"""
    aff_life("France", "life_expectancy_years.csv")


if __name__ == "__main__":
    "main run"
    main()
