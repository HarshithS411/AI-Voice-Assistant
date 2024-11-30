import sqlite3

con =sqlite3.connect("jarvis.db") 
cursor =con.cursor()

# query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name varchar(100),path varchar(1000))"
# cursor.execute(query)

# query="INSERT INTO sys_command VALUES (null,'Excel','C:\\Program Files\\Microsoft Office\\root\\Office16\\excel.exe')"
# cursor.execute(query)
# con.commit()

# query="CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name varchar(100),url varchar(1000))"
# cursor.execute(query)


# query="INSERT INTO web_command VALUES (null,'youtube','https://www.youtube.com/')"
# cursor.execute(query)
# con.commit()

# query="DELETE FROM web_command WHERE id=4"
# cursor.execute(query)
# con.commit()

#testing module
app_name = "Android Studio"
cursor.execute('select path from sys_command where name IN(?)',(app_name,))
results=cursor.fetchall()
print(results)

