#! /home/franck/anaconda3/bin/python
import sys, json
from collections import Counter

K = 100
if(len(sys.argv)>1):
    K = int(sys.argv[1])
    
country_top_tags = dict()

for line in sys.stdin.readlines():

    country_code,tags = line.split("\t")
    tags = json.loads(tags)
    if country_code not in country_top_tags:
        country_top_tags[country_code]=Counter()
    country_top_tags[country_code].update(tags)

for key in country_top_tags:
    for tag,value in country_top_tags[key].most_common(K):
        print("%s\t%s\t%d"%(key,tag,value))
