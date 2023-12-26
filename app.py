import json
import pickle

import nltk
from flask import Flask

from keras.models import load_model

from ChatBot.chat_bot_actions import BotResponse
from WebApp.views import IndexView, BotResponseView

nltk.download('popular')
nltk.download('omw-1.4')
nltk.download("punkt")
nltk.download("wordnet")

# Initialise Chatbot Object
model = load_model('ChatBot/model.h5')
intents = json.loads(open('ChatBot/training_source.json').read())
words = pickle.load(open('ChatBot/texts.pkl', 'rb'))
labels = pickle.load(open('ChatBot/labels.pkl', 'rb'))
bot = BotResponse(model, intents, words, labels)

# initialise Flask App
app = Flask(__name__,
            static_url_path='/static',
            static_folder='static',
            template_folder='templates')

# Config Secret Key
app.config['SECRET_KEY'] = 'FlasK/Pythonfi234j2fr2j-939jsdf2sdf43243a2'

# Define URL
app.add_url_rule('/', view_func=IndexView.as_view("class_view", "index.html"))
app.add_url_rule('/get', view_func=BotResponseView.as_view('bot_response', bot))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)


# TODO: Study experience/work experience button -  CENTER - Add 3D effect in button
# TODO: CENTER CHAT WINDOW IN MOBILE VERSION

