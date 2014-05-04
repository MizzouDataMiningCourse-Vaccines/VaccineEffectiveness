'''
(c) Mizzou Data Miners
'''

import argparse
import os
import csv
import re

import sys

def main(directory,name,columns):
  fpout = open("../data_csv/%s.csv" % (name),'w')
  for root, dirs, files in os.walk(directory):
    for name in files:
      if "csv" in name and "PRJ" in name:
        year = re.match(r'.*(?P<year>\d{4})(_\d+)?\.csv',name)
        year = year.group('year')
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
            item = line[mapper[colname]]
            thisline.append('%s' % (item))
          thisline.append(str(year))
          thisline = ','.join(thisline)
          fpout.write("%s\n" % (thisline))
        fp.close()
  fpout.close()

if "__main__" == __name__:
  parser = argparse.ArgumentParser()
  parser.add_argument("directory")
  parser.add_argument("name")
  parser.add_argument("columns",type=str,nargs='+')
  args = parser.parse_args()
  main(args.directory,args.name,args.columns)