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
cur.execute("SELECT organization_id, name FROM Organization")
allTerms = cur.fetchall()
orgHash = {}
for pair in allTerms:
  orgHash[pair[1]] = pair[0]
cur.execute("SELECT department_id, name FROM Department")
allTerms = cur.fetchall()
deptHash = {}
for pair in allTerms:
  deptHash[pair[1]] = pair[0]
cur.close()
conn.close()

def main(directory,columns):
  data = {}
  for colname in columns:
    data[colname] = []
  fp1 = open("../data_csv/Grant_Institution.csv",'w')
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
          if(line[header.index("ORG_NAME")] in orgHash):
            orgID = orgHash[line[header.index("ORG_NAME")]]
          else:
            break
          if(line[header.index("ORG_DEPT")] in deptHash):
            deptID = deptHash[line[header.index("ORG_DEPT")]]
          else:
            break
          grantID = line[header.index("APPLICATION_ID")]
          fp1.write("\"%s\",\"%s\",\"%s\"\n" % (grantID,orgID,deptID))
        fp.close()
  fp1.close()
if "__main__" == __name__:
  parser = argparse.ArgumentParser()
  parser.add_argument("directory")
  parser.add_argument("columns",type=str,nargs='+')
  args = parser.parse_args()
  main(args.directory,args.columns)