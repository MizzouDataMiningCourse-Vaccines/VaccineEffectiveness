'''
Plot Grants vs Funding per Year
'''

import csv
import numpy as np
import matplotlib.pyplot as plt

reader = csv.reader(open('../gen_stats/funding_grants_per_year.tsv','r'),delimiter='\t')

data = []

for row in reader:
	data.append(row)

data = np.array(data)

fig = plt.figure('Funding and Grants per Year',figsize=(16,9))
sub = fig.add_subplot(111)
sub2 = sub.twinx()

subline = sub.plot(data[:,0],data[:,1],color='b')
subline2 = sub2.plot(data[:,0],data[:,2],color='g')

fig.legend((subline[0],subline2[0]),('Grants','Funding'))

plt.savefig('../imgs/Funding-Grants-per-Year.png',dpi=96,format='png')

plt.show()