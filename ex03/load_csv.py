import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    Prints the dataset dimensions.
    Returns the DataFrame or None if an error occurs.
    """
    try:
        df = pd.read_csv(path)
        if df.empty:
            print(f"File is empty: {path}")
            return None

        print(f"Loading dataset of dimensions {df.shape}")
        return df

    except pd.errors.EmptyDataError:
        print(f"Error: no data in file: {path}")
        return None
    except pd.errors.ParserError:
        print(f"Error: could not parse CSV: {path}")
        return None
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
