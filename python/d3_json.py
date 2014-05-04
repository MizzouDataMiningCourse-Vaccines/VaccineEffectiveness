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
import csv
import yaml

def main():
  fpj = open("../data_json/PIs.json","r")
  fpn = open("../data_json/newPIs.json","w")
  fpu = open("../gen_stats/co_pi_undirected_sorted.centrality.tab","r") # closeness(2), betweenness(3), NetworkConstraint(5), ClusteringCoefficient(6)
  fpd = open("../gen_stats/co_pi_directed_sorted.centrality.tab","r")  # page_rank(7)
  fpm = open("../data_csv/sorted_PI_map.tsv","r")  #PI_ID, Index
  fpp = open("../data_csv/funding_per_pi.tsv","r") #PI_ID, Total_Fund, Total_grant
  
  graph = yaml.load(fpj)
  nodes = graph["nodes"]
  lu = list(csv.reader(fpu, delimiter='\t'))
  ld = list(csv.reader(fpd, delimiter='\t'))
  lm = list(csv.reader(fpm, delimiter='\t'))
  lp = list(csv.reader(fpp, delimiter='\t'))
  #print(nodes)
  #print(len(ld))
  #print(len(lp))
  fund = {}
  grant = {}
  for i in range(len(lp)):
    fund[lp[i][0]] = lp[i][1]
    grant[lp[i][0]] = lp[i][2]
    
  for i in range(len(lm)):
    pid = lm[i][0]
    page = ld[i][7]
    #ppid = lp[i][]
    
    index = int(lu[i][0])
    close = float(lu[i][2])
    between = float(lu[i][3])
    network = float(lu[i][5])
    cluster = float(lu[i][6])
    tfund = int(fund[pid])
    tgrant = int(grant[pid])
    #print page
    
    nodes[index]['pid'] = pid
    nodes[index]['close'] = close
    nodes[index]['between'] = between
    nodes[index]['network'] = network
    nodes[index]['cluster'] = cluster
    nodes[index]['page'] = page
    nodes[index]['fund'] = tfund
    nodes[index]['grant'] = tgrant
    
  graph["nodes"] = nodes
  json.dump(graph, fpn)
  
  fpj.close()
  fpn.close()
  fpu.close()
  fpd.close()
  fpm.close()
  
'''
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
'''

if __name__ == '__main__':
  main()
'''
  parser = argparse.ArgumentParser()
  parser.add_argument('directed',help='directed PIs file',type=argparse.FileType('r'))
  parser.add_argument('mapper',help='PIs mapper file',type=argparse.FileType('r'))
  args = parser.parse_args()
'''