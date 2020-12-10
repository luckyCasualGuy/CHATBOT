from pandas import DataFrame, Series

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
            

    def generateIntentDataFrame(self, intents=None):
        # Maker this change in v1 too
        if intents:
            self.loadIntents(intents)

        tag = []
        pattern = []
        for intent in self.intents:
            for patt in intent[self.__patterns]:
                tag.append(intent[self.__tag])
                pattern.append(patt)
        
        return DataFrame({self.__patterns: pattern, self.__tag: tag})

    def generateIntentClasses(self, intents=None):
        if not intents:
            intents = self.intents
        classes = []
        for intent in intents:
            classes.append(intent[self.__tag])

        return Series(list(set(classes)))

    def getKeys(self): return {"tag": self.__tag, "patterns": self.__patterns, "responses": self.__responces}
        
    def loadIntents(self, intents):
        self.__init__(intents)


class WordDict():
    __wordDict = {}

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

    def reset(self): self.__wordDict = {}
