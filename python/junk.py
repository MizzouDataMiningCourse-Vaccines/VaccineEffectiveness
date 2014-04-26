import MySQLdb as mysql

conn = mysql.connect(host="localhost",user="root",passwd="",db="Grants")
cur = conn.cursor()
cur.execute("SELECT * FROM Term LIMIT")
allTerms = cur.fetchall()
mapper = {}
for pair in allTerms:
  mapper[pair[1]] = pair[0]
cur.close()
conn.close()
