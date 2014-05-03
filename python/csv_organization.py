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
cur.execute("SELECT * FROM City")
allTerms = cur.fetchall()
cityHash = {}
for pair in allTerms:
  cityHash[pair[1]] = pair[0]
cur.execute("SELECT * FROM State")
allTerms = cur.fetchall()
stateHash = {}
for pair in allTerms:
  stateHash[pair[1]] = pair[0]
cur.execute("SELECT * FROM Country")
allTerms = cur.fetchall()
countryHash = {}
for pair in allTerms:
  countryHash[pair[1]] = pair[0]
cur.close()
conn.close()

def main(directory,columns):
  data = {}
  for colname in columns:
    data[colname] = []
  fp1 = open("../data_csv/Organization.duplicates.csv",'w')
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
          if(line[header.index("ORG_CITY")] in cityHash):
            cityID = int(cityHash[line[header.index("ORG_CITY")]])
          else:
            cityID = cityHash["n/a"]
          if(line[header.index("ORG_STATE")] in stateHash):
            stateID = stateHash[line[header.index("ORG_STATE")]]
          else:
            stateID = stateHash["n/a"]
          if(line[header.index("ORG_COUNTRY")] in countryHash):
            countryID = countryHash[line[header.index("ORG_COUNTRY")]]
          else:
            countryID = countryHash["n/a"]
          if line[header.index("ORG_DISTRICT")] is None or line[header.index("ORG_DISTRICT")] is "":
            district = "-1"
          else:
            district = line[header.index("ORG_DISTRICT")]
          if line[header.index("ORG_NAME")] is None or line[header.index("ORG_NAME")] is "":
            break
          else:
            name = line[header.index("ORG_NAME")]
          if not isinstance(line[header.index("ORG_ZIPCODE")],int) or line[header.index("ORG_ZIPCODE")] is "":
            zipcode = 0
          else:
            zipcode = line[header.index("ORG_ZIPCODE")]
          fp1.write("\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\"\n" % (name,cityID,countryID,stateID,district,zipcode))
        fp.close()
  fp1.close()
if "__main__" == __name__:
  parser = argparse.ArgumentParser()
  parser.add_argument("directory")
  parser.add_argument("columns",type=str,nargs='+')
  args = parser.parse_args()
  main(args.directory,args.columns)