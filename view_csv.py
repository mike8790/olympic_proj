import pandas as pd


def view_csv(filepathname: string, separator: string)


df = pd.read_csv(filepathname, sep=separator)

print(df)
