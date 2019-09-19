# Parse CSV, comparing and create JSON
# Author: Akshar Amin
# Data: July 18th, 2019

import csv
import json

canada_file = open("O_PG_GS1 Canada.json", "w")

canada_list = []
us_list = []

canada_json = []

with open('O_PG_GS1 Canada.csv') as csv_canada:
	csv_reader_canada = csv.reader(csv_canada, delimiter=",")
	for row in csv_reader_canada:
		canada_gtin = row[5]
		canada_list.append(canada_gtin)



with open('O_PG_GS1 US.csv') as csv_us:
	csv_reader_us = csv.reader(csv_us, delimiter=",")
	next(csv_reader_us)
	for row in csv_reader_us:
		bn_0_l = row[0]
		bn_0_v = row[1]
		bn_1_l = row[2]
		bn_1_v = row[3]
		bn_2_l = row[4]
		bn_2_v = row[5]
		gpc = row[6]
		gtin = row[7]
		nc_0_m = row[8]
		nc_0_q = row[9]
		nc_1_m = row[10]
		nc_1_q = row[11]
		nc_2_m = row[12]
		nc_2_q = row[13]
		nc_3_m = row[14]
		nc_3_q = row[15]
		nc_4_m = row[16]
		nc_4_q = row[17]
		status = row[18]
		tmcc_0 = row[19]
		tmcc_1 = row[20]
		tmcc_2 = row[21]
		tid_0_l = row[22]
		tid_0_v = row[23]
		tid_1_l = row[24]
		tid_1_v = row[25]
		tid_2_l = row[26]
		tid_2_v = row[27]
		tiiu_0_l = row[28]
		tiiu_0_v = row[29]
		tiiu_1_l = row[30]
		tiiu_1_v = row[31]
		tiiu_2_l = row[32]
		tiiu_2_v = row[33]


		if gtin in canada_list:
			brand_name_list = []
			if bn_0_l != '':
				brand_name_list.append({
					"lang": bn_0_l,
					"value": bn_0_v
					})
			if bn_1_l != '':
				brand_name_list.append({
					"lang": bn_1_l,
					"value": bn_1_v
					})
			if bn_2_l != '':
				brand_name_list.append({
					"lang": bn_2_l,
					"value": bn_2_v
					})
			
			tmcc_list = []
			if tmcc_0 != '':
				tmcc_list.append(tmcc_0)
			if tmcc_1 != '':
				tmcc_list.append(tmcc_1)
			if tmcc_2 != '':
				tmcc_list.append(tmcc_2)

			tid_list = []
			if tid_0_l != '':
				tid_list.append({
					"lang": tid_0_l,
					"value": tid_0_v
					})
			if tid_1_l != '':
				tid_list.append({
					"lang": tid_1_l,
					"value": tid_1_v
					})
			if tid_2_l != '':
				tid_list.append({
					"lang": tid_2_l,
					"value": tid_2_v
					})

			tiiu_list = []
			if tiiu_0_l != '':
				tiiu_list.append({
					"lang": tiiu_0_l,
					"value": tiiu_0_v
					})
			if tiiu_1_l != '':
				tiiu_list.append({
					"lang": tiiu_1_l,
					"value": tiiu_1_v
					})
			if tiiu_2_l != '':
				tiiu_list.append({
					"lang": tiiu_2_l,
					"value": tiiu_2_v
					})

			nc_list = []
			if nc_0_m != '':
				nc_list.append({
					"quantity": float(nc_0_q),
					"measurementUnitCode": nc_0_m
					})
			if nc_1_m != '':
				nc_list.append({
					"quantity": float(nc_1_q),
					"measurementUnitCode": nc_1_m
					})
			if nc_2_m != '':
				nc_list.append({
					"quantity": float(nc_2_q),
					"measurementUnitCode": nc_2_m
					})
			if nc_3_m != '':
				nc_list.append({
					"quantity": float(nc_3_q),
					"measurementUnitCode": nc_3_m
					})
			if nc_4_m != '':
				nc_list.append({
					"quantity": float(nc_4_q),
					"measurementUnitCode": nc_4_m
					})


			canada_json.append({
			 "gtin": gtin,
			 "status": status,
			 "brandName": brand_name_list,
			 "gpcCode": gpc,
			 "targetMarketCountryCode": tmcc_list,
			 "tradeItemDescription": tid_list,
			 "tradeItemImageUrl": tiiu_list,
			 "netContent": nc_list
			})
			brand_name_list = []
			tmcc_list = []
			tid_list = []
			tiiu_list = []
			nc_list = []

	canada_file.write(json.dumps(canada_json, indent=4, ensure_ascii=False))

			

