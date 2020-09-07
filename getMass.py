# A. Soylu 2020 // NEXT Project // VSI-RUG //
#
# the script to get value from the atomic mass table .
# https://www-nds.iaea.org/amdc/
# it needs fine tuned 'atomicMassData.csv'
#
import pandas as pd


df = pd.read_csv('atomicMassData.csv')


#print(df['AtomicMass'].head()) 


def getMass(N,Z):
	#s = df['N'].where((df['N'] == N )& (df['Z'] == Z))
	#s = df.loc[(df['N']==N) & df['Z']==Z]
	index = df.loc[(df['N']==N) & (df['Z']==Z)].index[0]
	
	#print(index) 
	print('Mass of {}-{} isotope : {}'.format( df['EL'][index], df['A'][index], df['AtomicMass'][index]))
	return df['AtomicMass'][index]

#getMass(126,77)