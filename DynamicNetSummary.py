# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import pandas as pd
import os
path = "D:\User_Documents\Dowd_Michael\Python\\\netOutputs_SC2_2030_4ft_Variable.PRN"

#Fixed
baseFixed = ["D:\User_Documents\Dowd_Michael\Python\\netOutputs_Year 2010.PRN",
             "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SLR1_Fixed.PRN",
             "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SLR2_Fixed.PRN",
             "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SLR3_Fixed.PRN",
             "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SLR4_Fixed.PRN",
             "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SLR5_Fixed.PRN",
             "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SLR6_Fixed.PRN"]

baseVariable = ["D:\User_Documents\Dowd_Michael\Python\\netOutputs_Year 2010.PRN",
                "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SLR2_Variable.PRN",
                "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SLR1_Variable.PRN",
                "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SLR3_Variable.PRN",
                "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SLR4_Variable.PRN",
                "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SLR5_Variable.PRN",
                "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SLR6_Variable.PRN"]

Scenario1Fixed = ["D:\User_Documents\Dowd_Michael\Python\\netOutputs_Sc1_2030.PRN",
                  "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SC1_2030_4ft_Fixed.PRN",
                  "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SC1_2030_NOBUS.PRN",
                  "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SC1_2030_NOBUS_4ft_Fixed.PRN",
                  "D:\User_Documents\Dowd_Michael\Python\\netOutputs_Sc1_2030_OuterBus.PRN",
                  "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SC1_2030_OuterBus_4ft_Fixed.PRN"]

Scenario1Variable = ["D:\User_Documents\Dowd_Michael\Python\\netOutputs_Sc1_2030.PRN",
                     "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SC1_2030_4ft_Variable.PRN",
                     "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SC1_2030_NOBUS.PRN",
                     "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SC1_2030_NOBUS_4ft_Variable.PRN",
                     "D:\User_Documents\Dowd_Michael\Python\\netOutputs_Sc1_2030_OuterBus.PRN",
                     "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SC1_2030_OuterBus_4ft_Variable.PRN"]

Scenario2Fixed = ["D:\User_Documents\Dowd_Michael\Python\\netOutputs_Sc2_2030.PRN",
                  "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SC2_2030_4ft_Fixed.PRN",
                  "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SC2_2030_NOBUS.PRN",
                  "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SC2_2030_NOBUS_4ft_Fixed.PRN",
                  "D:\User_Documents\Dowd_Michael\Python\\netOutputs_Sc2_2030_OuterBus.PRN",
                  "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SC2_2030_OuterBus_4ft_Fixed.PRN"]

Scenario2Variable = ["D:\User_Documents\Dowd_Michael\Python\\netOutputs_Sc2_2030.PRN",
                     "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SC2_2030_4ft_Variable.PRN",
                     "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SC2_2030_NOBUS.PRN",
                     "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SC2_2030_NOBUS_4ft_Variable.PRN",
                     "D:\User_Documents\Dowd_Michael\Python\\netOutputs_Sc2_2030_OuterBus.PRN",
                     "D:\User_Documents\Dowd_Michael\Python\\netOutputs_SC2_2030_OuterBus_4ft_Variable.PRN"]
                        
def dynamicSummary(path, scenario=False):
    """ 
    Takes in one Lost Trip File and Calcualtes the Reduction from the baseline totals    
    """
    with open(path, 'r') as f:
       lines = f.readlines()
    print lines
    if not scenario:
        slr_lvl = path.split("_")[-1]
    else:
        slr_lvl = path.split("\\")[-2]
    
    splitLines = []
    start_index =0;
    
    linkPhase = False
    begin = "Variable"
    for index, line in enumerate(lines):
        if (line == 'Begin PROCESS PHASE LINKMERGE\n'):
            linkPhase = True
            print "TRUE"
        if linkPhase and (line[0:8] == begin):
            print "Success", index
            start_index = index
            break
    
    if start_index == 0:
        print "Error"
        return lines
    #Header holds triple tuple (start, len, length)
    header = {
        "Variable": {"loc":0,"end":0, "start":0},
            "Obs<>0":  {"loc":0,"end":0, "start":0},
                "Total":  {"loc":0,"end":0, "start":0},
                    "Ave":  {"loc":0,"end":0, "start":0},
                        "Min":  {"loc":0,"end":0, "start":0},
                            "Max":  {"loc":0,"end":0, "start":0},
                                "RMS":  {"loc":0,"end":0, "start":0}
    }
    order = ["Variable","Obs<>0","Total","Ave","Min","Max","RMS"]

    for key in header.keys():
        if key == "Obs<>0":
             header[key]["loc"] = 18
             header[key]["end"] = header[key]["loc"] + len(key)
        if key == "Variable":
            header[key]["end"] = 17
            header[key]["loc"] = 0            
        else:
            print key, start_index
            header[key]["loc"] = lines[start_index].index(key)
            header[key]["end"] = header[key]["loc"] + len(key)
        
    for index, key in enumerate(order):
        if key == "Variable" or key == "Obs<>0":
           header[key]["start"] = header[key]["loc"]
        else:
           header[key]["start"] = header[order[index-1]]["end"]
           
    def tryConvert(arg):
        try:
            float(arg)
        except:
            pass
        return arg
    
    splitLines = []
    lines = lines[start_index+2:len(lines)]
    for line in lines:
        if line[0] not in [" ","-"] and "Massachusetts Institute of Technology (MIT)" not in line \
        and "Voyager" not in line:
            Variable = line[header["Variable"]["start"]:header["Variable"]["end"]].replace(",","")
            Obs = line[header["Obs<>0"]["start"]:header["Obs<>0"]["end"]].replace(",","")
            Total = line[header["Total"]["start"]:header["Total"]["end"]].replace(",","")
            Ave = line[header["Ave"]["start"]:header["Ave"]["end"]].replace(",","")
            Min = line[header["Min"]["start"]:header["Min"]["end"]].replace(",","")
            Max = line[header["Max"]["start"]:header["Max"]["end"]].replace(",","")
            Variable 	= tryConvert("".join(Variable.split()))
            Obs 		= tryConvert(" ".join(Obs.split()))	 
            Total 	= tryConvert(" ".join(Total.split()))
            Ave 		= tryConvert(" ".join(Ave.split()))
            Min 		= tryConvert(" ".join(Min.split()))
            Max 		= tryConvert(" ".join(Max.split()))
            
         
            
            
            
        if len(" ".join(line.split())) > 0:
            splitLines.append([Variable,Obs,Total,Ave,Min,Max])
        else:
            break
            
    df = pd.DataFrame(splitLines)
    df.columns = order[0:6]
    return df
    
    
    
#        line = line.replace(":", " ")
#        line = line.replace(",", "")
#        splitLine = " ".join(line.split())
#        #Below checks if the line is an MI or an MO
#        if (splitLine[0:2] == "MI" or splitLine[0:2] == "MW"):
#            #Below skips the travel time matrices that are MI's
#            if ((splitLine[0:2] == "MI") and (int(splitLine[3:5]) < 13)) or (splitLine[0:2] == "MW"):
#                info = splitLine.split(" ")
#                #Remove thousands commas
#                print info
#                #NHBW/NHBO Always have Zero for PTDRIVE
#                #Below Controls for that
#                try: 
#                    float(info[1])
#                    #Convert the trips to a number with the float()
#                    splitLines.append([info[0], float(info[1])])
#                except ValueError:
#                    print info[0], info[1]
#                    splitLines.append([info[0], 0])
#            
#    #I know this number of trip purposes will always be the same
#    #so that is why I am using number 40 instead of a dynamic number
#
#    original            = pd.DataFrame(splitLines[0:42])
#    new                 = pd.DataFrame(splitLines[42:len(splitLines)])
#
#    original.columns    = ["Input", "BaseTotal"]
#    new.columns         = ["Output","NewTot_"+ slr_lvl]
#    df = pd.merge(original, new, left_index=True, right_index=True, how='outer')
#    df["Lost_"+ slr_lvl] = df.BaseTotal - df["NewTot_"+slr_lvl]
#    df["LostPerc" + slr_lvl] = df["Lost_"+slr_lvl] / df.BaseTotal
#    return df    
    