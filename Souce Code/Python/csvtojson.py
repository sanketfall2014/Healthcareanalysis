
import csv
import json

csvfile = open('tweepy.csv', 'r')
jsonfile = open('out.json', 'w')

fieldnames = ("Tweet","Created_Date")
reader = csv.DictReader( csvfile, fieldnames)

for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')