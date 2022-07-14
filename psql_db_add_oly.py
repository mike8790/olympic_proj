#!/usr/bin/python

import psycopg2
from config import config
import sys
import os

table_name = ['rio_2016', 'london_2012', 'beijing_2008', 'athens_2004', \
    'sydney_2000', 'atlanta_1996', 'barcelona_1992', 'seoul_1988']
filenamns = ['rio-2016_oly_table.csv', 'london-2012_oly_table.csv', 'beijing-2008_oly_table.csv', \
    'athens-2004_oly_table.csv', 'sydney-2000_oly_table.csv', 'atlanta-1996_oly_table.csv', \
        'barcelona-1992_oly_table.csv', 'seoul-1988_oly_table.csv']

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
        
    for n in range(len(filenamns)):

        '''USER INPUT: enter table name and choose table columns'''
        sql = '''CREATE TABLE ''' + table_name[n] + '''(Rank int, Country char(30), Gold int, Silver int, Bronze int, Total_Medals int);'''
        print(sql)

        cur.execute(sql)
        
        '''USER INPUT: insert file name to be tranferred to table'''
        
        os.chdir("C:/Users/micha/Desktop/olympic_proj/csv") 

        with open(filenamns[n], 'r') as fin:
            data = fin.read().splitlines(True)
        with open('temp_txt.csv', 'w') as fout:
            fout.writelines(data[1:])
        f = open(r'temp_txt.csv', 'r')
        cur.copy_from(f, table_name[n])
        f.close()
        os.remove('temp_txt.csv')

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.commit()
        conn.close()
        print('Changes committed and database connection closed.')