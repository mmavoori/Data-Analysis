from  nltk.tokenize import RegexpTokenizer
import nltk
import os, sys
filepath = "../reviewfiles/"
final_path = "../strippedfiles/"
dir = os.listdir(filepath)
for file in dir:
  f= open(filepath+file,"r")
  print(file)
  s1 = f.read().lower()
  f.close()
  tokenizer = RegexpTokenizer(r'\w+')
  token_list=tokenizer.tokenize(s1)
  temp_list = [w.strip() for w in token_list if w.strip() not in nltk.corpus.stopwords.words('english')]
  word_list=' '.join(temp_list)
  file_write = open(final_path+file,'w+')
  file_write.write(word_list)
  file_write.close()


