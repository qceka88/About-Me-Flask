import json
import pickle
from datetime import datetime

import nltk
from dateutil.relativedelta import relativedelta
from flask import Flask, render_template, request, jsonify
from flask.views import View
from keras.models import load_model

from ChatBot.chat_bot_actions import BotResponse

nltk.download('popular')
nltk.download('omw-1.4')
nltk.download("punkt")
nltk.download("wordnet")

app = Flask(__name__,
            static_url_path='/static',
            static_folder='static',
            template_folder='templates')

app.config['SECRET_KEY'] = 'FlasK/Pythonfi234j2fr2j-939jsdf2sdf43243a2'  # Change this to your own secret key

information = """
    Newbie in programming, but with a big passion and constant willingness to learn more about this science and to use it to 
    develop new technologies and cross new borders. Have a good basis from SoftUni in programming and DevOps. I want to
    be a part of this impressive and dynamic industry. I have also a master's degree from Technical University Varna as
    'Naval Architect/Hull Design engineer'. Also, have twelve years of experience in the shipbuilding industry. Good team player
    or good as a single unit, no matter of the situation always stays in condition.
"""

test_context = {
    "CV": "/static/pdf/Yanko_CV.pdf",
    "personal_information": information,
}

# TODO: In the future add Modal func to certificate images (Find how to modal more than one picture)
# TODO: Train the chatbot


model = load_model('ChatBot/model.h5')
intents = json.loads(open('ChatBot/training_source.json').read())
words = pickle.load(open('ChatBot/texts.pkl', 'rb'))
labels = pickle.load(open('ChatBot/labels.pkl', 'rb'))

bot = BotResponse(model, intents, words, labels)


class MyDevice:
    def device_detect(self):
        user_agent = request.headers.get("User-Agent")

        if "iphone" in user_agent.lower() or 'android' in user_agent.lower():
            return True

        return False


class MyTime:

    def active_coding_time(self):
        start_date = datetime(year=2022, month=5, day=7, hour=10, minute=0, second=0, microsecond=0)
        today = datetime.now()
        my_time = relativedelta(today, start_date)
        return {"years": my_time.years, "months": my_time.months, "days": my_time.days}


class IndexView(View, MyDevice, MyTime):
    methods = ['GET', 'POST']

    def __init__(self, some_context, template):
        self.some_context = some_context
        self.template = template

    def dispatch_request(self):
        self.some_context['mobile_device'] = self.device_detect()
        self.some_context.update(self.active_coding_time())

        return render_template(self.template, **self.some_context)


class BotResponseView(View):
    methods = ['GET']

    def dispatch_request(self):
        user_text = request.args.get('message')
        response = bot.chatbot_response(user_text)
        return jsonify(response)


app.add_url_rule('/', view_func=IndexView.as_view("class_view", test_context, "index.html"))
app.add_url_rule('/get', view_func=BotResponseView.as_view('bot_response'))

if __name__ == '__main__':
    app.run()
