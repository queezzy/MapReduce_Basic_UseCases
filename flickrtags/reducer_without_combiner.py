#! /home/franck/anaconda3/bin/python
import sys
from collections import Counter

K = 100
if len(sys.argv)>1:
    K = int(sys.argv[1])
    
country_top_tags = dict()
line = sys.stdin.readline()

while line :
    
    country_code,tags = line.split("\t")
    if country_code not in country_top_tags.keys():
        country_top_tags[country_code] = Counter()
    country_top_tags[country_code].update(tags.strip().split(","))
    line = sys.stdin.readline()

for key in country_top_tags:
    for tag,value in country_top_tags[key].most_common(K):
        print("%s\t%s\t%d"%(key,tag,value))
