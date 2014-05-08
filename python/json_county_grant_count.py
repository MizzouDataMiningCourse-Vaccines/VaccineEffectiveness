'''
Takes in a Co_PIs table dump and creates
a directect and undirected graph input for
Snap Stanford library
'''

import argparse


fp = open("../data_csv/grants_per_countycode.tsv","r")
fp1 = open("../data_json/county_count.json","w")
county_count = []
max = 1
sum = 1
for line in fp:
  [cy,c] = line.strip().split('\t')
  county_count.append([str(cy),int(c)])
  if int(c) > max:
    max = int(c)
    sum += int(c)
parts = "{"
for cc in county_count:
  normCount = round(float(cc[1])/sum * len(county_count) + .2, 1)
  parts +='"'+cc[0]+'":'+str(normCount)+','
parts = parts[:-1]+"}"
fp1.write(parts)
