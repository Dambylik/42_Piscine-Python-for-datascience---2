import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def convert_population(value_str):
    """Converts population strings (e.g., '60.1M', '300k') to integers."""
    value_str = str(value_str).strip()
    if value_str.endswith('M'):
        return int(float(value_str[:-1]) * 1_000_000)
    if value_str.endswith('k'):
        return int(float(value_str[:-1]) * 1_000)
    try:
        return int(value_str)
    except ValueError:
        return None


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

        all_years = my_country_data.columns[1:].astype(int)
        values1_raw = my_country_data.values[0, 1:]
        values2_raw = another_country_data.values[0, 1:]
        filter = (all_years >= 1800) & (all_years <= 2050)
        years_to_plot = all_years[filter]
        values1_to_plot = values1_raw[filter]
        values2_to_plot = values2_raw[filter]
        values1 = [convert_population(v) for v in values1_to_plot]
        values2 = [convert_population(v) for v in values2_to_plot]

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.plot(years_to_plot, values2, label=country2, color="blue")
        plt.plot(years_to_plot, values1, label=country1, color="green")
        plt.yticks([20_000_000, 40_000_000, 60_000_000], ["20M", "40M", "60M"])
        plt.xticks(np.arange(1800, 2050, 40))
        plt.legend(loc='lower right')
        plt.show()

    except Exception as e:
        print(f"Error while plotting: {e}")


def main():
    """Main function"""
    aff_pop("France", "Belgium", "population_total.csv")


if __name__ == "__main__":
    "main run"
    main()
