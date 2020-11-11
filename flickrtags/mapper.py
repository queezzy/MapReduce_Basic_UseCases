#! /home/franck/anaconda3/bin/python

import sys,os
import country


country.init_pays()

for line in sys.stdin.readlines():
    
    
    content = line.split("\t")
    if len(content)<23:
        continue
    try:
        longitude = float(content[10])
        latitude = float(content[11])
    except ValueError:
        continue
    
    user_tags = content[8].strip()

    country_code = country.getCountryAt(latitude,longitude)

    if country_code:
        print(country_code+"\t"+user_tags)