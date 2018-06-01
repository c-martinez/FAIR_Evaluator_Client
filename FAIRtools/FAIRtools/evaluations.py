#-*- coding: utf-8 -*-
#!/usr/bin/env python


link = 'http://linkeddata.systems:3000'
base_link = 'https://purl.org/fair-metrics/'
from .showup import showup
import urllib2
import json
import requests


def evaluations():
    req = urllib2.urlopen(link+'/evaluations.json')
    principle = raw_input("Choose your evaluations id : (Ex. 2, 4 or all)")
    if "all" in principle:
        showup(req)
    else:
        json_off = json.load(req)
        for i in json_off:
            if principle == str(i["id"]):
                for m in i:
                    if type(i[m]) == list:
                        showin(i[m])
                    else:
                        i[m] = str(i[m])
                        print ("\t%s:  %s")%(m, i[m])
                print "\n"
            else:
                continue