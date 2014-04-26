'''
(c) Mizzou Data Miners
'''

import argparse
import os
import csv
import sys
import MySQLdb as mysql

conn = mysql.connect(host="localhost",user="root",passwd="",db="Grants")
cur = conn.cursor()
cur.execute("SELECT term_id, LOWER(name) FROM Term")
allTerms = cur.fetchall()
termHash = {}
for pair in allTerms:
  termHash[pair[1]] = pair[0]
cur.close()
conn.close()

def main(directory,columns):
  data = {}
  for colname in columns:
    data[colname] = []
  fp1 = open("../data_csv/PROJECT_TERMS.relation.csv",'w')
  for root, dirs, files in os.walk(directory):
    for name in files:
      if "csv" in name and "PRJ" in name:
        print("On file",name)
        fp = open("%s%s" % (root,name),'r')
        reader = csv.reader(fp, delimiter=',', quotechar='"')
        mapper = {}
        header = next(reader)
        for colname in columns:
          mapper[colname] = header.index(colname)
          #data[colname] = []
        for line in reader:
          grantID = line[header.index("APPLICATION_ID")]
          for colname,index in mapper.items():
            terms = line[index]
            itemss = terms.split(';')
            for item in itemss:
              if item.lower() in termHash:
                fp1.write("%s,%s\n" % (grantID,termHash[item.lower()]))
              else:
                print(item)
                print("\n")
        fp.close()
  fp1.close()
if "__main__" == __name__:
  parser = argparse.ArgumentParser()
  parser.add_argument("directory")
  parser.add_argument("columns",type=str,nargs='+')
  args = parser.parse_args()
  main(args.directory,args.columns)