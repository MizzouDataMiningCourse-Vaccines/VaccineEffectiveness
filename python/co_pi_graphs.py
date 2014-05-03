'''
Takes in a Co_PIs table dump and creates
a directect and undirected graph input for
Snap Stanford library
'''

import argparse

def main(fp):
  Co_PIs = []
  for line in fp:
    [pi1,pi2] = line.strip().split('\t')
    Co_PIs.append([int(pi1),int(pi2)])
    
  PIs = []
  for [pi1,pi2] in Co_PIs:
    if pi1 not in PIs:
      PIs.append(pi1)
    if pi2 not in PIs:
      PIs.append(pi2)
      
  PI_map = {}
  for i in range(len(PIs)):
    PI_map[PIs[i]] = i
    
  pimap = open('../data_csv/PI_map.tsv','w')
  pimap.write('PI id\tIndex\n')
  for k,v in PI_map.items():
    pimap.write('%d\t%d\n' % (k,v))
  pimap.close()
  
  PI_directed_raw = {}
  PI_undirected_raw = {}
  
  for [pi1,pi2] in Co_PIs:
    pi1 = PI_map[pi1]
    pi2 = PI_map[pi2]
    if pi1 not in PI_undirected_raw.keys():
      PI_undirected_raw[pi1] = []
    if pi1 not in PI_directed_raw.keys():
      PI_directed_raw[pi1] = []
    if pi2 not in PI_directed_raw.keys():
      PI_directed_raw[pi2] = []
    PI_undirected_raw[pi1].append(pi2)
    PI_directed_raw[pi1].append(pi2)
    PI_directed_raw[pi2].append(pi1)
    
  PI_undirected_raw = sorted(PI_undirected_raw.items(), key = lambda x: x[0])
  PI_directed_raw = sorted(PI_directed_raw.items(), key = lambda x: x[0])
      
  undirected = open('../data_csv/PIs_undirected.tsv','w')
  for pi1,pis in PI_undirected_raw:
    pis = sorted(pis)
    for pi2 in pis:
      undirected.write('%d\t%d\n' % (pi1,pi2))
  undirected.close()
      
  directed = open('../data_csv/PIs_directed.tsv','w')
  PI_directed = []
  for pi1,pis in PI_directed_raw:
    for pi2 in pis:
      directed.write('%d\t%d\n' % (pi1,pi2))
  directed.close()
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('PIs',help='tsv containing PI and Co-PI ids',type=argparse.FileType('r'))
  
  args = parser.parse_args()
  
  main(args.PIs)