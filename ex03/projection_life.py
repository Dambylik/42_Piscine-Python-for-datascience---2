import matplotlib.pyplot as plt
from load_csv import load


def projection_life(path_gdp: str, path_life: str) -> None:
    """
    Loads the GDP and life expectancy datasets and displays a comparison
    of the population projections for two countries.
    """
    gdp_df = load(path_gdp)
    life_df = load(path_life)
    if gdp_df is None or life_df is None:
        return
    try:
        gdp_data = gdp_df[["country", "1900"]]
        life_data = life_df[["country", "1900"]]

        if gdp_data.empty or life_data.empty:
            print("Error: data not found in dataset")
            return

        merged_data = gdp_data.merge(life_data,
                                     on="country",
                                     suffixes=("_gdp", "_life"))

        plt.scatter(merged_data["1900_gdp"], merged_data["1900_life"])
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.xscale("log")
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
        plt.ylabel("Life expectancy")
        plt.show()

    except Exception as e:
        print(f"Error while plotting: {e}")


def main():
    """Main function"""
    projection_life(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
        "life_expectancy_years.csv")


if __name__ == "__main__":
    "main run"
    main()
