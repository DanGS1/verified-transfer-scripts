# Parse CSV, comparing and append to existing JSON
# Author: Akshar Amin
# Data: July 18th, 2019

import csv
import json


final_json = []

mexico_final_json = []
venezuela_final_json = []
brazil_final_json = []
uk_final_json = []

mexico_data = ["00000075062613","00000075010478","00000075023393","00000075029173","00000075061722","00000075066857"]
venezuela_data = ["00000075917265"]
brazil_data = ["00000078911222","00000078911239","00000078911246"]
uk_data = ["00000096138700"]

with open('O_PG_GS1 Mexico.json') as mexico_file:
    mexico_old_data = json.load(mexico_file)
with open('O_PG_GS1 Venezuela.json') as venezuela_file:
    venezuela_old_data = json.load(venezuela_file)
with open('O_PG_GS1 Brasil.json') as brazil_file:
    brazil_old_data = json.load(brazil_file)
with open('O_PG_GS1 UK.json') as uk_file:
    uk_old_data = json.load(uk_file)


def createJSON(gtin_list):
	if gtin in gtin_list:
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


		final_json.append({
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
	return final_json

with open('O_PG_GS1 US.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	next(csv_reader)
	for row in csv_reader:
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

		mexico_final_json = createJSON(mexico_data)
		venezuela_final_json = createJSON(venezuela_data)
		brazil_final_json = createJSON(brazil_data)
		uk_final_json = createJSON(uk_data)


		


mexico_data = mexico_old_data + mexico_final_json
venezuela_data = venezuela_old_data + venezuela_final_json
brazil_data = brazil_old_data + brazil_final_json
uk_data = uk_old_data + uk_final_json

with open('O_PG_GS1 Mexico1.json', 'w') as mexico_file_final:
    json.dump(mexico_data, mexico_file_final, indent=4, ensure_ascii=False)
with open('O_PG_GS1 Venezuela1.json', 'w') as venezuela_file_final:
    json.dump(venezuela_data, venezuela_file_final, indent=4, ensure_ascii=False)
with open('O_PG_GS1 Brasil1.json', 'w') as brazil_file_final:
    json.dump(brazil_data, brazil_file_final, indent=4, ensure_ascii=False)
with open('O_PG_GS1 UK1.json', 'w') as uk_file_final:
    json.dump(uk_data, uk_file_final, indent=4, ensure_ascii=False)
