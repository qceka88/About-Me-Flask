from flask import render_template, request, jsonify, redirect, url_for
from flask.views import View

from WebApp.helpers import MyDevice, MyTime, InfoClass


class IndexView(View, MyTime, InfoClass):
    """
        Class view for main page. Add information from parent classes to context.

        :returns: render for main page.
    """
    methods = ["GET", "POST"]

    def __init__(self, template):
        self.template = template

    def dispatch_request(self):
        self.context.update(self.active_coding_time())
        return render_template(self.template, **self.context)


class HobbiesView(View, MyDevice, MyTime):
    """
        Class view for hobbies page. It is hidden Easter Egg.

        :returns: render for hobbies page.
    """
    methods = ["GET"]

    def __init__(self, template):
        self.template = template

    def dispatch_request(self):
        context = self.device_os_detect()

        return render_template(self.template, **context)


class BotResponseView(View):
    """
        Class that handle user messages to communicate with  the chatbot.

        :returns: chatbot response string format.
    """
    methods = ["GET"]

    def __init__(self, bot):
        self.bot = bot

    def dispatch_request(self):
        user_text = request.args.get("message")
        response = self.bot.chatbot_response(user_text)

        return jsonify(response)


class Page404View(View):
    """
        Class for 404 handler. When user generate 404 error is redirected to 'index_view'

        :returns: redirect to home page.
    """
    methods = ["GET", "POST"]

    def dispatch_request(self, **kwargs):
        return redirect(url_for("index_view"))
