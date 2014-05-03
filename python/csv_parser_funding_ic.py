'''
(c) Mizzou Data Miners
'''

import argparse
import os
import csv
import sys
import MySQLdb as mysql

#Query database and create a hash map from IC to name
conn = mysql.connect(host="localhost",user="root",passwd="",db="Grants")
cur = conn.cursor()
cur.execute("SELECT ic_id, name FROM IC")
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
  fp1 = open("../data_csv/Funding_IC.csv",'w')
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
          fundingIC = line[header.index("FUNDING_ICs")]
          ICF = fundingIC.split(chr(92))
          #if(terms.count(chr(92))>1):
          ICF_map = {}
          for items in ICF:
            ICArray = items.split(':')
            if(len(ICArray) > 1):
              IC = ICArray[0]
              if IC not in ICF_map.keys():
                ICF_map[IC] = 0
              amount = ICArray[1]
              if(amount == ''):
                amount = 0
              ICF_map[IC] += int(amount)
          for k,v in ICF_map.items():  
            fp1.write("%s,%s,%s\n" % (termHash[k], grantID, v))
        fp.close()
  fp1.close()
  
if "__main__" == __name__:
  parser = argparse.ArgumentParser()
  parser.add_argument("directory")
  parser.add_argument("columns",type=str,nargs='+')
  args = parser.parse_args()
  main(args.directory,args.columns)