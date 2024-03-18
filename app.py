# import json
# import pickle
#
# import nltk
from flask import Flask
# from keras.models import load_model
#
# from ChatBot.chat_bot_actions import BotResponse
# from WebApp.helpers import unique_extension
from WebApp.views import IndexView, HobbiesView #, Page404View, BotResponseView

# nltk.download("popular")
# nltk.download("omw-1.4")
# nltk.download("punkt")
# nltk.download("wordnet")
#
# # Initialise Chatbot Object
# model = load_model("ChatBot/model.h5")
# intents = json.loads(open("ChatBot/training_source.json").read())
# words = pickle.load(open("ChatBot/texts.pkl", "rb"))
# labels = pickle.load(open("ChatBot/labels.pkl", "rb"))
# bot = BotResponse(model, intents, words, labels)

# Initialise Flask App
app = Flask(__name__,
            static_url_path="/static",
            static_folder="static",
            template_folder="templates")
unique_extension = 'ho'
# Config Secret Key
app.config["SECRET_KEY"] = "FlasK/Pythonfi234j2fr2j-939jsdf2sdf43243a2"
# urlpatterns
app.add_url_rule("/", view_func=IndexView.as_view("index_view", "index.html"))
# app.add_url_rule("/get", view_func=BotResponseView.as_view("bot_response", bot))
app.add_url_rule(f"/{unique_extension}", view_func=HobbiesView.as_view("hobbies_view", "hobbies.html"))
# app.add_url_rule("/<path:invalid_path>", view_func=Page404View.as_view("page_not_found"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)

# TODO: Add more data for ChatBot

