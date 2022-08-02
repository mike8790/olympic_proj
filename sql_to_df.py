#!/usr/bin/python

from pathlib import Path
from sqlalchemy import create_engine
import pandas as pd
import psycopg2

def sql_to_df(sql_tb):
    # Create engine to connect with sql db using sqlalchemy.
    # First argument is db URI as string
    # If using postgresql as I am the URI will be structured as such...
    # postgresql+psycopg2://[username]:[password]@[hostname]:[port]/[dbname]
    engine = create_engine("")

    # uses table name entered when calling module and connection engine to access correct table
    table_df = pd.read_sql_table(sql_tb, engine)

    return table_df

if __name__ == "__main__":
    import sys
    sql_to_df(sys.argv[1])
