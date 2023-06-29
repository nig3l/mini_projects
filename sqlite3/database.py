import sqlite3

# incase you'd want to delete data after you're done with it .
# connection = sqlite3.connect(':memory:')

 #creates/connects the said db for me
connection = sqlite3.connect('customer.db')

# create a cursor
c = connection.cursor()

# create a table
c.execute(""" CREATE TABLE customers(
             first_name text,
             last_name text,
             email text
 
)
""")
        # commit command    
connection.commit()

# close connection
connection.close()

 


