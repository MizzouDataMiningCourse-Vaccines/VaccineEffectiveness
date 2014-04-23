import MySQLdb as mysql

conn = mysql.connect(host="localhost",user="root",passwd="",db="grants")

cur = conn.cursor()

cur.execute("SELECT * FROM `Grant`")

output = cur.fetchall()

print(output)

cur.close()

conn.close()

print("done!")
