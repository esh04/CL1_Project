from numpy import append
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

font="./font/gargi.ttf"

###################################################3

#remove links (if any)
def remove_links(text):
    text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    return text

#remove digits
def remove_numbers(text):
    #digits are mapped to None
    translation_table = str.maketrans('', '', string.digits)

    #deletes all number
    text = text.translate(translation_table)
    return text


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
    string.punctuation += '‘'
    string.punctuation += '’'

    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]

    # remove remaining tokens that are in English or are numbers 
    words = [word for word in stripped if not word.isalnum()]


    # FILTERING OUT STOPWORDS

    filename = 'stopwords.txt'
    file = open(filename, 'rt')
    stop_words = file.read()
    file.close()

    words = [w for w in words if not w in stop_words]

    #uncommment to store cleaned tokens in a file

    # with open('./data/clean_tokens.txt', 'w') as filehandle:
    #     filehandle.writelines("%s\n" % word for word in words)

    return words


def stemmer(string):
    #stemming
    stemmed_tokens = []
    doc = nlp_Spacy(string)
    for token in doc:
        stemmed_tokens.append(token.norm_)
    
    #uncommment to store stemmed tokens in a file

    # with open('./data/stem.txt', 'w') as filehandle:
    #     filehandle.writelines("%s\n" % stem for stem in stemmed_tokens)

    return stemmed_tokens

#lemmatization and POS tagging are performed here together
def stanza_operations(string):
    doc = nlp(string)
    lemm_tokens = []
    POS_tagged = []
    POS_tags = []
    for sent in doc.sentences:
        for word in sent.words:
            lemm_tokens.append(word.lemma)
            POS_tagged.append([word.text,word.xpos])
            POS_tags.append(word.xpos)


    #uncommment to store stemmed tokens in a file
    # with open('./data/lemm.txt', 'w') as filehandle:
    #     filehandle.writelines("%s\n" % lemm for lemm in lemm_tokens)
    
    #uncommment to store POS tokens in a file
    # with open('./data/POS.txt', 'w') as filehandle:
    #     filehandle.writelines("%s, %s\n" % (pos[0], pos[1]) for pos in POS_tagged)

    return lemm_tokens, POS_tagged , POS_tags

def wordcloud(POS_tagged):
    #only nouns and adjectives will be included in the wordcloud
    cloud_words = []
    tags = ['NN','NNC','NNP','NNPC']

    for token in POS_tagged:
        if token[1] in tags:
            cloud_words.append(token[0])

    #word cloud

     #top 147 words make the word cloud i.e all words that have been used more than 100 times
    dictionary=Counter(cloud_words)


    words_in_cloud = dictionary.most_common(155)
    # print all words in decreasing order of priority
    print(words_in_cloud)

    #top 155 words make the word cloud

    cloud = WordCloud(max_font_size=80,colormap="hsv",width=600, height=400,background_color="white",font_path=font,max_words=155).generate_from_frequencies(dictionary)
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