import json
import logging
import pickle
import random

import nltk
import numpy as np
import tensorflow as tf
from keras.layers import Dense, Dropout
from keras.models import Sequential
from nltk.stem import WordNetLemmatizer

nltk.download("popular")
nltk.download("omw-1.4")
nltk.download("punkt")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()


class Data:

    def __init__(self, source_file):
        self.words = []
        self.labels = []
        self.documents = []
        self.training = []
        self.ignore_symbols = ["?", "!"]
        self.intents = json.loads(source_file)
        self.model = None


class Tokenizer(Data):

    def process_initial_data_from_source(self):
        for intent in self.intents["intents"]:
            for pattern in intent["patterns"]:
                tokenized_words = nltk.word_tokenize(pattern)
                self.words.extend(tokenized_words)

                self.documents.append((tokenized_words, intent["tag"]))

                if intent["tag"] not in self.labels:
                    self.labels.append(intent["tag"])
        self.labels = sorted(list(set(self.labels)))


class Lemmatizer(Tokenizer):

    def lemmatize_and_lower_words(self):
        words = []
        for word in self.words:
            if word not in self.ignore_symbols:
                words.append(lemmatizer.lemmatize(word.lower()))
        self.words = sorted(list(set(words)))


class AddDataForChatBot(Lemmatizer):

    def dump_words_and_classes(self):
        file = open("ChatBot/texts.pkl", "r")
        file.close()
        file2 = open("ChatBot/texts.pkl", "r")
        file2.close()
        pickle.dump(self.words, open("ChatBot/texts.pkl", "wb"))
        pickle.dump(self.labels, open("ChatBot/labels.pkl", "wb"))


class Trainer(AddDataForChatBot):
    train_x = []
    train_y = []

    def training_set(self):
        output_empty = [0] * len(self.labels)

        for document in self.documents:
            bag = []
            pattern_words = document[0]
            pattern_words = [lemmatizer.lemmatize(w.lower()) for w in pattern_words]

            for word in self.words:
                if word in pattern_words:
                    bag.append(1)
                else:
                    bag.append(0)

            output_row = list(output_empty)
            output_row[self.labels.index(document[1])] = 1

            self.training.append([bag, output_row])

    def shuffle_and_transform_into_array(self):
        random.shuffle(self.training)
        self.training = np.array(self.training)

    def train_and_test_lists(self):
        self.train_x = list(self.training[:, 0])
        self.train_y = list(self.training[:, 1])


class Model(Trainer):

    def create_model(self):
        self.model = Sequential()
        self.model.add(Dense(256, input_shape=(len(self.train_x[0]),), activation="relu"))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(128, activation="relu"))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(64, activation="relu"))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(len(self.train_y[0]), activation="softmax"))

    def compile_model(self):
        sgd = tf.keras.optimizers.legacy.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
        self.model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])


class FitModel(Model):
    hist = None

    def fit_and_save_model(self):
        self.hist = self.model.fit(np.array(self.train_x), np.array(self.train_y), epochs=200, batch_size=5, verbose=1)

    def save_model(self):
        file = open("ChatBot/model.h5", "r")
        file.close()
        self.model.save("ChatBot/model.h5", self.hist)


data_file = open("ChatBot/training_source.json").read()
model = FitModel(data_file)
model.process_initial_data_from_source()
model.lemmatize_and_lower_words()
model.dump_words_and_classes()
model.training_set()
model.shuffle_and_transform_into_array()
model.train_and_test_lists()
model.create_model()
model.compile_model()
model.fit_and_save_model()
model.save_model()
logging.info(msg="Training complete!")
