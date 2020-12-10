# from ChatBot.core import Trainer
from Intents.nullIntents import intents, new_intents
from ChatBot_v2.generate import DataGenerator
from pandas import read_csv, Series
from ChatBot_v2.predictor import ModelPredictor
from ChatBot_v2.trainer import ModelTrainer

# ChatBot v2
# DataGenerator.generate(new_intents, dir_path='./data')

# mt = ModelTrainer('./data/train_x_df.csv', './data/train_y_df.csv')
# mt.startTraining('./model')


mp = ModelPredictor('./data/classes_s.csv', './data/transformedWordDict_s.csv', model_path='./model')


while True:
    ip = str(input("::< "))
    pre = mp.getPredictionFor(ip)
    print("::> ", mp.getResponseForClass(pre, new_intents))


#Chatbot V1

# trainer = Trainer(new_intents)
# trainer.startTraining()

# while True:
#     ip = str(input("::< "))
#     pre = trainer.predict(ip)
#     print("::> ", trainer.getResponseForClass(pre))

# for sentence in [
#     "Hello, How do you do.",
#     "I need help",
#     "What can you help me with?",
#     "I want to know more",
#     "Bye.",
#     "Thanks a lot!",
#     "Thank you for your help.",
#     "Why are you so funny?",
#     "I want to know more.",
#     "Hi, What is this?",
#     "It was helpful, thanks!",
#     "Hey man!",
#     "I like this bot",
#     "What do you do?",
#     "What is your company into?",
#     "Is dolphyn for me?",
#     "What products do you have?",
#     "Why the name dolphyn?",
#     "I would like to know more about the products."
# ]:
#     print('\n', sentence)
#     pre = trainer.predict(sentence)
#     print(pre, '\n')
#     print(":> ", trainer.getResponseForClass(pre))
    # print(trainer.checkClasses)