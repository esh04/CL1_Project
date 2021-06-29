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

    with open('./data/tokens.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % token for token in tokens)

    return tokens

#cleaning the tokens
def clean(tokens):
    #convert to lower case
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

    #uncommment to store cleaned tokens in a file

    with open('./data/clean_tokens.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % word for word in words)

    return words

def stemmer(words):
    #stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in words]

    #uncommment to store stemmed tokens in a file

    with open('./data/stem.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % stem for stem in stemmed_tokens)

    return stemmed_tokens

def lemmatizer(words):
    #lemmatization
    lm = WordNetLemmatizer()
    lemmatized_tokens = [lm.lemmatize(token) for token in words]

    #uncommment to store stemmed tokens in a file

    with open('./data/lemm.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % lemm for lemm in lemmatized_tokens)

    return lemmatized_tokens

def POS_tagging(words):
    POS_tagged = nltk.pos_tag(words)
    return POS_tagged


def wordcloud(words,POS_tagged):
    

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

def Frequency_graphs(tokens):
   
    fd = nltk.FreqDist(tokens)
    #graph will have 50 entries
    fd.plot(50,cumulative=False)

##########################################################

#English_data.txt is the scraped English data.
filename = 'English_data.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

remove_links(text)
sent = tokenize_sentence(text)
tokens = tokenize_word(text)

#uncomment to view frequency graph of initial tokens
Frequency_graphs(tokens)

cleaned_tokens = clean(tokens)

#uncomment to view frequency graph of cleaned tokens
Frequency_graphs(cleaned_tokens)

stemm_tokens = stemmer(cleaned_tokens)

#uncomment to view frequency graph of stemmed tokens
Frequency_graphs(stemm_tokens)

lemm_tokens = lemmatizer(cleaned_tokens)

#uncomment to viewfrequency graph of lemmatized tokens
Frequency_graphs(lemm_tokens)

POS_tagged_tokens = POS_tagging(cleaned_tokens)

#uncomment to form a frequency graph of all the POS_tags used
POS_tags = [list[1] for list in POS_tagged_tokens]
Frequency_graphs(POS_tags) 


wordcloud(cleaned_tokens,POS_tagged_tokens)


##################################################################

#uncomment to form a frequency graph of a pre-processed token file present in data file (file name 'token' in this case) 


# with open("./data/tokens.txt") as f:
#     tokens = [ line.strip() for line in f ]

# Frequency_graphs(tokens)

#uncomment to form a wordcloud of a pre-processed token file present in data folder (file name 'token' in this case)

# with open("./data/tokens.txt") as f:
#     tokens = [ line.strip() for line in f ]

# wordcloud(tokens,POS_tagging(tokens))



