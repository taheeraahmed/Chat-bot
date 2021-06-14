# 🤖 Chat-bots
Trying to implement three types of chat-bots in order to learn something about natrual language processing.

1. Rule-based based chat-bot 
2. Retrieval based chat-bot
3. Deep learning based chat-bot

### (1) Alien bot 👽 
Libraries used: <code>re</code> and <code>random</code>

This is a rule-based chat bot. The bot is supposed to be an alien which has been abolished from it's own civilization and needs a new home. It want's to gain more information about "Earth".
It can also cube numbers if you ask it to :) 

It's a quite simplistic approach to a chat bot and only uses if-elif-else statements to match different regular expressions to different intents which have been self defined.  

### (2) Cyborg cantina 🌮
Libraries used: <code>re</code>, <code>collections</code>, <code>spacy</code>, <code>nltk</code>, <code>nltk.corpus</code> and <code>nltk.tokenize</code>
This is a retrieval based chat-bot, these are best for closed-domain tasks. This specific chat-bot is a system which answer's diner questions given a restaurant serving mexican cuisine. 

This approach uses td-idf scoring with cosine similarity, word embedded models and a set of user-defined functions. The intents and chat-bot responses has been written by the one and only Taheera. This is also a major drawback when taking this approach.

### (3) Generative chat-bot
The chat-bot is going to generate a text stream given the input of different streams of tweets. The streams consists of different topics. 

It takes advantage of deep learning, or more specifically, a neural network to generate new sentences. 
