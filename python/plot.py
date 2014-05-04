'''
Plots data
'''

import csv

import numpy as np
from itertools import groupby
import matplotlib.pyplot as plt

import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('input',help="input file",type=argparse.FileType('r'))
	parser.add_argument('output',help="name of output image")
	parser.add_argument('-v','--vids',help="value column(s) to plot",type=int,nargs='+')
	parser.add_argument('-d','--delimiter',help="delimiter for file",default=',')
	parser.add_argument('-q','--quotechar',help="quote character for file",default='"')

	args = parser.parse_args()

	delimiter = args.delimiter
	if delimiter == r'\t':
		delimiter = '\t'
	quotechar = args.quotechar

	reader = csv.reader(args.input,delimiter=delimiter,quotechar=quotechar)

	alldata = []
	for row in reader:
		alldata.append(tuple(row))
	num_rows = len(alldata)
	num_cols = len(alldata[0])

	dtype = []
	for i in range(1,num_cols+1):
		if i in args.vids:
			dtype.append(('%s' % (i),'f8'))
		else:
			dtype.append(('%s' % (i),'S50'))

	dtype = np.dtype(dtype)
	
	alldata = np.array(alldata,dtype=dtype)

	datas = []
	for vid in args.vids:
		data = alldata['%s' % (vid)].tolist()
		data.sort(reverse=True)
		tmp = []
		cur = 1e20
		count = 0
		for row in data:
			if row < cur:
				tmp.append([row,count])
				cur = row
				count += 1
		datas.append(tmp)

	datas = np.array(datas)

	subplotids_base = 100*(len(args.vids))+20

	fig =  plt.figure('Data Plot',figsize=(16,9))
	for i in range(len(datas)):
		data = datas[i]
		subplotid = subplotids_base+i+1
		subplot = fig.add_subplot(subplotid)
		x = data[:,1]
		y = data[:,0]
		subplot.plot(x,y)
		subplotid = subplotids_base+i+2
		subplot = fig.add_subplot(subplotid)
		x = data[:,1]
		y = data[:,0]
		subplot.plot(x,y)
		subplot.set_xscale('log')
		subplot.set_yscale('log')
	plt.savefig("../imgs/%s.png" % (args.output), dpi=96, format='png')
	plt.show()


if __name__ == "__main__":
	main()