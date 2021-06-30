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

POS_tagged_tokens = POS_tagging(lemm_tokens)

#uncomment to form a frequency graph of all the POS_tags used
# POS_tags = [list[1] for list in POS_tagged_tokens]
# Frequency_graphs(POS_tags) 


wordcloud(lemm_tokens,POS_tagged_tokens)


##################################################################

#uncomment to form a frequency graph of a pre-processed token file present in data file (file name 'token' in this case) 


# with open("./data/tokens.txt") as f:
#     tokens = [ line.strip() for line in f ]

# Frequency_graphs(tokens)

#uncomment to form a wordcloud of a pre-processed token file present in data folder (file name 'token' in this case)

# with open("./data/tokens.txt") as f:
#     tokens = [ line.strip() for line in f ]

# wordcloud(tokens,POS_tagging(tokens))



