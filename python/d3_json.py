'''
Generates D3 json files from PIs_directed and PI_map files

JSON format:
{
  'nodes' : [ {'id':pid'}...],
  'links' : [ {'source':index,'target':index}...]
}
'''

import argparse
import json

def main(pis_directed,pis_mapper):
  out = {}
  out['nodes'] = []
  out['links'] = []

  pis = []
  pis_mapper.readline() # remove header
  for line in pis_mapper:
    [pid,index] = line.strip().split('\t')
    pis.append([int(pid),int(index)])
    
  pis = sorted(pis, key=lambda x: x[1])
  for pi in pis:
    out['nodes'].append({'pid':pi[0]})
  
  links = []
  for line in pis_directed:
    [p1,p2] = line.strip().split('\t')
    out['links'].append({'source':int(p1),'target':int(p2)})
  
  outfile = open('../data_json/PIs.json','w')
  json.dump(out,outfile)
  outfile.close()
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('directed',help='directed PIs file',type=argparse.FileType('r'))
  parser.add_argument('mapper',help='PIs mapper file',type=argparse.FileType('r'))
  args = parser.parse_args()
  
  main(args.directed,args.mapper)