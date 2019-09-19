# Parse CSV, comparing and removing data from JSON file
# Author: Yuang Li
# Data: July 18th, 2019


import csv
import json
from collections import OrderedDict

gtins = []

with open('products_to_compare.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        gtins.append(line[5])

    data = json.load(open('mo_products.json'), object_pairs_hook=OrderedDict)
    for gtin in gtins:
        for i in xrange(len(data)):
            if data[i]['gtin'] == gtin:
                del data[i]
                print('deleted...          gtin: ' + data[i]['gtin'])
                break

with open('result.json', 'w') as f:
    json.dump(data, f, sort_keys=False, indent=4)
