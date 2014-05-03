'''
(c) Mizzou Data Miners
'''

import argparse
import os
import csv

import sys

def main(directory,columns):
  data = {}
#  for colname in columns:
#    data[colname] = []
    
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
          flag = 0    #not proud of this!!
          for colname,index in mapper.items():
            if(flag==1):
              gid = line[index]  ###
              data[gid] = []
              #print(index, flag, gid)
              flag = 0
            else:
              terms = line[index]
              #print(index, flag,terms)
              itemss = terms.split(';')
              flag = 1
          for item in itemss:
            #print(gid, item)
            if item:
              data[gid].append(item)    ##
            #print(data)
        fp.close()
###       data[colname] = list(set(data[colname]))
  print("Saving to files")
  fp = open("../data_csv/PI.unique.csv",'w')
  for key,array in data.items():
##    uniqueSet = set(array)
    for item in array:    ###
      fp.write("%s,%s\n" % (key,item))    ##
  fp.close()

if "__main__" == __name__:
  parser = argparse.ArgumentParser()
  parser.add_argument("directory")
  parser.add_argument("columns",type=str,nargs='+')
  args = parser.parse_args()
  main(args.directory,args.columns)