import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def aff_pop(my_country: str, another_country: str, path: str):
    """
    Loads the dataset and displays the population projection
    for two given countries.
    """
    df = load(path)
    if df is None:
        return 
    try:
        country1 = my_country
        country2 = another_country
        my_country_data = df.query("country == @country1")
        another_country_data = df.query("country == @country2")

        if my_country_data.empty or another_country_data.empty:
            print("Error: country not found in dataset")
            return

        years = my_country_data.columns[1:].astype(int)
        values1 = my_country_data.values[0, 1:]
        values2 = another_country_data.values[0, 1:]
        
        plt.plot(years, values1, label=country1, color="green")
        plt.plot(years, values2, label=country2, color="blue")
        
        plt.xticks(np.arange(1800, 2050, 40))        
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"Error while plotting: {e}")


def main():
    """Main function"""
    aff_pop("France", "Belgium", "population_total.csv")


if __name__ == "__main__":
    "main run"
    main()
