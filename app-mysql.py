import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal


print('app is started...')

# Construct connection string

try:   
   conn = mysql.connector.connect(    
   host="mysql-server-test.mysql.database.azure.com",
   user="sonpal", 
   password="Sonpal@12345", 
   #port=3306, 
   database="test" 
   #ssl_ca="DigiCertGlobalRootCA.crt.pem", 
   #ssl_disabled=False
   )
   
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

# Drop previous table of same name if one exists
cursor.execute("DROP TABLE IF EXISTS inventory;")
print("Finished dropping table (if existed).")

# Create table
cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
print("Finished creating table.")

# Insert some data into table
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
print("Inserted",cursor.rowcount,"row(s) of data.")
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
print("Inserted",cursor.rowcount,"row(s) of data.")
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
print("Inserted",cursor.rowcount,"row(s) of data.")

# Cleanup
conn.commit()
cursor.close()
conn.close()
print("Done.")
