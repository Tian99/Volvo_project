#Part description
#Comment field
import pandas as pd
import os
from pandas import ExcelWriter
from pandas import ExcelFile

def read():
	# Change the directory to whereever you store all the data
	address_data = "~/desktop/junior/coop/"
	file_claims = 'data/2019-12 Mack Claims.xlsx'
	file_location = 'data/Location.xlsx'

	pickle_claims = 'pickle/2019-12 Mack Claims.pkl'
	pickle_location = 'pickle/Location.pkl'

	#
	for fname in os.listdir('../pickle'):
		if fname.endswith('.pkl'):
			#Directly read in the pickle file
			df_claims = pd.read_pickle(address_data + pickle_claims)
			df_location = pd.read_pickle(address_data + pickle_location)

	#if the pickle not stored, store it, reduce tremendous runtime
	if not os.listdir("../pickle"):
		#Read the excel form and store them in pickle
		df_claims = pd.read_excel(address_data+file_claims)
		df_location = pd.read_excel(address_data+file_location)
		#Store all the files in pickle so that no need to read it every time
		df_claims.to_pickle(address_data+pickle_claims)
		df_location.to_pickle(address_data+pickle_location)

	return(df_claims, df_location)


def logic(x):
	#Wait to be cross-listed later
	if((x[0].isdigit() or x[1].isdigit()) and (x[2:4].isalpha()) and ((x[4:6]).isdigit() or x[4:7].isdigit())):
		return 1

	if(len(x) < 6):
		return 2

def normalize(df_claims, df_location):
	#Drop the unwanted number

	#Find the outliers
	df_claims_extra = df_claims[df_claims['Causal Part Number'].apply(lambda x: logic(x) == 1)]
	#Output the outliers to the output directory
	# df_claims_extra.to_excel('../data/output/outliers.xlsx')

	#Find the non-standard numbers
	df_claims_nons = df_claims[df_claims['Causal Part Number'].apply(lambda x: logic(x) == 2)]
	# df_claims_nons.to_excel('../data/output/non-standard.xlsx')

	#All the potential useful numbers
	df_claims = df_claims[df_claims['Causal Part Number'].apply(lambda x: x.isdigit())]
	df_location = df_location[df_location['PartNumber'].apply(lambda x: x.isdigit())]
	#Change the type to float to make things easier
	df_claims['Causal Part Number'] = df_claims['Causal Part Number'].astype(float)
	df_location['PartNumber'] = df_location['PartNumber'].astype(float)
	#Sort all the values in the dataframe
	df_claims = df_claims.sort_values(by =['Causal Part Number'])
	df_location = df_location.sort_values(by =['PartNumber'])

	# #Store the dataframe to excel so they are easy to be viewed.
	# df_claims.to_excel('../data/output/sorted_claim.xlsx')
	# df_location.to_excel('../data/output/sorted_location.xlsx')

	# exit()
	# print('Sorting and saving done')

	return df_claims, df_location, df_claims_extra, df_claims_nons

def merge(nor_claims, nor_location):
	#First Change the claim column name to PartNumber
	nor_claims = nor_claims.rename(columns = {'Causal Part Number': 'PartNumber'})

	#Starting to merge
	merged = pd.merge(nor_location, nor_claims, on = 'PartNumber')

	#See what the merged file looks like
	# merged.to_excel('../data/output/merged.xlsx')
	print('Merging successfully')
	print(len(merged.columns))
	print(len(nor_claims.columns))
	print(len(nor_location.columns))

	return merged

# df_claims, df_location = read()

# nor_claims, nor_location, df_claims_extra, df_claims_nons = normalize(df_claims, df_location)

# print(merge(nor_claims, nor_location))



###############################
#Function to read every single excel file from the directory
# os.chdir(address)

# # Create a list with all the files
# path = os.getcwd()
# files = os.listdir(path)

# #Select all the xlsx files in the directory for now

# excels = [e for e in files if "xlsx" in e]














