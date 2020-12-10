from nltk.stem.lancaster import LancasterStemmer
from nltk import word_tokenize
from numpy.core.fromnumeric import sort
from pandas import Series, DataFrame, get_dummies
from numpy import zeros

class Encoder():
    stemmer = LancasterStemmer()
        
    @classmethod
    def transformSeries(cls, series, as_is=True, sort_series=True, set_series=False):
        values = []
    
        for value in series.values:

            value = word_tokenize(value)
            
            tempTokens = []
            for token in value:
                token = cls.stemmer.stem(token)
                tempTokens.append(token)
            if as_is: values.append(' '.join(tempTokens))
            else: values.extend(tempTokens)
                            
        ret = list(values)
        
        if set_series: ret = list(set(ret))
        if sort_series: ret = sort(ret)
        return Series(ret)


    @classmethod
    def encode(cls, sentenceSeries, wordsSeries):
        # print('E sentence series', sentenceSeries, 'should be series:', type(sentenceSeries))

        sentenceSeries = cls.transformSeries(sentenceSeries, as_is=True, sort_series=False)
        # print('E-:', sentenceSeries)

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


    @classmethod
    def oneHotEncode(cls, series):
        df = get_dummies(series)
        return df


    @classmethod
    def encodeSentence(self, sentence, transformedWordDict):
        sentence = Series([sentence])
        sentence = self.encode(sentence, transformedWordDict)
        
        return sentence   