from functions import *

#the scraped data will be stored in this file: Hindi_data.txt
filename = 'Hindi_data.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

text = remove_links(text)
text = remove_numbers(text)

sent = tokenize_sentence(text)
tokens = tokenize_word(text)

#uncomment to view frequency graph of initial tokens
# Frequency_graphs(tokens)

cleaned_tokens = clean(tokens)

#uncomment to view frequency graph of cleaned tokens
# Frequency_graphs(cleaned_tokens)

#converts the list to a string so that spacy and stanza can be performed easilty
string = ' '.join([str(elem) for elem in cleaned_tokens])

stemm_tokens = stemmer(string)

#uncomment to view frequency graph of stemmed tokens
# Frequency_graphs(stemm_tokens)

lemm_tokens,POS_tagged,POS_tags = stanza_operations(string)

#uncomment to viewfrequency graph of lemmatized tokens
# Frequency_graphs(lemm_tokens)

#uncomment to form a frequency graph of all the POS_tags used
# Frequency_graphs(POS_tags) 

wordcloud(POS_tagged)










