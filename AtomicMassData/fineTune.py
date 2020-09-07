import numpy as np
import scipy
import pandas as pd
from pandas import *
import matplotlib.pyplot as plt
import colorpy
import fileinput
from sys import exit
# fig.write_html('first_figure.html', auto_open=True)

def replaceStr(text,index=0,replacement=''):                            # nth Character Replacement Function
    return '%s%s%s'%(text[:index],replacement,text[index+1:])           # %string %string %string

filename = 'AtomicMass1.csv'   #Source file
outFileName = 'AtomicMass.csv'  #outfile

file = pd.read_csv(filename,delimiter=';')

tempFile = file

#print(file['N'])

i = 0 
for value in file['AtomicMass']:
    if value[3]==' ':
        value = replaceStr(value,3,'.')
    if value[10]=='.' or value[10]=='#':
        value = replaceStr(value,10,'')
    while True:
        if value[0]==' ':

            value = replaceStr(value,0,'')

        else:
            break
    #file.replace(to_replace = file['AtomicMass'][i],value)
  #  print(file['AtomicMass'][i])
    print(value)
    tempFile['AtomicMass'] = tempFile['AtomicMass'].replace(tempFile['AtomicMass'][i],float(value))
    print(tempFile['AtomicMass'][i])
    i = i+1
 #   print(i)

print(tempFile['AtomicMass'].head())

file.to_csv("atomicMassData.csv", index=False)

  #  print(value)







#        txtToCsv.py 
"""
withleinput.FileInput("takeThis.txt") as file:
    for line in file:
        tempLine = str(line)
    #   print(type(tempLine))
        aa = replaceStr(tempLine,5,';')
    #   print(aa)
        aa = replaceStr(aa,11,';')
    #   print(aa)
        aa = replaceStr(aa,15,';')
    #   print(aa)
        aa = replaceStr(aa,19,';')
    #   print(aa)
        aa = replaceStr(aa,22,';')
    #   print(aa)
        aa = replaceStr(aa,28,';')
    #   print(aa)
        aa = replaceStr(aa,42,';')
    #   print(aa)
        aa = replaceStr(aa,72,';')
    #   print(aa)
        aa = replaceStr(aa,95,';')
    #   print(aa)
        aa = replaceStr(aa,111,';')
        print(aa)
        outFile.write(aa)


    #   exit()

        #print(tempLine)             #   print(line.replace(checkThis, 'LOL\n\n\n\n {}'.format(checkThis)), end='')
"""
