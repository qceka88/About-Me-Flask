from datetime import datetime

from dateutil.relativedelta import relativedelta
from flask import request

"""
As a junior programmer with a strong foundation in programming and DevOps, I am driven by a passion to pioneer new 
technologies and contribute to this dynamic industry. My experience has honed my ability to excel both as a team player
 and individually, staying focused, adaptable, and goal-oriented. The combination of being a developer and a mechanical 
 engineer offers a unique perspective and meticulous attention to detail.
"""

class InfoClass:
    information = """I'm a junior in programming, driven by a deep passion and a constant eagerness to learn more about this science, utilizing it to develop new technologies and explore new frontiers. I have a solid foundation in programming and DevOps practices, aspiring to be part of this impressive and dynamic industry. Through my work experience, I've developed the ability to excel both as a team player and independently, always staying focused and achieving goals. The combination of a developer and a mechanical engineer brings a unique perspective and meticulous attention to detail.
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
