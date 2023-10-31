import json
import pickle
import random

import nltk
import numpy as np
from keras.models import load_model
from nltk.stem import WordNetLemmatizer

nltk.download('popular')
nltk.download('omw-1.4')
nltk.download("punkt")
nltk.download("wordnet")
lemmatizer = WordNetLemmatizer()


class TrainedData:

    def __init__(self):
        self.model = load_model('model.h5')
        self.intents = json.loads(open('data.json').read())
        self.words = pickle.load(open('texts.pkl', 'rb'))
        self.labels = pickle.load(open('labels.pkl', 'rb'))


class Lemmatizer:

    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [lemmatizer.lemmatize(w.lower()) for w in sentence_words]
        return sentence_words


class BOW(TrainedData, Lemmatizer):

    def bag_of_words(self, sentence):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0] * len(self.words)
        for s in sentence_words:
            for i, word in enumerate(self.words):
                if s == word:
                    bag[i] = 1
        return (np.array(bag))


class Predict(BOW):
    ERROR_THRESHOLD = 0.25

    def prediction(self, sentence):
        p = self.bag_of_words(sentence)
        predict_result = self.model.predict(np.array(p))[0]
        result = [[i, r] for i, r in enumerate(predict_result) if r > self.ERROR_THRESHOLD]
        result.sort(key=lambda x: x[1], reverse=True)

        new_data = []

        for r in result:
            new_data.append({"intent": self.labels[r[0]], "probability": str(r[1])})

        return new_data


class GetResponse(TrainedData):

    def get_response(self, user_msg):
        tag = user_msg[0]['intent']
        list_of_intents = self.intents['intents']

        for intent in list_of_intents:
            if intent['tag'] == tag:
                result = random.choice(intent['responses'])

                return result


class BotResponse(GetResponse, Predict):

    def chatbot_response(self, received_message):
        intents = self.prediction(received_message)
        result = self.get_response(intents)

        return result
