from nltk import WordNetLemmatizer
from nltk import word_tokenize,pos_tag
import csv
import sys
import codecs

def csv_reader(file_obj):
	csv.field_size_limit(sys.maxsize)
	reader = csv.reader(file_obj)
	wnl = WordNetLemmatizer()
	final = []
	lem = []
	i = 0
	for row in reader:
		rowstr = row[0].decode('utf-8',errors='ignore')
		lem = [wnl.lemmatize(word)for word in rowstr.split(" ")]
	file2 = open('/home/ubuntu/strippedfiles/lem.csv','a')
	for item in lem:
		file2.write(item.encode('utf-8',errors='ignore'))
		file2.write(" ")
	file2.close()


if __name__ == "__main__":
	csv_path = "/home/ubuntu/strippedfiles/yelp_academic_dataset_user.csv"
	with open(csv_path, "rb") as f_obj:
		csv_reader(f_obj)