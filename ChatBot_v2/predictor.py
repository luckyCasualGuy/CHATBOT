from keras.models import load_model
from ChatBot_v2.encode import Encoder
from pandas import read_csv
from numpy import amax, where
from random import choice

class ModelPredictor():
    def __init__(self, classes_s_path: str, transformedWordDict_s: str, model_path='./model',):
        self.readModel(model_path)
        self.checkClasses = read_csv(classes_s_path).values
        self.transformedWordDict = read_csv(transformedWordDict_s)['0']

    def readModel(self, model_path):
        self.model = load_model(model_path)

    def predict(self, value):
        return self.model.predict(value)

    def getPredictionFor(self, sentence):        
        sentence = Encoder.encodeSentence(sentence, transformedWordDict=self.transformedWordDict)
        sentence = self.predict(sentence)
        return self.getClassForResult(sentence)
        # return sentence

    def getClassForResult(self, sentence):
        max = amax(sentence[0])
        index = where(sentence == max)
        # return index
        return self.checkClasses[index[1][0]][0]


    def getResponseForClass(self, detectedClass, intents):
        for intent in intents:
            if intent['tag'] == detectedClass:
                return choice(intent['responses'])