'''
(c) Us
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
        print("Name:",name)
        fp = open("%s%s" % (root,name),'r')
        reader = csv.reader(fp, delimiter=',', quotechar='"')
        mapper = {}
        header = next(reader)
        for colname in columns:
          mapper[colname] = header.index(colname)
        for line in reader:
          for colname,index in mapper.items():
            item = line[index]
            if item not in data[colname]:
              data[colname].append(item)
        fp.close()
  print("Saving to files")
  for key,array in data.items():
    fp = open("%s.unique.csv" % (key),'w')
    for item in array:
      fp.write("%s\n" % (item))
    fp.close()

if "__main__" == __name__:
  parser = argparse.ArgumentParser()
  parser.add_argument("directory")
  parser.add_argument("columns",type=str,nargs='+')
  args = parser.parse_args()
  main(args.directory,args.columns)