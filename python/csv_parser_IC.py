'''
(c) Mizzou Data Miners
'''

import argparse
import os
import csv

import sys

def main(directory,columns):
  data = {}
  uniqueIC = set()
  bs = chr(92)
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
            if(flag==0):
              gid = line[index]  ###
              uniqueIC.add(gid)
              #data[gid] = []
              #print(index, flag, gid)
              flag = 1
            else:
              terms = line[index]
              #print(index, flag,terms)
              itemss = terms.split(chr(92))
              #if(len(itemss)>1):
              if(terms.count(chr(92))>1):
                print(itemss)
              for items in itemss:
                IC = items.split(':')
                uniqueIC.add(IC[0])
              flag = 0
          #for item in itemss:
            #print(gid, item)
          #  if item:
          #    data[gid].append(item)    ##
            #print(data)
        fp.close()
###       data[colname] = list(set(data[colname]))
  print("Saving to files")
  fp = open("../data_csv/IC.unique.csv",'w')
  for key in uniqueIC:    ##
    fp.write("%s\n" % (key))    ##
##    uniqueSet = set(array)
##    for item in array:    ###
  fp.close()

if "__main__" == __name__:
  parser = argparse.ArgumentParser()
  parser.add_argument("directory")
  parser.add_argument("columns",type=str,nargs='+')
  args = parser.parse_args()
  main(args.directory,args.columns)