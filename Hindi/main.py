import string
from nltk.tokenize import sent_tokenize, word_tokenize
import re
from spacy.lang.hi import STOP_WORDS as STOP_WORDS_HI
import nltk
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import spacy
from spacy.lang.hi import Hindi
from wordcloud.wordcloud import FONT_PATH

import stanza
nlp = stanza.Pipeline('hi', processors='tokenize,lemma,pos')

from spacy.lang.hi import Hindi
nlp_Spacy = Hindi()

font="./font/Lohit-Devanagari.ttf"

###################################################3

#the scraped data will be stored in this file: Hindi_data.txt
filename = 'Hindi_data.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

###################################################

# CLEANING AND TOKENISATION

#remove links (if any)
text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

#tokenisation
sentences = sent_tokenize(text)
tokens = word_tokenize(text)


# remove punctuation from each word
#adding some additional punctuations
string.punctuation += '।'
string.punctuation += '“'
string.punctuation += '”'

table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]

# remove remaining tokens that are in English or are numbers 
words = [word for word in stripped if not word.isalnum()]


#################################################


# FILTERING OUT STOPWORDS

filename = './data/stopwords.txt'
file = open(filename, 'rt')
stop_words = file.read()
file.close()


words = [w for w in words if not w in stop_words]

#spacy-stopwords removal
words = [word for word in words if word not in set(STOP_WORDS_HI) ]


################################################


#stemming
stemmed_tokens = []
string = ' '.join([str(elem) for elem in words])
doc = nlp_Spacy(string)
for token in doc:
    stemmed_tokens.append(token.norm_)

###################################################

#TO LOAD ANY PRE-EXISTING TOKEN FILE (if you have preprocessed data you can comment out the code above this comment, and just load your file)
#loading data
# strip() removes the trailing \n

# with open("./data/clean_tokens.txt") as f:
#     clean_tokens = [ line.strip() for line in f ]



#POS tagging
POS_tags = []
lemm_tokens = []
string = ' '.join([str(elem) for elem in words])
doc = nlp(string)

###############################################

#only nouns and adjectives will be included in the wordcloud
cloud_words = []
tags = ['NN','JJ','NNC','NNP','NNPC']


for sent in doc.sentences:
    for word in sent.words:
        POS_tags.append(word.xpos)
        #LEMMETIZATION
        lemm_tokens.append(word.lemma)
        if word.xpos in tags:
            cloud_words.append(word.text)


#word cloud

dictionary=Counter(cloud_words)
cloud = WordCloud(max_font_size=80,colormap="hsv",width=600, height=400,background_color="white",font_path=font).generate_from_frequencies(dictionary)
plt.figure(figsize=(20,15))
plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')
plt.show()


#to make graphs (uncomment whichever graph you wish to make)
#different lists denote the state of data at that point

fd = nltk.FreqDist(lemm_tokens)

fd = nltk.FreqDist(stemmed_tokens)

fd = nltk.FreqDist(tokens)

fd = nltk.FreqDist(words)

fd = nltk.FreqDist(POS_tags)

# to print hindi words:

# also, uncomment these lines
plt.rcParams['font.sans-serif']=['gargi'] 
plt.rcParams['axes.unicode_minus']=False
fd.plot(50,cumulative=False)


#to store any of these in text files

with open('./data/tokens.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % token for token in tokens)

with open('./data/clean_tokens.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % word for word in words)

with open('./data/stem.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % stem for stem in stemmed_tokens)

with open('./data/lemm.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % lemm for lemm in lemm_tokens)

with open('./data/POS.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % pos for pos in POS_tags)


