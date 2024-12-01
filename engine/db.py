import sqlite3
import csv

con =sqlite3.connect("jarvis.db") 
cursor =con.cursor()

# for inserting inbuilt apps 
# query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name varchar(100),path varchar(1000))"
# cursor.execute(query)

# query="INSERT INTO sys_command VALUES (null,'Excel','C:\\Program Files\\Microsoft Office\\root\\Office16\\excel.exe')"
# cursor.execute(query)
# con.commit()

# for web apps
# query="CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name varchar(100),url varchar(1000))"
# cursor.execute(query)


# query="INSERT INTO web_command VALUES (null,'youtube','https://www.youtube.com/')"
# cursor.execute(query)
# con.commit()

# query="DELETE FROM web_command WHERE id=4"
# cursor.execute(query)
# con.commit()

#testing module
# app_name = "Android Studio"
# cursor.execute('select path from sys_command where name IN(?)',(app_name,))
# results=cursor.fetchall()
# print(results)

# cursor.execute('drop table contacts')



# create a table with the desired colums
# cursor.execute('''Create table if not exists contacts (id integer primary key ,name varchar(255),mobile_no varchar(255),email varchar(255) null)''')




# Specify the column indices you want to import (0-based index)
# example importing the 1st and 3rd columns
desired_columns_indices=[0,18]

# read data from CSV and insert into SQLITE table from desierd column
with open('contacts.csv','r',encoding='utf-8')as csvfile:
    csvreader =csv.reader(csvfile)
    for row in csvreader:
        selected_data=[row[i] for i in desired_columns_indices]
        cursor.execute('''insert into contacts (id,'name','mobile_no') values(null,?,?);''',tuple(selected_data)) 

# commit changes and close connection
con.commit()
con.close


# query="insert into contacts values(null,'kishore','9535235174',null)"
# cursor.execute(query)
# con.commit()

# query = 'kishore'
# query = query.strip().lower()

# # Execute the query with properly formatted parameters
# cursor.execute(
#     "SELECT mobile_no FROM contacts WHERE lower(name) LIKE ? OR lower(name) LIKE ?", 
#     ('%' + query + '%', '%' + query + '%')
# )

# # Fetch and print the results
# results = cursor.fetchall()
# print(results[0][0])  # Print the first result

