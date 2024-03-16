from flask import render_template, request, jsonify, redirect, url_for
from flask.views import View

from WebApp.helpers import MyDevice, MyTime, InfoClass





class IndexView(View, MyTime, InfoClass):
    methods = ["GET", "POST"]

    def __init__(self, template):
        self.template = template

    def dispatch_request(self):
        self.context.update(self.active_coding_time())
        return render_template(self.template, **self.context)


class HobbiesView(View, MyDevice, MyTime):
    methods = ["GET"]

    def __init__(self, template):
        self.template = template

    def dispatch_request(self):
        context = {"device": self.device_detect()}
        return render_template(self.template, **context)


class BotResponseView(View):
    methods = ["GET"]

    def __init__(self, bot):
        self.bot = bot

    def dispatch_request(self):
        user_text = request.args.get("message")
        response = self.bot.chatbot_response(user_text)
        return jsonify(response)


class PageNotFoundView(View):
    def dispatch_request(self, **kwargs):
        return redirect(url_for("index_view"))
