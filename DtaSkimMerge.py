# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:30:25 2015

@author: mdowd
"""
import os
import pandas as pd
import numpy as np
path = "/Users/mdowd/MIT/MIT_Fall2014/Thesis/Analysis/ProductionWork/Accessiblity_Work/Skims/March/March29Skims"
theFiles = os.listdir(path)[1:]
levels = {"base":[],"1ft":[],"2ft":[],"3ft":[],"4ft":[],"5ft":[],"6ft":[]}
outpath = "/Users/mdowd/MIT/MIT_Fall2014/Thesis/Analysis/ProductionWork/Accessiblity_Work/Skims/March/mergedAuto" 

for key in levels.keys():
    for a_file in theFiles:
        temp = a_file.split(".")[0].split("_")[1]
        if key == temp:
            levels[key].append(a_file)
            
for skimSet in levels.iteritems(): 
    print "working on", skimSet[0]
    #Static df to Matrix
    static = pd.read_csv(path + "/" + skimSet[1][0])
    static.index = static[static.columns[0]]
    amtime = static[static.columns[0]]
    static = static.drop(static.columns[0], axis=1)
    staticMat = static.as_matrix()

    #DTA df to Matrix
    dta = pd.read_csv(path + "/" + skimSet[1][1])
    dta.index = dta[dta.columns[0]]
    dta = dta.drop(dta.columns[0], axis=1)
    dtaMat = dta.as_matrix()

    staticMat[0:0+dtaMat.shape[0], 0:0+dtaMat.shape[1]] = dtaMat
    zeroMask = staticMat == 0
    staticMat[zeroMask] = 9999

    out_df = pd.DataFrame(staticMat, columns = [i for i in xrange(1,len(staticMat)+1)], index = [i for i in xrange(1,len(staticMat)+1)])
    out_df.to_csv(outpath + "/" + "DtaMerge_"+ skimSet[0]+".csv")    
    
print "Complete"