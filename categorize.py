
def analyze(merged):
	#First remove anything that is a storage area
	#Then merge based on the Vehicle model family
	
	#Remove the not-needed data(Anything with a DROP but not CAC, anything with a DS)
	# processed = merged[~merged.LocationId.str.contains("DROP") or merged.LocationId.str.contains('CAC')] #or ~merged.LocationId.str.contains('DS')]
	# processed.to_excel('../data/output/dropped.xlsx')
	print('Still Implementing')