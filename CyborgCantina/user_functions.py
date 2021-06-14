import re
from collections import Counter
import spacy
word2vec = spacy.load('en')
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))

# Preprocesses the input sentence given by the user
# Removes uppercases, whitespaces, tokenizes 
# Return an array of the strings given by the user
def preprocess(input_sentence):
    input_sentence = input_sentence.lower()
    input_sentence = re.sub(r'[^\w\s]','',input_sentence)
    tokens = word_tokenize(input_sentence)
    input_sentence = [i for i in tokens if not i in stop_words]
    return(input_sentence)

# Compares two different strings and sees if 
# they have anything in common aka. if there are any 
# similar words
# Returns this number
def compare_overlap(user_message, possible_response):
    similar_words = 0
    for token in user_message:
        if token in possible_response:
              similar_words += 1
    return similar_words

# Uses pos-tagged user message and extracts nouns 
# from the input sentence and is used for entitiy extraction 
def extract_nouns(tagged_message):
    message_nouns = list()
    for token in tagged_message:
        if token[1].startswith("N"):
            message_nouns.append(token[0])
    return message_nouns

# Computes similarity given a token and a category 
# Returns a 2D array of the token, the category and the similarity
def compute_similarity(tokens, category):
    output_list = list()
    for token in tokens:
        output_list.append([token.text, category.text, token.similarity(category)])
    return output_list
  