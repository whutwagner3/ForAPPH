#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:48:21 2019
@author: willhutwagner
"""

import sys
from bokeh.plotting import figure,output_file,show
from bokeh.palettes import viridis
from mpldatacursor import datacursor

txt = sys.argv[1]
eigenvec = sys.argv[2]
outfile = sys.argv[3]

Breeds={}
convert={}
with open(txt) as fi:
    for line in fi:
        text=line.split(None,1)
        convert[text[0]]=text[1]
        if text[1] not in Breeds:
            Breeds[text[1]]=[[],[]]


with open(eigenvec) as fi:
    fi.readline()
    for line in fi:
        text=line.split()
        if text[1] in convert:
            Breeds[convert[text[1]]][0].append(float(text[3]))
            Breeds[convert[text[1]]][1].append(float(text[4]))
        
p=figure(plot_width = 1000,plot_height = 800)
p.title.text = 'Click on legend entries to hide their data'
colors=viridis(len(Breeds))
index=0

for key in Breeds:
    cir = p.circle(Breeds[key][0],Breeds[key][1], size=3,legend=key,color=colors[index])
    index+=1
    datacursor(fomatter=key)
    

p.legend.location="bottom_right"
p.legend.click_policy="hide"
output_file(outfile,title="iteractive legend")
show(p)
