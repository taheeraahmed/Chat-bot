# importing regex and random libraries
import re
import random

class AlienBot:
  # potential negative responses
  negative_responses = ("No","no" "Nope", "Nah", "naw", "not a chance", "sorry", "never")
  # keywords for exiting the conversation
  exit_commands = ("quit","Exit", "pause", "exit", "goodbye", "bye", "later", "stop")
  # random starter questions
  random_questions = (
        "Why are you here?\n",
        "Are there many humans like you?\n",
        "What do you consume for sustenance?\n",
        "Is there intelligent life on this planet?\n",
        "Does Earth have a leader?\n",
        "What planets have you visited?\n",
        "What technology do you have on this planet?\n",
        "Why does human exist?\n", 
        "What other galaxies have you been to?\n", 
        "Why do you eat animals?\n",
    )

  def __init__(self):
    self.alienbabble = {'describe_planet_intent': r'.*\s*your planet.*',
                        'answer_why_intent': r'why\sare.*',
                        'cubed_intent': r'.*cube.*(\d+)'
                            }
  # Define .greet() below:
  def greet(self):
    self.name = input("Hello human, what is your name?\n")
    self.will_help = input(f"Hi {self.name}, I'm Etcetera, and I'm not from here. Would you be so kind to answer some questions?\n")
    
    if self.will_help in self.negative_responses:
      print("Okay then, have a nice day on Earth!")
      return exit
    self.chat()

  # Define .make_exit() here:
  def make_exit(self, reply):
    for exit_command in self.exit_commands:
      if reply in exit_command:
        print('Thanks for nothing, but still have a great Earth day:)')
        return True

  # Define .chat() next:
  def chat(self):
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
      reply = input(self.match_reply(reply))

  # Define .match_reply() below:
  def match_reply(self, reply):
    for intent, regex_pattern in self.alienbabble.items():
      found_match = re.match(regex_pattern, reply)
      if found_match and intent == 'describe_planet_intent':
        return self.describe_planet_intent()
      elif found_match and intent == 'answer_why_intent':
        return self.answer_why_intent()
      elif found_match and intent == 'cubed_intent':
        return self.cubed_intent(found_match.groups()[0])
      else:
        return self.no_match_intent()

  # Define .describe_planet_intent():
  def describe_planet_intent(self):
    responses = (
      "My planet is a utopia of diverse organisms and species. ", 
      "I am from Opidipus, the capital of the Wayward Galaxies. ",
      "It is almost 1 billion light years away",
      "We don't have such a fruity and delightful type of vegetation like you have. Our planet is close to its end, we are therefore looking for a new home.")
    return random.choice(responses)

  # Define .answer_why_intent():
  def answer_why_intent(self):
    responses = (
      "I come in peace. ",
      "I am here to collect data on your planet and its inhabitants. ",
      "I heard the coffee is good. ", 
      "I need a new home, my family abolished me. ", 
      "I want to learn to speak mandarin", 
      "I want to learn more about humans",
    )
    return random.choice(responses)
       
  # Define .cubed_intent():
  def cubed_intent(self, number):
    number = int(number)
    cubed_number = number**3
    return f"The cube of {number} is {cubed_number}. Isn't that cool?"

  # Define .no_match_intent():
  def no_match_intent(self):
    responses = (
      "Please tell me more.",
      "Tell me more! ",
      "Why do you say that? ", 
      "I see. Can you elaborate?", 
      "Interesting. Can you tell me more?", 
      "I see. How do you think?", 
      "Why?", 
      "How do you think I feel when you say that?"
    )
    return random.choice(responses)

# Create an instance of AlienBot below:
alien_bot = AlienBot()
alien_bot.greet()
