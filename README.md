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

## To run the Project
Both the folders English and Hindi, contain a `main.py` which is to be runned. Uncomment the lines depending upon the required output. Appropriate comments have been provided in the code. 
To store the tokens in files, uncomment the required code in `functions.py`
The required packages have been added in requirements.txt, apart fromm that the NLTK, stanza and spacy datasets have to be downloaded.

## Creating the Dataset
The project contains crawl_English.py and crawl_Hindi.py; these are the codes used to crawl data from the urls. All the urls used are mentioned in the url.txt file in each folder. `Beautiful soup` was used in order to crawl this data.

## Cleaning data
`re` is used to clean the data.

## Processing the English Dataset
`NLTK` is used to tokenize, remove stopwords, stem, lemmatize and POS tag.

## Processing the Hindi Dataset
`NLTK` is used to tokenize the data, a custom dataset (stopwords.txt) is used to remove stopwords, `spacy` is used for stemming and `stanza` is used to lemmatize and POS tag.
(P.S: lemmatizationa and POS tagging takes longer than the others for the Hindi dataset)

## Frequency Graph
`nltk.FreqDist` was used to make this.

## Wordcloud
`wordcloud` python package and `mathplotlib.pyplot` was used in order to form the wordcloud.
Only the Nouns and Adjectives are used to make the Wordcloud more relevant. 

(A seperate font has to be imported to make the Hindi wordcloud and graphs, the fonts have been include in ./Hindi/font)

The Hindi and English folders have the graphs and wordclouds also enclosed.
To view any Frequency Graph, uncomment the necessary line in `main.py`, by default only the wordcloud and  list of the tokens in decreasing order of priority are printed.

## Final Result

![WordCloud](https://user-images.githubusercontent.com/71181616/124010000-e4963500-d9fb-11eb-8e59-dfd58cfc8537.png)

The above wordcloud is of the data collected through around 200 news articles regarding 'Corona Virus'

![wordcloud](https://user-images.githubusercontent.com/71181616/124010031-ecee7000-d9fb-11eb-919f-23d64e56a88e.png)

The above wordloud is about the Indian classic 'Mahabharata'. It comprises some of the incidences that took place during the 'Mahabharata'.

The analysis.pdf contains the overview of the algorithms used and analysis of the Frequency Graphs at various stages.
The data folder has all the tokens saved at different stages.
The graph folder contains all the Frequency graphs.
