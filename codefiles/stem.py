from nltk import PorterStemmer
import csv
import sys
import os


path = '/home/ubuntu/test'
listing = os.listdir(path)
outputpath = '/home/ubuntu/answers'
stemmer = PorterStemmer()
for infile in listing:
	dir_output_path = os.path.join(outputpath,infile)
	file2 = open(dir_output_path,'a')
	f = os.path.join(path,infile)
	with open(f) as file_object:	
		for line in file_object:
			stemword = [stemmer.stem(word)for word in line.split(" ")]
			final = ' '.join(stemword)
			file2.write(final)
			file2.write(" ")
	file2.close()
	



