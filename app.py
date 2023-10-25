from datetime import datetime

from dateutil.relativedelta import relativedelta
from flask import Flask, render_template
from flask.views import View

app = Flask(__name__,
            static_url_path='/static',
            static_folder='static',
            template_folder='templates')

app.config['SECRET_KEY'] = 'FlasK/Pythonfi234j2fr2j-939jsdf2sdf43243a2'  # Change this to your own secret key

information = """
    Newbie in programming, but with a big passion and constant willingness to learn more about this science and to use it to 
    develop new technologies and cross new borders. Have a good basis from SoftUni in programming and DevOps. I want to
    be a part of this impressive and dynamic industry. I have also master degree from Technical University Varna as
    'Naval Architect/Hull Design engineer'. Also have twelve years experience in shipbuilding industry. Good team player
    or good as single unit, no mather of the situation always stay in condition.
"""

test_context = {
    "CV": ["/static/pdf/Yanko_CV.pdf", 1],
    "personal_information": information,
}


class MyTime:

    def active_coding_time(self):
        start_date = datetime(year=2022, month=5, day=7, hour=10, minute=0, second=0, microsecond=0)
        today = datetime.now()
        my_time = relativedelta(today, start_date)
        return {"years": my_time.years, "months": my_time.months, "days": my_time.days}


class IndexView(View, MyTime):

    def __init__(self, some_context, template):
        self.some_context = some_context
        self.template = template

    def dispatch_request(self):
        self.some_context.update(self.active_coding_time())
        return render_template(self.template, **self.some_context)


app.add_url_rule('/', view_func=IndexView.as_view("class_view", test_context, "index.html"))

if __name__ == '__main__':
    app.run(debug=True)
