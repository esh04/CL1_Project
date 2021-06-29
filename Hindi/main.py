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

#remove links (if any)
def remove_links(text):
    text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

#tokenisation
def tokenize_sentence(text):
    sentences = sent_tokenize(text)
    return sentences

def tokenize_word(text):
    tokens = word_tokenize(text)
    
    #uncommment to store tokens in a file

    # with open('./data/tokens.txt', 'w') as filehandle:
    #     filehandle.writelines("%s\n" % token for token in tokens)

    return tokens

#cleaning the tokens
def clean(tokens):
    # remove punctuation from each word
    #adding some additional punctuations
    string.punctuation += '।'
    string.punctuation += '“'
    string.punctuation += '”'

    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]

    # remove remaining tokens that are in English or are numbers 
    words = [word for word in stripped if not word.isalnum()]


    # FILTERING OUT STOPWORDS

    filename = './data/stopwords.txt'
    file = open(filename, 'rt')
    stop_words = file.read()
    file.close()


    words = [w for w in words if not w in stop_words]

    #spacy-stopwords removal
    words = [word for word in words if word not in set(STOP_WORDS_HI) ]

    #uncommment to store cleaned tokens in a file

    # with open('./data/clean_tokens.txt', 'w') as filehandle:
    #     filehandle.writelines("%s\n" % word for word in words)

    return words


def stemmer(words):
    #stemming
    stemmed_tokens = []
    string = ' '.join([str(elem) for elem in words])
    doc = nlp_Spacy(string)
    for token in doc:
        stemmed_tokens.append(token.norm_)
    
    #uncommment to store stemmed tokens in a file

    # with open('./data/stem.txt', 'w') as filehandle:
    #     filehandle.writelines("%s\n" % stem for stem in stemmed_tokens)

    return stemmed_tokens

            
#lemmatization
def lemmatizer(words):
    lemm_tokens = []
    string = ' '.join([str(elem) for elem in words])
    doc = nlp(string)

    for sent in doc.sentences:
        for word in sent.words:
            lemm_tokens.append(word.lemma)

    #uncommment to store stemmed tokens in a file

    # with open('./data/lemm.txt', 'w') as filehandle:
    #     filehandle.writelines("%s\n" % lemm for lemm in lemm_tokens)

    return lemm_tokens



#POS tagging
def POS_tagging(words):

    POS_tags = []

    string = ' '.join([str(elem) for elem in words])
    doc = nlp(string)
    for sent in doc.sentences:
        for word in sent.words:
            POS_tags.append(word.xpos)
    
    
    return POS_tags

def wordcloud(words):
    #only nouns and adjectives will be included in the wordcloud
    cloud_words = []
    tags = ['NN','JJ','NNC','NNP','NNPC']
    string = ' '.join([str(elem) for elem in words])
    doc = nlp(string)

    for sent in doc.sentences:
        for word in sent.words:
            if word.xpos in tags:
                cloud_words.append(word.text)


    #word cloud

    dictionary=Counter(cloud_words)
    cloud = WordCloud(max_font_size=80,colormap="hsv",width=600, height=400,background_color="white",font_path=font).generate_from_frequencies(dictionary)
    plt.figure(figsize=(20,15))
    plt.imshow(cloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def Frequency_graphs(tokens):
   
    fd = nltk.FreqDist(tokens)
    # to print hindi words:
    plt.rcParams['font.sans-serif']=['gargi'] 
    plt.rcParams['axes.unicode_minus']=False

    #graph will have 50 entries
    fd.plot(50,cumulative=False)

################################################################

#the scraped data will be stored in this file: Hindi_data.txt
filename = 'Hindi_data.txt'
file = open(filename, 'rt')
text = file.read()
file.close()



remove_links(text)
sent = tokenize_sentence(text)
tokens = tokenize_word(text)

#uncomment to view frequency graph of initial tokens
# Frequency_graphs(tokens)

cleaned_tokens = clean(tokens)

#uncomment to view frequency graph of cleaned tokens
# Frequency_graphs(cleaned_tokens)

stemm_tokens = stemmer(cleaned_tokens)

#uncomment to view frequency graph of stemmed tokens
# Frequency_graphs(stemm_tokens)

lemm_tokens = lemmatizer(cleaned_tokens)

#uncomment to viewfrequency graph of lemmatized tokens
# Frequency_graphs(lemm_tokens)

POS_tags = POS_tagging(cleaned_tokens)

#uncomment to form a frequency graph of all the POS_tags used
# Frequen   cy_graphs(POS_tags) 


wordcloud(cleaned_tokens)


##################################################################

#uncomment to form a frequency graph of a pre-processed token file present in data file (file name 'token' in this case) 


# with open("./data/tokens.txt") as f:
#     tokens = [ line.strip() for line in f ]

# Frequency_graphs(tokens)

#uncomment to form a wordcloud of a pre-processed token file present in data folder (file name 'token' in this case)

# with open("./data/tokens.txt") as f:
#     tokens = [ line.strip() for line in f ]

# wordcloud(tokens)







