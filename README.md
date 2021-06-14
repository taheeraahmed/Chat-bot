# 🤖 Chat-bots
Trying to implement three types of chat-bots in order to learn something about natrual language processing.

1. Rule-based based chat-bot 
2. Retrieval based chat-bot
3. Deep learning based chat-bot

### (1) Alien bot 👽 
This is a rule-based chat bot. The bot is supposed to be an alien which has been abolished from it's own civilization and needs a new home. It want's to gain more information about "Earth".
It can also cube numbers if you ask it to :) 

It's a quite simplistic approach to a chat bot and only uses if-elif-else statements to match different regular expressions to different intents. 

### (2) Cyborg cantina 🌮
This is a retrieval based chat-bot, these are best for closed-domain tasks. This specific chat-bot is a system which answer's diner questions given a restaurant serving mexican cuisine. 

This approach uses td-idf scoring with cosine similarity, word embedded models and a set of use-defined functions.

### (3) Generative chat-bot
The chat-bot is going to generate a text stream given the input of different streams of tweets. The streams consists of different topics. 

This chat-bot takes advantage of deep learning, or more specifically, a neural network. 
