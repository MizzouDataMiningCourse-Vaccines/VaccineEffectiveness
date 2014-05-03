'''
(c) Mizzou Data Miners
'''

import argparse
import os
import csv
import sys
fp2 = open("../data_csv/438_frequent_terms.csv")
reader = csv.reader(fp2, delimiter="\t")
termHash = []
for line in reader:
    termHash.append(line[1])

def main(directory,columns):
  data = {}
  for colname in columns:
    data[colname] = []
  fp1 = open("../sean_csv/auto_encoder_input.csv",'w')
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
            temp = terms.split(';')
            itemss = [x.lower() for x in temp]
            row = []
            for term in termHash:
              if term in itemss:
                row.append(1)
              else:
                row.append(0)
            fp1.write(grantID+",")
            fp1.write(",".join(str(x) for x in row))
            fp1.write("\n")
        fp.close()
  fp1.close()
if "__main__" == __name__:
  parser = argparse.ArgumentParser()
  parser.add_argument("directory")
  parser.add_argument("columns",type=str,nargs='+')
  args = parser.parse_args()
  main(args.directory,args.columns)