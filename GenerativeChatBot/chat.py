import numpy as np
import re
from test_model import encoder_model, decoder_model, num_decoder_tokens, num_encoder_tokens, input_features_dict, target_features_dict, reverse_target_features_dict, max_decoder_seq_length, max_encoder_seq_length

class ChatBot():
    # negative_commands: a list of words and phrases that indicate the user’s response is negative when asked if they want to chat.
    negative_commands = ('No', 'no', 'never', 'Never', 'Not now', 'not now', 'I don\'t want to')
    # exit_commands: a list of words and phrases that should terminate the chatbot conversation.
    exit_commands = ('exit', 'Exit', 'quit', 'Quit', 'stop', 'Stop', 'goodbye', 'Goodbye', 'Seeya', 'seeya', 'Later', 'later')

    '''
    function start_chat(): greets the user and asks if the user want's to chat

    return: print-statement if the user denies or calls on .generate_response 
    '''
    def start_chat(self):
        user_input = input('Hello, my friend, do you want to have a conversation with me?\n')
        if user_input in self.negative_commands:
            print('Okay, then #r00d but okay')
            return
        self.chat(user_input)
    
    '''
    function chat(user_input): a method which keeps up a loop of conversation

    :param user_input, generated in start_chat
    '''
    def chat(self, user_input):
        while not self.make_exit(user_input):
            user_input = input(self.generate_response(user_input))
   
    '''
    function make_exit(user_input): a method which checks whether any exit commands are in the user_input

    :param user_input, generated in start_chat
    :return True/False depending on whether an exit command is in the user_input
    '''
    def make_exit(self, user_input):
        for exit_command in self.exit_commands:
            if exit_command in user_input:
                print('Okay then, have good day')
                return True
            else:
                return False
    '''
    function string_to_matrix(user_input): a method which accepts the user input and creates a numpy matrix with
    one hot-vectors

    :param user_input, generated in start_chat
    :return user_input_matrix, the matrix of one hot-vectors
    '''
    def string_to_matrix(self, user_input):
        tokens = re.findall(r"[\w']+|[^\s\w]", user_input)
        user_input_matrix = np.zeros((1, max_encoder_seq_length, num_encoder_tokens),dtype='float32')
        for timestep, token in enumerate(tokens):
          if token in input_features_dict:
            user_input_matrix[0, timestep, input_features_dict[token]] = 1. 
        
        return user_input_matrix
    '''
    function generate_response(user_input): generates the response by decoding the user_input by using a neural net which
    has been defined in training_model.py

    :return chatbot_output, a string which the chatbot should output
    '''
    def generate_response(self,user_input):
        input_matrix = self.string_to_matrix(user_input)
        # Hidden state values
        states_value = encoder_model.predict(input_matrix)
        target_seq = np.zeros((1, 1, num_decoder_tokens))
        target_seq[0, 0, target_features_dict['<START>']] = 1.
        
        chatbot_output = ''

        stop_condition = False
        # Decoder which generates an output matrix of possible words and their probabilities
        while not stop_condition:
            output_tokens, hidden_state, cell_state = decoder_model.predict([target_seq] + states_value)
        
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_token = reverse_target_features_dict[sampled_token_index]
        
        chatbot_output += " " + sampled_token
        
        if (sampled_token == '<END>' or len(chatbot_output) > max_decoder_seq_length):
            stop_condition = True
            
        target_seq = np.zeros((1, 1, num_decoder_tokens))
        target_seq[0, 0, sampled_token_index] = 1.
        
        states_value = [hidden_state, cell_state]
        
        # remove <START> and <END> tokens
        chatbot_output = chatbot_output.replace("<END>", "").replace("<START>", "")  
        return chatbot_output

chat_bot = ChatBot()

chat_bot.start_chat()