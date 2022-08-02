#!/usr/bin/python

from sqlalchemy import create_engine
import psycopg2
from config import config
import pandas as pd

def sql_to_df(sql_table):

    """ Connect to the PostgreSQL database server """
    conn = None

    try:
    # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
            
        # create a cursor
        cur = conn.cursor()
            
        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)


        sql = '''SELECT * FROM ''' + sql_table + ''';'''   
        print(sql)

        cur.execute(sql)

        df = pd.read_sql(sql, conn)
        # df = pd.DataFrame(cur.fetchall())   
        
        return df

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit()
            conn.close()
            print('Changes committed and database connection closed.')

if __name__ == "__main__":
    import sys
    sql_to_df(sys.argv[1])
