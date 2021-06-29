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
