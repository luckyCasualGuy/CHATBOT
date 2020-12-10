from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from keras.models import load_model

class ModelTrainer():
    def __init__(self, trainx, trainy):
        self.trainx = trainx
        self.trainy = trainy
        self.__initModel()
        self.__compile()

    def __initModel(self):
        # self.ntrainy = expand_dims(self.trainy, 0)
        # self.ntrainx = expand_dims(self.trainx, 0)

        model = Sequential()
        model.add(Dense(128, input_shape=((self.trainx.shape[1],)), activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(64, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(self.trainy.shape[1], activation='softmax'))
        self.model = model


    def __compile(self):
        sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        self.model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    def startTraining(self, save_path='./model'):

        self.model.fit(self.trainx, self.trainy, epochs=200, batch_size=5, verbose=1)
        self.model.save(save_path)
        

class ModelPredictor():
    def __init__(self, model_path='./model'):
        self.readModel(model_path)

    def readModel(self, model_path):
        self.model = load_model(model_path)

    def predict(self, value):
        return self.model.predict(value)
