from general import read, normalize, merge
from categorize import analyze


#First merge the two excel files
df_claims, df_location = read()

nor_claims, nor_location, df_claims_extra, df_claims_nons = normalize(df_claims, df_location)

merged = merge(nor_claims, nor_location)

analyze(merged)





