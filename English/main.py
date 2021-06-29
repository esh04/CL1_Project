from Hindi.main import POS_tags
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import re
import nltk
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud


#English_data.txt is the scraped English data.
filename = 'English_data.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

####################################################

#remove links
text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

####################################################

# TOKENISATION
sentences = sent_tokenize(text)
tokens = word_tokenize(text)


#########################################

#Cleaning the corpus

# convert to lower case
tokens = [w.lower() for w in tokens]
# remove punctuation from each word
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
# remove remaining tokens that are not alphabetic 
words = [word for word in stripped if word.isalpha()]

English_words = set(nltk.corpus.words.words())
#adding words relevent to current topic

English_words.add('coronavirus')
English_words.add('covishield')
English_words.add('wuhan')
English_words.add('covaxin')
English_words.add('pfizer')
English_words.add('sputnik')
English_words.add('pfizerbiontech')
English_words.add('johnson')


#remove foreign words
words = [word for word in stripped if word in English_words ]


#################################################


# FILTERING OUT STOPWORDS
stop_words = set(stopwords.words('english'))
stop_words.add('al')
stop_words.add('may')
stop_words.add('might')
stop_words.add('also')
stop_words.add('could')
stop_words.add('like')
stop_words.add('said')

words = [w for w in words if not w in stop_words]


################################################

#Stemming and lemmatization

#stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in words]

#lemmatization
lm = WordNetLemmatizer()
lemmatized_tokens = [lm.lemmatize(token) for token in words]


####################################################

#POS tagging
POS_tagged = nltk.pos_tag(words)

#Making the wordcloud
cloud_words = []
tags = ['NN','JJ']

#only add those words to wordcloud that are nouns/adjectives
for token in POS_tagged:
    if token[1] in tags:
        cloud_words.append(token[0])

dictionary=Counter(cloud_words)
cloud = WordCloud(max_font_size=80,colormap="hsv",width=600, height=400,background_color="white").generate_from_frequencies(dictionary)
plt.figure(figsize=(20,15))
plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')
plt.show()


#to make graphs (uncomment whichever graph you wish to make)
#different lists denote the state of data at that point

# fd = nltk.FreqDist(tokens)

# fd = nltk.FreqDist(words)

# fd = nltk.FreqDist(stemmed_tokens)

# fd = nltk.FreqDist(lemmatized_tokens)

# POS_tags = [list[1] for list in POS_tagged]
# fd = nltk.FreqDist(POS_tags)

#and uncomment this line:
# fd.plot(100,cumulative=False)

#to store any of these in text files

with open('./data/tokens.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % token for token in tokens)

with open('./data/clean_tokens.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % word for word in words)

with open('./data/stem.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % stem for stem in stemmed_tokens)

with open('./data/lemm.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % lemm for lemm in lemmatized_tokens)

with open('./data/POS.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % pos for pos in POS_tags)
