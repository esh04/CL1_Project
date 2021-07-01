from functions import *

#English_data.txt is the scraped English data.
filename = 'English_data.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

text = remove_links(text)
text = remove_numbers(text)
sent = tokenize_sentence(text)
tokens = tokenize_word(text)

cleaned_tokens = clean(tokens)
stemm_tokens = stemmer(cleaned_tokens)
lemm_tokens = lemmatizer(cleaned_tokens)
POS_tagged_tokens = POS_tagging(lemm_tokens)

wordcloud(lemm_tokens,POS_tagged_tokens)


#Uncomment to view graphs
# Frequency_graphs(tokens)
# Frequency_graphs(cleaned_tokens)
# Frequency_graphs(stemm_tokens)
# Frequency_graphs(lemm_tokens)

# POS_tags = [list[1] for list in POS_tagged_tokens]
# Frequency_graphs(POS_tags)
