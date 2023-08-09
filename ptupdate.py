# PhishTank updater for piHole
#
# This script automatically download and parse the phising links
# on PhishTank and creates an updated file for piHole
#
# Note: This script is based on online-valid.xml PhishTank file
#
# Carles Figueras 2023
# v 0.3

import os
import wget

# Define url download site
url = 'http://data.phishtank.com/data/YOUR_PHISHTANK_KEY/online-valid.xml'

# Retrieving file
print('Downloading file from PhishTank...')
wget.download(url, 'online-valid.xml')

# Preparing files
file = open('online-valid.xml', 'r')
output = open('phising-hole.txt', 'w')

print('\n')
print('Extracting URLs...')
for line in file:
        if (line.find('<url>') != -1) and (line.find('?') == -1):
                if line.find('https') != -1:
                        inici = line.find('https')
                        final = line.find('</url>')
                        text = '0.0.0.0 ' + line[inici + 8:final - 1]
                        output.write(text)
                        i = i + 1
                        output.write('\n')
                elif line.find('http') != -1:
                        inici = line.find('http')
                        final = line.find('</url>')
                        text = '0.0.0.0 ' + line[inici + 7:final - 1]
                        output.write(text)
                        i = i + 1
                        output.write('\n')


print('Phishing URLs extracted: ', i)
# Closing files
file.close()
output.close()

# Deleting raw data
os.remove('online-valid.xml')
