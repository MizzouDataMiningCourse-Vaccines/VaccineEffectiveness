'''
(c) Mizzou Data Miners
'''

import argparse
import os
import csv

import sys

def main(directory,columns):
  data = {}
  for colname in columns:
    data[colname] = []
    
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
          for colname,index in mapper.items():
            terms = line[index]
            itemss = terms.split(';')
            for item in itemss:
              data[colname].append(item)
        fp.close()
        data[colname] = list(set(data[colname]))
  print("Saving to files")
  for key,array in data.items():
    fp = open("../data_csv/terms/%s.unique.csv" % (key),'w')
    uniqueSet = set(array)
    for item in uniqueSet:
      fp.write("%s\n" % (item))
    fp.close()

if "__main__" == __name__:
  parser = argparse.ArgumentParser()
  parser.add_argument("directory")
  parser.add_argument("columns",type=str,nargs='+')
  args = parser.parse_args()
  main(args.directory,args.columns)