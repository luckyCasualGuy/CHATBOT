from ChatBot_v2.utils import WordDict, IntentsReader
from pathlib import Path
from ChatBot_v2.encode import Encoder
from pandas import Series

class DataGenerator():
    wordDict = WordDict()
    intents = IntentsReader()

    @classmethod
    def generate(cls, intents: list, dir_path: str):
        path = Path(dir_path)

        cls.wordDict.reset()

        intents_df = cls.intents.generateIntentDataFrame(intents)
        classes_s = cls.intents.generateIntentClasses(intents)

        intents_df.to_csv(str(path/ 'intents_df.csv'), index=False)

        keys = cls.intents.getKeys()
        for value in intents_df[keys['patterns']].values:
            cls.wordDict.load(value.split(' '))

        wordDict_df = cls.wordDict.getDataFrame()
        wordDict_df.to_csv(path/ 'wordDict_df.csv', index=False)

        transformedWordDict_s = Encoder.transformSeries(
            wordDict_df['words'], as_is=False, set_series=True)
        transformedWordDict_s.to_csv(path/ 'transformedWordDict_s.csv', index=False)

        train_x_df = Encoder.encode(
            intents_df['patterns'], transformedWordDict_s)
        train_x_df.to_csv(path/ 'train_x_df.csv', index=False)

        train_y_df = Encoder.oneHotEncode(intents_df['tag'])
        train_y_df.to_csv(path/ 'train_y_df.csv', index=False)

        classes_s = Series(train_y_df.columns)
        classes_s.to_csv(path/ 'classes_s.csv', index=False)