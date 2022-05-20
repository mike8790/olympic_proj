
import pandas as pd
import sys

print("working")


def tsv_transfer(fff, ffff):
    df = pd.read_csv(fff)
    df.to_csv(ffff, header='True', sep='\t', na_rep='NULL')
    return


if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2], sys.argv[3])
