# from Trainer.model import Modal
from numpy.core.fromnumeric import sort
from numpy import expand_dims
from pandas import DataFrame, Series, get_dummies
from nltk import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
from numpy import zeros, where, amax
from random import choice

class IntentsReader():
    # checking
    __tag = "tag"
    __patterns = "patterns"
    __responces = "responses"
    __req_keys = [__tag, __patterns, __responces]

    def __init__(self, intents: list = None):
        self.intents = self.__intentCheck(intents)

    class WrongIntent(Exception): pass
    def __intentCheck(self, intents):
        if not isinstance(intents, list) and intents != None:
            raise ValueError("Intent has to be list")

        if intents:
            check_all = 0 # for checking all intents have these keys
            for intent in intents:
                check_key = 0 # for checking in 3 req keys present
                for key in intent:
                    if key in self.__req_keys:
                        check_key += 1
                if check_key != 3:
                    break
                check_all += 1

            if check_all != len(intents):            
                raise self.WrongIntent("Intents should contain ", self.__req_keys)

        return intents
            

    def generateIntentDataFrame(self, intents):
        self.__loadIntents(intents)

        tag = []
        response = []
        for intent in self.intents:
            for patt in intent[self.__patterns]:
                tag.append(intent[self.__tag])
                response.append(patt)
        
        return DataFrame({self.__patterns: response, self.__tag: tag})

    def generateIntentClasses(self):
        classes = []
        for intent in self.intents:
            classes.append(intent[self.__tag])

        return Series(list(set(classes)))

    def getKeys(self): return {"tag": self.__tag, "patterns": self.__patterns, "responses": self.__responces}
        
    def __loadIntents(self, intents):
        self.__init__(intents)



class WordDict() :
    __wordDict = {}
    __currentIndex = 0

    def load(cls, loadThis: list):
        for key in loadThis:
            key = key.lower()
            cls.__put(key)           

    def __put(self, key):
        this = self.__wordDict
        if key not in this:
            this[key] = 0
        this[key] += 1

    def getDict(cls): return cls.__wordDict

    def getDataFrame(cls):
        this = cls.getDict()
        return DataFrame({'words': this.keys(), 'counts': this.values()})


class Transform():
    def __init__(self):
        self.stemmer = LancasterStemmer()
        
    
    def transformSeries(self, series, as_is=True, sort_series=True, set_series=False):
        values = []
        for value in series.values:
            value = word_tokenize(value)

            tempTokens = []
            for token in value:
                token = self.stemmer.stem(token)
                tempTokens.append(token)
            if as_is: values.append(' '.join(tempTokens))
            else: values.extend(tempTokens)
                            
        ret = list(values)
        if set_series: ret = list(set(ret))
        if sort_series: ret = sort(ret)
        return Series(ret)


    def encode(self, sentenceSeries, wordsSeries, encodeWithOne=False):
        sentenceSeries = self.transformSeries(sentenceSeries, as_is=True, sort_series=False)
        print('#####', type(wordsSeries))
        indexes = []
        for sentence in sentenceSeries.values:
            indexes_set = []
            for word in sentence.split(' '):
                index = wordsSeries[wordsSeries == word]
                if index.empty: indexes_set.append(-1)
                else: indexes_set.append(index.index[0])
            indexes.append(indexes_set)

        df = DataFrame(columns=[num for num in range(0, wordsSeries.size)])
        for i_s in indexes:
            encodes = Series(zeros((wordsSeries.size,)), index=df.columns)
            for i in encodes.index:
                if i in i_s: encodes.iloc[i] = 1
            df = df.append(encodes, ignore_index=True)
     
        return df

    def oneHotEncode(self, series):
        df = get_dummies(series)
        return df

 
from ChatBot.model import ModelTrainer, ModelPredictor
class Trainer():
    def __init__(self, intents: dict):
        self.__initIntents(intents)
        self.__initWordDict()
        self.__initTransform()
        self.trainer = ModelTrainer(self.train_x_df, self.train_y_df)
        self.predictor = ModelPredictor()

    class InvalidType(Exception): pass

    def __initIntents(self, intents):
        if not isinstance(intents, list): 
            raise self.InvalidType('intents shouldbe of type list')

        self.intents = IntentsReader(intents)
        self.intents_df = self.intents.generateIntentDataFrame(intents)
        self.classes = self.intents.generateIntentClasses()

    def __initWordDict(self):
        self.wordDict = WordDict()
        keys = self.intents.getKeys()

        for value in self.intents_df[keys['patterns']].values:
            self.wordDict.load(value.split(' '))

        self.wordDict_df = self.wordDict.getDataFrame()

    def __initTransform(self):
        self.transform = Transform()

        self.transformedWordDict = self.transform.transformSeries(
            self.wordDict_df['words'], as_is=False, set_series=True)
        
        self.train_x_df = self.transform.encode(
            self.intents_df['patterns'], self.transformedWordDict, encodeWithOne=True)

        self.train_y_df = self.transform.oneHotEncode(self.intents_df['tag'])
        # Adding one blank row for noanswer
        if self.classes.size != self.train_y_df.shape[1]:
            self.train_y_df['noanswer'] = 0

        self.checkClasses = self.train_y_df.columns


    def startTraining(self, path='./model'):
        self.trainer.startTraining(path)

    def predict(self, sentence):
        sentence = self.encodeSentence(sentence)
        sentence = self.predictor.predict(sentence)
        return self.getClassForResult(sentence)
    

    def encodeSentence(self, sentence):
        sentence = Series([sentence])
        sentence = self.transform.encode(sentence, self.transformedWordDict)
        # expand_dims(sentence, 0)
        return sentence

    def getClassForResult(self, sentence):
        max = amax(sentence[0])
        index = where(sentence == max)
        # return index[1][0]
        return self.checkClasses[index[1][0]]

    def getResponseForClass(self, detectedClass):
        for intent in self.intents.intents:
            if intent['tag'] == detectedClass:
                return choice(intent['responses'])

    def det(self):
        print('Chatbot v1:\n')
        print(self.transformedWordDict)
        en = self.encodeSentence('Hello!')
        print(en)
        print(len(en[en==1.0]))
        print('->', self.transformedWordDict[self.transformedWordDict=='!'])