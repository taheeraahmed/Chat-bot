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
Libraries used: <code>tensorflow</code>, <code>keras</code>, <code>numpy</code> and <code>re</code>

The chat-bot is going to generate a text stream given the input from a corpus consisting of different movie dialogues. 
It uses a seq2seq decoding function (which can be found in <code>seq2seq.py</code>), where the decoder will generate several output tokens, and the one with the highest probability will be selected. 

The neural net is trained by using RMS-prop (which is a fancy type of backpropgation) and categorical cross entropy to measure the error rate. The model is trained in <code>training_model.py</code>. When running this script there will be generate a <code>training_model.h5</code>- file which will be used later on when using the <code>seq2seq.py</code> script.


This technique uses deep learning, and the outcome is highly dependent on the training data (as with every other neural nets). 