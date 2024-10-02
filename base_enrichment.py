# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:03:56 2024

@author: 52935
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--genome', help = 'input genome')
parser.add_argument('--outprefix', help = 'Prefix for output files')
parser.add_argument('--window', default = 10, help = 'window to be calculate')
parser.add_argument('--base', default = "T", help = 'base to calculate')
args = parser.parse_args()



with open(args.outprefix,'w') as o_file:
    with open(args.genome) as file:
        lines = file.readlines()
        Full_lines = []
        chr_line = ''
        for line in lines:
            if '>' in line:
                Full_lines.append(chr_line)
                Full_lines.append(line)
                chr_line = ''
            else:
                chr_line = chr_line+line.replace('\n','')
        Full_lines.append(chr_line)
        Full_lines=Full_lines[1:]
        
        window= args.window
        for seq in Full_lines:
            if '>' in seq:
                chro = seq.replace('>','').replace('\n', '')
                start = int(window/2)
            else:
                seq = seq.replace('\n', '')
                n = start + 1
                for base in range(int(window/2),len(seq)-int(window/2)):
                    sentence =chro+'\t'+ str(start) + '\t' + str(n)
                    key = seq[base-int(window/2):base+round(window/2)]
                    A_count = 0
                    max_gap = 0
                    gap = 0
                    p = ''
                    bonus = 0
                    for i in key:
                        if i == args.base:
                            if p == args.base:
                                bonus += 1
                            A_count = A_count + 1+bonus
                            if gap >= max_gap:
                                max_gap = gap
                            gap = 0
                        else:
                            gap = gap+1
                            bonus = 0
                        p = i
                    if gap >= max_gap:
                        max_gap = gap
                        
                    score = A_count - max_gap
                    if score < 0:
                        score = 0
                    sentence = sentence + '\t' +str(score) +'\n'
                    start +=1
                    n+=1
                    o_file.write(sentence)
                    
                    
