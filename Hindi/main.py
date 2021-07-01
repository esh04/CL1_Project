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

cleaned_tokens = clean(tokens)

string = ' '.join([str(elem) for elem in cleaned_tokens])
stemm_tokens = stemmer(string)
lemm_tokens,POS_tagged,POS_tags = stanza_operations(string)

wordcloud(POS_tagged)

#uncomment to view graphs:
# Frequency_graphs(tokens)
# Frequency_graphs(cleaned_tokens)
# Frequency_graphs(stemm_tokens)
# Frequency_graphs(lemm_tokens)
# Frequency_graphs(POS_tags) 












