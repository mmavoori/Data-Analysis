import os
import re
from gensim import corpora, models, similarities
import pylab as pl

# LDA, k number of topics
k = 10

stoplist = set('came way dad yes try oh phoenix one two three four th alot well wasn went now doesn know want give take said lo r w co st v o b c g p bf ok k l n x f didn m nice restaurant back food good great place don always a about above after again against all am and any are at as be because been before being below between both but by can cant cannot could couldnt do did does down each for from further had have here how if me no nor not our of the and to too i is in into on there then them themselves this it he she her him you so some that was with would more or they will do has which an embedded quote its embed dont out who whom why where when his very other only while their http www up com than my your also most mostly never next what much one such many us were we over own often should shall same that those under until when won d re s t ll ve im these just isnt ive theres go going get got however made meanwhile please perhaps see seem seems thru even doesnt hes wouldnt thats youre wasnt youll really got like make makes think around through didnt doing may might maybe wont u arent werent ill e'.split())

path = '../stemfiles'
listing = os.listdir(path)
# If LDA model doesn't exist already...
if not os.path.isfile('lda_model'):
    # Do everything
    print "Generating LDA model..."
    os.mkdir('LDA')
    corpus = []
    for infile in listing:
      infile=os.path.join('../stemfiles',infile)
      with open(infile, "r") as myfile:
        review=myfile.read().replace('\n', '')
        # Only care about documents of certain length
        # Remove punctuations
      review = re.sub(r'[^a-zA-Z]', ' ', review)
      # To lowercase
      review = review.lower()
      # Remove stop words
      texts = [word for word in review.lower().split() if word not in stoplist]
      try:
        corpus.append(texts)
      except:
        pass
        

    # Build dictionary
    dictionary = corpora.Dictionary(corpus)
    dictionary.save('LDA/restaurant_reviews.dict')

    # Build vectorized corpus
    corpus_2 = [dictionary.doc2bow(text) for text in corpus]
    corpora.MmCorpus.serialize('LDA/restaurant_reviews.mm', corpus_2)
    
    lda = models.LdaModel(corpus_2, num_topics=k, id2word=dictionary)
    lda_topics = lda.show_topics(num_topics=-1, num_words=10, log=False, formatted=True)
    
    # Save LDA model to file
    lda.save('LDA/lda_model')

    # Save topics and terms to file
    file_lda = open("LDA/lda_topics.txt", mode = "w")
    count = 1
    for topic in lda_topics:
        topic = re.sub(r'[^a-z\s]', "", topic)
        topic = re.sub(" + ", ", ", topic)
        data_str = "Topic {0}: {1}\n".format(str(count), topic)
        print data_str
        file_lda.write(data_str.encode('utf-8'))
        count += 1
    file_lda.close()
# Just load previous LDA model
else:
    print "Loading LDA model..."
    lda = models.LdaModel.load('LDA/lda_model')
    
    f = open("LDA/lda_topics.txt", mode = "r")
    for line in f:
        print line
    f.close()


