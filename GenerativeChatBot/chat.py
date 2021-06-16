import numpy as np
import re
from test_model import encoder_model, decoder_model, num_decoder_tokens, num_encoder_tokens, input_features_dict, target_features_dict, reverse_target_features_dict, max_decoder_seq_length, max_encoder_seq_length

class ChatBot():
    #negative_commands: a list of words and phrases that indicate the user’s response is negative when asked if they want to chat.
    negative_commands = ('No', 'no', 'never', 'Never', 'Not now', 'not now', 'I don\'t want to')
    #exit_commands: a list of words and phrases that should terminate the chatbot conversation.
    exit_commands = ('exit', 'Exit', 'quit', 'Quit', 'stop', 'Stop', 'goodbye', 'Goodbye', 'Seeya', 'seeya', 'Later', 'later')

    #.start_chat(): a method that greets the user, asks if the user would like to chat, 
    # returns from the program if not (using the negative_commands list), 
    # and continues the chat if the user is interested.

    def start_chat(self):
        user_input = input('Hello, my friend, do you want to have a conversation with me?\n')

        if user_input in self.negative_commands:
            print('Okay, then #r00d but okay')
            return
        
        self.chat()

    # .make_exit(): a method that checks if any exit commands are in the user’s reply. 
    # The method should return True if the reply contains any exit command, 
    # False if the reply contains no exit commands.

    def make_exit(self, user_input):
        for exit_command in self.exit_commands:
            if exit_command in user_input:
                print('Okay then, have good day')
                return True
            else:
                return False

    # .string_to_matrix(): a method that accepts user input and creates a NumPy matrix of 
    # one-hot vectors with a shape of (1, max_encoder_seq_length, num_encoder_tokens):

    # The method should only account for a given timestep and token if the token exists within the input_features_dict:

    def string_to_matrix(self, user_input):
        tokens = re.findall(r"[\w']+|[^\s\w]", user_input)
        user_input_matrix = np.zeros((1, max_encoder_seq_length, num_encoder_tokens),dtype='float32')
        for timestep, token in enumerate(tokens):
          if token in input_features_dict:
            user_input_matrix[0, timestep, input_features_dict[token]] = 1. 
        
        return user_input_matrix

    # .generate_response(): a method that copies the body of decode_sequence() from test_model.py. 
    # However, this method should accept user input and use .string_to_matrix() to convert user_input into a NumPy matrix. 
    # The method should also remove "<START>" and "<END>" from the chatbot response before it gets returned from the method.

    def generate_response(self,user_input):
        # Encode the input as state vectors.
        states_value = encoder_model.predict(user_input)

        # Generate empty target sequence of length 1.
        target_seq = np.zeros((1, 1, num_decoder_tokens))
        # Populate the first token of target sequence with the start token.
        target_seq[0, 0, target_features_dict['<START>']] = 1.

        # Sampling loop for a batch of sequences
        # (to simplify, here we assume a batch of size 1).
        decoded_sentence = ''

        stop_condition = False
        while not stop_condition:
            # Run the decoder model to get possible 
            # output tokens (with probabilities) & states
            output_tokens, hidden_state, cell_state = decoder_model.predict(
            [target_seq] + states_value)

            # Choose token with highest probability
            sampled_token_index = np.argmax(output_tokens[0, -1, :])
            sampled_token = reverse_target_features_dict[sampled_token_index]
            decoded_sentence += " " + sampled_token

            # Exit condition: either hit max length
            # or find stop token.
            if (sampled_token == '<END>' or len(decoded_sentence) > max_decoder_seq_length):
                stop_condition = True

            # Update the target sequence (of length 1).
            target_seq = np.zeros((1, 1, num_decoder_tokens))
            target_seq[0, 0, sampled_token_index] = 1.

            # Update states
            states_value = [hidden_state, cell_state]

        return decoded_sentence