#! /home/franck/anaconda3/bin/python
import sys
import json
from collections import Counter
country_top_tags = dict()

for line in sys.stdin.readlines():

    country_code,tags = line.split("\t")
    tags_list = country_top_tags.get(country_code,Counter())
    tags_list.update(tags.strip().split(","))
    country_top_tags[country_code] = tags_list 

for key in country_top_tags:
    print(key+"\t"+ json.dumps(country_top_tags[key]))
