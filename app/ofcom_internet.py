import pandas as pd
import json, base64

def find_with_postcode(internet, columns, postcodes):
	pc_col = {}
	col_data = {}
	pc = postcodes['Postcode']
	for col in columns:
		data = internet[internet['postcode'] == pc][col].item()
		col_data[col] = data
	pc_col[pc] = col_data
	return pc_col

def run(encoded_json, internet_columns, df_internet):
	postcodes = json.loads(base64.b64decode(encoded_json).decode('utf-8'))

	df_internet.drop(df_internet.filter(regex="Unname"),axis=1, inplace=True)
	return find_with_postcode(df_internet,internet_columns,postcodes)




