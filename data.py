import pandas as pd
from pandas import DataFrame


def read_dataset(name: str) -> DataFrame:
    return pd.read_excel(name)


def get_filtered_dataset(name: str, query: str, columns) -> DataFrame:
    dataset = read_dataset(name).query(query)
    return DataFrame(dataset, columns=columns)
