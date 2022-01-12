import csv
from os import write
import pprint

with open('file_name.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['row1_item1', 'row1_item2'])
    writer.writerow(['row2_item1', 'row2_item2'])

with open('file_name.csv', 'r') as file:
    reader = csv.reader(file)
    park_list = list(reader)

pprint.pprint(park_list)
