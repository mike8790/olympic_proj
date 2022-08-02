#!/usr/bin/python

from pathlib import Path
from sqlalchemy import create_engine
import pandas as pd
import psycopg2

def df_to_sql(df_sql, table_name):
    # Create engine to connect with sql db using sqlalchemy.
    # First argument is db URI as string
    # If using postgresql as I am the URI will be structured as such...
    # postgresql+psycopg2://[username]:[password]@[hostname]:[port]/[dbname]
    engine = create_engine("")

    # use pandas .to_sql to send table to db you have made a connection with, specify 
    # table name when calling module
    df_sql.to_sql(table_name, engine)

if __name__ == "__main__":
    import sys
    sql_to_df(sys.argv[1])
