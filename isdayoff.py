from enum import IntEnum
from datetime import date, timedelta
from pathlib import Path
import calendar

import requests



class ServiceNotRespond(Exception):
    pass


class DayType(IntEnum):
    WORKING = 0
    NOT_WORKING = 1


class ProdCalendar:
    """Производственный календарь.  Обёртка на API https://isdayoff.ru/."""
    URL = 'https://isdayoff.ru/'
    DATE_FORMAT = '%Y%m%d'
    CACHE_FILE_FORMAT = '%sisdayoff%i%s.txt'
    LOCALES = ('ru', 'ua', 'kz', 'by')

    def __init__(self, locale: str = 'ru', cache=True, cache_dir: str = 'cache/', cache_year: int = date.today().year):
        if locale not in self.LOCALES:
            raise ValueError('locale must be in '+str(self.LOCALES))
        self.locale = locale
        self.cache = cache
        self.cache_dir = cache_dir
        if cache:
            self.cache_year(cache_year, forced=False)

    def check(self, day: date) -> DayType:
        if self.cache:
            with open(self.cache_year(day.year, forced=False)) as f:
                return DayType(int(f.read(day.timetuple().tm_yday)[-1]))
        else:
            req = requests.get(self.URL + day.strftime(self.DATE_FORMAT), params={'cc': self.locale})
            if req.status_code != 200:
                raise ServiceNotRespond
            return DayType(int(req.text))

    def today(self) -> DayType:
        return self.check(date.today())

    def next(self, day: date, dtype: DayType) -> date:
        while self.check(day) != dtype:
            day += timedelta(days=1)
        return day

    def previous(self, day: date, dtype: DayType) -> date:
        while self.check(day) != dtype:
            day -= timedelta(days=1)
        return day

    def cache_year(self, year: int, forced: bool=True) -> str:
        """Кеширование результатов на год"""
        Path(self.cache_dir).mkdir(exist_ok=True, parents=True)
        cache_file = Path(self.CACHE_FILE_FORMAT % (self.cache_dir, year, self.locale))
        if forced or not cache_file.is_file():
            res = requests.get(self.URL + 'api/getdata', params={'year': year, 'cc': self.locale})
            if not res.status_code == 200:
                raise ServiceNotRespond()
            with open(cache_file.absolute(), 'w') as f:
                f.write(res.text)

        return cache_file.absolute()


