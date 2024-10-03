# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:33:33 2024

@author: 52935
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--region', help = 'input region file in bed format')
parser.add_argument('--output', help = 'output files')
parser.add_argument('--ref', help = 'reference score file')
parser.add_argument('--window', default = 30, help = 'window to be calculate')
parser.add_argument('--filter', default = 10, help = 'lowest score to be consider as T_boundaries')
args = parser.parse_args()

signal = {}
with open(args.ref) as file:
    lines = file.readlines()
    for line in lines:
        sen = line.split('\t')
        Chr = sen[0]
        key1 = int(sen[1])
        score = int(sen[3].replace('\n', ''))
        if Chr not in signal:
            signal[Chr] = {}
        signal[Chr][key1] = score
        
with open(args.output,'w') as o_file:
    with open(args.region) as in_file:
        lines = in_file.readlines()
        for line in lines:
            sen = line.split('\t')
            Chr = sen[0]
            key1 = int(sen[1])
            key2 = int(sen[2])
            T_B = False
            for i in range(key1-args.window,key1+args.window):
                try:
                    if signal[Chr][i] >= args.filter:
                        T_B = True
                except:
                    pass
            for j in range(key2-args.window,key2+args.window):
                try:
                    if signal[Chr][j] >= args.filter:
                        T_B = True
                except:
                    pass               
            if T_B:    
                o_file.write(line.replace('\n','') + '\t' + 'True' +'\n' )
            else:
                o_file.write(line.replace('\n','') + '\t' + 'count' +'\n' )