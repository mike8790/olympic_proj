#!/usr/bin/python

import psycopg2
from config import config
import sys
import os

def send_query(query_text):
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
        
        sql = query_text
        print(sql)

        cur.execute(sql)
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit()
            conn.close()
            print('Changes committed and database connection closed.')