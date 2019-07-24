#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:34:42 2019

@author: willhutwagner
"""

import sys
import subprocess

inp = sys.argv[1]
out = sys.argv[2]

popular = ['Beagle','Boxer','Collie','German Shepherd Dog', 'Golden Retriever','Labrador Retriever', 'Pug','Poodle']
keep = ''
keep2 = ''
keep3 = ''
keep4 = ''
count={'Beagle':0,'Boxer':0,'Collie':0,'German Shepherd Dog':0, 'Golden Retriever':0,'Labrador Retriever':0, 'Pug':0,'Poodle':0}
with open(inp+'.txt')as fi:
    for line in fi:
        text = line.strip().split(None,1)
        if text[1] in popular:
            keep+=text[0]+'\n'
            keep2+=line
            count[text[1]]+=1
            if count[text[1]]<25:
                keep3+=text[0]+'\n'
                keep4+=line
with open('keeping.txt','w')as fi:
    fi.write(keep)
with open('pop_breedandid.txt','w') as fi:
    fi.write(keep2)
with open('keeping_25.txt','w')as fi:
    fi.write(keep3)
with open('25_breedandid.txt','w')as fi:
    fi.write(keep4)

subprocess.call(["../plink","--bfile",inp, "--keep-fam", "keeping.txt","--make-bed", "--out",out,"--dog"])
subprocess.call(["../plink","--bfile",inp, "--keep-fam", "keeping_25.txt","--make-bed", "--out",out+"_25","--dog"])
subprocess.call(["../plink","--bfile",out, "--genome","--noweb", "--dog", "--out", out])
subprocess.call(["../plink","--bfile",out+"_25", "--genome","--noweb", "--dog", "--out", out+"_25"])



    