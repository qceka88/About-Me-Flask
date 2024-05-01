from datetime import datetime
from random import choice
from string import ascii_letters, digits

from dateutil.relativedelta import relativedelta
from flask import request


class InfoClass:
    """
        Base Info class representing some initial information for me.
    """
    information = """I'm a junior in programming, driven by a deep passion and a constant eagerness to learn more about 
        this science, utilizing it to develop new technologies and explore new frontiers. I have a solid foundation in 
        programming and DevOps practices, aspiring to be part of this impressive and dynamic industry. Through my work 
        experience, I've developed the ability to excel both as a team player and independently, always staying focused and 
        achieving goals. The combination of a developer and a mechanical engineer brings a unique perspective and meticulous 
        attention to detail.
                """
    context = {
        "CV": "/static/pdf/Yanko_CV.pdf",
        "personal_information": information,
    }


class MyDevice:
    """
        Class that is used to detect the device OS of client and to return it as image.

        :returns: image file.
    """
    __device_os_image_map = {
        "windows": "/static/img/visitors/windows-visitor.png",
        "linux": "/static/img/visitors/linux-visitor.png",
        "android": "/static/img/visitors/android-visitor.png",
        "apple": "/static/img/visitors/apple-visitor.png",
        "playstation": "/static/img/visitors/ps-visitor.png",
        "no_device": "/static/img/visitors/no-device.png",
    }

    def device_os_detect(self):
        user_agent = request.headers.get("User-Agent").lower()

        if "windows" in user_agent:
            user_device_os = "windows"
        elif "android" in user_agent:
            user_device_os = "android"
        elif "iphone" in user_agent or "ipad" in user_agent or "macintosh" in user_agent:
            user_device_os = "apple"
        elif "playstation" in user_agent:
            user_device_os = "playstation"
        elif "linux" in user_agent and "android" not in user_agent:
            user_device_os = "linux"
        else:
            user_device_os = "no_device"

        return {
            'device': self.__device_os_image_map[user_device_os],
            'user_agent': user_agent,
        }


class MyTime:
    """
        Class that calculate time from initial data that I stared to practice programming.

        :returns: dict with calculated period in {'years': .., 'months': .., 'days': ..}  format.
    """

    @staticmethod
    def active_coding_time():
        start_date = datetime(year=2022, month=5, day=7, hour=10, minute=0, second=0, microsecond=0)
        today = datetime.now()
        my_time = relativedelta(today, start_date)

        return {"years": my_time.years, "months": my_time.months, "days": my_time.days}


def get_unique_url_extension():
    """
        Function that generate unique string fifty characters long, randomly chosen.

        :returns: Randomly chosen length of string and randomly chosen characters.
    """
    alpha_digits = str(digits) + ascii_letters
    url_extension_length = choice(range(50, 101))
    return ''.join(choice(alpha_digits) for _ in range(url_extension_length))


unique_extension = get_unique_url_extension()
