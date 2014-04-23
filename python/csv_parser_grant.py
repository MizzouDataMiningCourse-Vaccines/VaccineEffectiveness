'''
(c) Mizzou Data Miners
'''

import argparse
import os
import csv

import sys

def main(directory,name,columns):
  data = []
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
        for line in reader:
          thisline = []
          for colname in columns:
            thisline.append(line[mapper[colname]])
          data.append(thisline)
        fp.close()
  print("Saving to files")
  fp = open("%s.csv" % (name),'w')
  for line in data:
    line = ','.join(line)
    fp.write("%s\n" % (line))
  fp.close()

if "__main__" == __name__:
  parser = argparse.ArgumentParser()
  parser.add_argument("directory")
  parser.add_argument("name")
  parser.add_argument("columns",type=str,nargs='+')
  args = parser.parse_args()
  main(args.directory,args.name,args.columns)