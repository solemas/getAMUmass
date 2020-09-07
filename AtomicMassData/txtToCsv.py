import numpy as np
import scipy
import pandas as pd
from pandas import *
import matplotlib.pyplot as plt
import colorpy
import fileinput
from sys import exit
# fig.write_html('first_figure.html', auto_open=True)

def replaceStr(text,index=0,replacement=''):                           #nth Character Replacement Function
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

filename = 'takeThis.txt'   #Source file
outFileName = 'AtomicMass.csv'  #outfile

outFile = open(outFileName, "w")

with fileinput.FileInput("takeThis.txt") as file:
    for line in file:
    	tempLine = str(line)
    #	print(type(tempLine))
    	aa = replaceStr(tempLine,5,';')
    #	print(aa)
    	aa = replaceStr(aa,11,';')
    #	print(aa)
    	aa = replaceStr(aa,15,';')
    #	print(aa)
    	aa = replaceStr(aa,19,';')
    #	print(aa)
    	aa = replaceStr(aa,22,';')
    #	print(aa)
    	aa = replaceStr(aa,28,';')
    #	print(aa)
    	aa = replaceStr(aa,42,';')
    #	print(aa)
    	aa = replaceStr(aa,72,';')
    #	print(aa)
    	aa = replaceStr(aa,95,';')
    #	print(aa)
    	aa = replaceStr(aa,111,';')
    	print(aa)
    	outFile.write(aa)


    #	exit()

    	#print(tempLine)    		 #   print(line.replace(checkThis, 'LOL\n\n\n\n {}'.format(checkThis)), end='')