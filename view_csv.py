import pandas as pd
import sys


def view_csv(filepathname: str, separator: str):
    df_csv = pd.read_csv(filepathname, separator)
    print(df_csv)
    return


if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2], sys.argv[3])
