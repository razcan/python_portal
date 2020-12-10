#testing sql connection

import pyodbc

# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=ROBUN028\\RZC;'
#                       'Database=TINMAR_ERP_NEW_LOCAL;'
#                       'Trusted_Connection=yes;')
#

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=ROBUN028\\RZC;DATABASE=TINMAR_ERP_NEW_LOCAL;UID=sa;PWD=vasilica#25')

cursor = conn.cursor()
cursor.execute('SELECT top 10 * FROM Document')

for row in cursor:
    print(row)
