#Daniel Rodriguez
#8/28/2019
#Remove all GTIN's in America's if they are in Canada file



import csv

# empty list that will be filled with all GTIN's in canada file
gtinCanada = []

# Python without extra modules can only write in csv's
# These are all seperate csv's that correlate to a sheet in the real xlsx files
f =  open('usNewData.csv', 'w')
netContent =  open('usNetContent.csv', 'w')
targetMarketCountryCode =  open('targetMarketCountryCode.csv', 'w')
tradeItemDescription =  open('tradeItemDescription.csv', 'w')
tradeItemUrl =  open('tradeItemImageUrl.csv', 'w')
brandName =  open('brandName.csv', 'w')
gtin =  open('gtin.csv', 'w')


# All gtin's in Canada file were put in a csv and call gtinCanada.csv
with open('gtinCanada.csv') as csv_file1:
    csv_reader = csv.reader(csv_file1, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
            gtinCanada.append(row[-1])
# All gtin's are now in the list gtinCanada
# print(gtinCanada)


# US all Flattened sheet in the US xlsx was placed in its own csv
with open('usFlattenedData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        # if gtin in usFlattenedData.csv is not in gtinCanada write entire row in usNewData.csv
        if row[7] not in gtinCanada:
            for i in range(len(row)):
                f.write(row[i]+',')
            f.write('\n')


# all following code is only running if gtin is not in GTIN Canada
# Gtin
            gtin.write(row[7]+','+row[6]+','+row[7][1:4] +'\n')


# if statements are to ensure products with multiple elements are written in csv's properly

# Country code
            if row[21] == '' and row[20] != '':
                targetMarketCountryCode.write(row[7]+','+row[19]+'\n')
                targetMarketCountryCode.write(row[7]+','+row[20]+'\n')
            elif row[20]=='':
                targetMarketCountryCode.write(row[7]+','+row[19]+'\n')
            elif row[21] != '':
                targetMarketCountryCode.write(row[7]+','+row[19]+'\n')
                targetMarketCountryCode.write(row[7]+','+row[20]+'\n') 
                targetMarketCountryCode.write(row[7]+','+row[21]+'\n')


# Image Url's
            if row[28]=='':
                continue
            elif row[33] == '' and row[31] != '':
                tradeItemUrl.write(row[7]+','+row[28]+','+row[29]+'\n')
                tradeItemUrl.write(row[7]+','+row[30]+','+row[31]+'\n')
            elif row[31]=='':
                tradeItemUrl.write(row[7]+','+row[28]+','+row[29]+'\n')
            elif row[33] != '':
                tradeItemUrl.write(row[7]+','+row[28]+','+row[29]+'\n')
                tradeItemUrl.write(row[7]+','+row[30]+','+row[31]+'\n')
                tradeItemUrl.write(row[7]+','+row[32]+','+row[33]+'\n')


# NetContent
            if row[8]=='':
                continue
            elif row[17] != '':
                netContent.write(row[7]+','+row[8]+','+row[9]+'\n')
                netContent.write(row[7]+','+row[10]+','+row[11]+'\n')
                netContent.write(row[7]+','+row[12]+','+row[13]+'\n')
                netContent.write(row[7]+','+row[14]+','+row[15]+'\n')
                netContent.write(row[7]+','+row[16]+','+row[17]+'\n')
            elif row[15] != '':
                netContent.write(row[7]+','+row[8]+','+row[9]+'\n')
                netContent.write(row[7]+','+row[10]+','+row[11]+'\n')
                netContent.write(row[7]+','+row[12]+','+row[13]+'\n')
                netContent.write(row[7]+','+row[14]+','+row[15]+'\n')
            elif row[13] != '':
                netContent.write(row[7]+','+row[8]+','+row[9]+'\n')
                netContent.write(row[7]+','+row[10]+','+row[11]+'\n')
                netContent.write(row[7]+','+row[12]+','+row[13]+'\n')
            elif row[11] != '':
                netContent.write(row[7]+','+row[8]+','+row[9]+'\n')
                netContent.write(row[7]+','+row[10]+','+row[11]+'\n')
            elif row[9] != '':
                netContent.write(row[7]+','+row[8]+','+row[9]+'\n')

# brandName
            if row[0]=='':
                continue
            elif row[5] == '' and row[3] != '':
                brandName.write(row[7]+','+row[0]+','+row[1]+'\n')
                brandName.write(row[7]+','+row[2]+','+row[3]+'\n')
            elif row[3]=='':
                brandName.write(row[7]+','+row[0]+','+row[1]+'\n')
            elif row[5] != '':
                brandName.write(row[7]+','+row[0]+','+row[1]+'\n')
                brandName.write(row[7]+','+row[2]+','+row[3]+'\n')
                brandName.write(row[7]+','+row[4]+','+row[5]+'\n')


# Item Description
            if row[0]=='':
                continue
            elif row[27] == '' and row[25] != '':
                tradeItemDescription.write(row[7]+','+row[22]+','+row[23]+'\n')
                tradeItemDescription.write(row[7]+','+row[24]+','+row[25]+'\n')
            elif row[25]=='':
                tradeItemDescription.write(row[7]+','+row[22]+','+row[23]+'\n')
            elif row[27] != '':
                tradeItemDescription.write(row[7]+','+row[22]+','+row[23]+'\n')
                tradeItemDescription.write(row[7]+','+row[24]+','+row[25]+'\n')
                tradeItemDescription.write(row[7]+','+row[26]+','+row[27]+'\n')

# ---------------README--------------
# once code is complete all csv's must be converted to UTF-8 because excel does not default to utf-8
# this means all special non-english characters will be changed
# then all csv's must be copied and pasted into seperate sheets in a xslx to keep formatt of origanl documents
# SUGGESTION --- use this code to help properly write a script that allows writing in xlsx files
# -------------- this will avoid copying errors and be much more time effceint