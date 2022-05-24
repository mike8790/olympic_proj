import pandas as pd


def view_csv(filepathname: str, separator: str):
    df = pd.read_csv(filepathname, sep=separator)
    print(df)
