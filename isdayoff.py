from enum import IntEnum
from datetime import date, timedelta
from typing import Optional
import calendar

import requests
from joblib import Memory


class ServiceNotRespond(Exception):
    pass


class DayType(IntEnum):
    WORKING = 0
    NOT_WORKING = 1


class ProdCalendar:
    """Производственный календарь.  Обёртка на API https://isdayoff.ru/. Есть кеширование результатов"""
    URL = 'https://isdayoff.ru/'
    DATE_FORMAT = '%Y%m%d'
    CACHE_DIR = 'cache'

    def __init__(self, cache=True):
        self.memory = Memory(self.CACHE_DIR if cache else None, verbose=1)

    def _check(self, day: date) -> DayType:
        req = requests.get(self.URL + day.strftime(self.DATE_FORMAT))
        if req.status_code != 200:
            raise ServiceNotRespond
        return DayType(int(req.text))

    def check(self, day: date) -> DayType:
        return self.memory.cache(self._check)(day)

    def today(self) -> DayType:
        return self.check(date.today())

    def next_work_day(self, day: date) -> date:
        while self.check(day) != DayType.WORKING:
            day += timedelta(days=1)
        return day

    def previous_work_day(self, day: date) -> date:
        while self.check(day) != DayType.WORKING:
            day -= timedelta(days=1)
        return day

    def cache_month(self, year: int, month: int):
        """Кеширование результатов на месяц"""
        for day in range(1, calendar.monthrange(year, month)[1]+1):
            self.check(date(year, month, day))