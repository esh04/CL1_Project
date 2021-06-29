# CL1_Project
Scrapping data and pre-processing it to form a word cloud in order to generate words of highest importance in English and Hindi. Created for the course project of the Spring '21 Course - Computational Linguistics -1.

## Tasks
1. Use crawling to extract 10,000 sentences from English and Hindi each.
2. Clean the corpus - Remove foreign words, punctuations, symbols.
3. Performing the following on the cleaned corpus:
    1. Tokenisation - Sentences and Tokens
    2. POS Tagging
    3. Remove Stopwords
    4. Stemming 
    5. Lemmatization
4. Making a frequency graph at each stage.
5. Building a word cloud

## Creating the Dataset
The project contains crawl_English.py and crawl_Hindi.py; these are the codes used to crawl data from the urls. All the urls used are mentioned in the url.txt file in each folder. `Beautiful soup` was used in order to crawl this data.

## Cleaning data
`re` is used to clean the data.

## Processing the English Dataset
`NLTK` is used to tokenize, remove stopwords, stem, lemmatize and POS tag.

## Processing the Hindi Dataset
`NLTK` is used to tokenize the data, `spacy` is used to remove stopwords - along with a custom stopword.txt, `spacy` is used for stemming and `stanza` is used to lemmatize and POS tag.

## Frequency Graph
`nltk.FreqDist` was used to make this.

## Wordcloud
`wordcloud` python package and `mathplotlib.pyplot` was used in order to form the wordcloud.
Only the Nouns and Adjectives are used to make the Wordcloud more relevant. 

(A seperate font has to be imported to make the Hindi wordcloud and graphs, the fonts have been include in ./Hindi/font)

The Hindi and English folders have the graphs and wordclouds also enclosed.

## Final Result

![NN+JJ](https://user-images.githubusercontent.com/71181616/123839516-d3c9be80-d92a-11eb-99af-129a80d8a1b9.png)

![NN+JJ](https://user-images.githubusercontent.com/71181616/123839554-df1cea00-d92a-11eb-9d28-97264e20ec7c.png)


