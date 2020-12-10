# CHATBOT
Simple NLP Implementation of chatbot. This chatbot is intents based.

The Implementation of CHATBOT is in `ChatBot` & `ChatBot_v2` Modules.  
I suggest using `ChatBot_v2`... (in v2 code is encapsulated properly that's why)


**main.py contains sample code to use the chatbot**
```python
## CHATBOT V1 Training:

from ChatBot.core import Trainer
from Intents.someIntent import new_intents

trainer = Trainer(new_intents)
trainer.startTraining()

## That's IT !!! :)
```

```python
## CHATBOT V1 PREDICTION: (application)

from ChatBot.core import Trainer
from Intents.someIntent import new_intents

trainer = Trainer(new_intents)

for sentence in [
    "Hello, How do you do.",
    "I need help",
    "What can you help me with?",
    "I want to know more",
    "Bye.",
    "Thanks a lot!",
    "Thank you for your help.",
    "Why are you so funny?",
    "I want to know more.",
    "Hi, What is this?",
    "It was helpful, thanks!",
    "Hey man!",
    "I like this bot",
    "What do you do?",
    "What is your company into?",
    "Is TitanX for me?",
    "What products do you have?",
    "Why the name TitanX?",
    "I would like to know more about the products."
]:
    print('\n', sentence)
    pre = trainer.predict(sentence)
    print(pre, '\n')
    print(":> ", trainer.getResponseForClass(pre))
    print(trainer.checkClasses)
```

```python
## CHATBOT_V2 TRAINING:

from ChatBot_v2.generate import DataGenerator
from ChatBot_v2.trainer import ModelTrainer
from Intents.someIntent import new_intents

# dir_path is a path to a folder THAT EXISTS ALREADY where you will store data for your chatbot
DataGenerator.generate(new_intents, dir_path='./data')

# These files will be present in above mentioned dir_path
mt = ModelTrainer('./data/train_x_df.csv', './data/train_y_df.csv')
mt.startTraining('./model')

:)
```

```python
## CHATBOT_v2 Application

from ChatBot_v2.predictor import ModelPredictor
from Intents.someIntent import new_intents

mp = ModelPredictor('./data/classes_s.csv', './data/transformedWordDict_s.csv', model_path='./model')

## COMMAND LINE BOT :P
while True:
    ip = str(input("::< "))
    pre = mp.getPredictionFor(ip)
    print("::> ", mp.getResponseForClass(pre, new_intents))
```

I dont plan on adding anymore features to this unless needed in future !!
