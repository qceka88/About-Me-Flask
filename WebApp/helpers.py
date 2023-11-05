from datetime import datetime

from dateutil.relativedelta import relativedelta
from flask import request


class InfoClass:
    information = """Newbie in programming, but with a big passion and constant willingness to learn more about 
            this science and to use it to develop new technologies and cross new borders. Have a good basis from SoftUni 
            in programming and DevOps. I want to be a part of this impressive and dynamic industry. I have also a 
            master's degree from Technical University Varna as 'Naval Architect/Hull Design engineer'. Also, have 
            twelve years of experience in the shipbuilding industry. Good team player
            or good as a single unit, no matter of the situation always stays in condition.
            """
    context = {
        "CV": "/static/pdf/Yanko_CV.pdf",
        "personal_information": information,
    }


class MyDevice:

    @staticmethod
    def device_detect():
        user_agent = request.headers.get("User-Agent")

        if "iphone" in user_agent.lower() or 'android' in user_agent.lower():
            return True

        return False


class MyTime:

    @staticmethod
    def active_coding_time():
        start_date = datetime(year=2022, month=5, day=7, hour=10, minute=0, second=0, microsecond=0)
        today = datetime.now()
        my_time = relativedelta(today, start_date)

        return {"years": my_time.years, "months": my_time.months, "days": my_time.days}
