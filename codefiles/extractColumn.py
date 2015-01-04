import csv
import io

def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]

filename = 'yelp_academic_dataset_business.csv'
reader = unicode_csv_reader(open(filename))
f = io.open('listOfCategories.txt', 'w')

for field in reader:
  print field[39]
  if "Restaurants" in field[39] :
    f.write(field[39])
    f.write(u'\n')  
