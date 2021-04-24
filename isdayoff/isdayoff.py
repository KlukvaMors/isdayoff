from enum import IntEnum
from datetime import date, timedelta, datetime
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
    LOCALES = ('ru', 'ua', 'kz', 'by', 'us')

    def __init__(self, locale: str = 'ru', cache: bool = True, cache_dir: str = 'cache/',
                 cache_year: int = date.today().year, freshness: timedelta = timedelta(days=30)):
        if locale not in self.LOCALES:
            raise ValueError('locale must be in '+str(self.LOCALES))
        self.locale = locale
        self.cache = cache
        self.cache_dir = cache_dir
        self.freshness = freshness
        if cache:
            self.cache_year(cache_year, forced=False)

    def check(self, day: date) -> DayType:
        if self.cache:
            return self._get_cache(day)
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
            self._write_cache(year, cache_file)
        elif not self._is_cache_fresh(cache_file):
            self._write_cache(year, cache_file)

        return cache_file.absolute()

    def _write_cache(self, year, cache_file):
        res = requests.get(self.URL + 'api/getdata', params={'year': year, 'cc': self.locale})
        if not res.status_code == 200:
            raise ServiceNotRespond()
        with open(cache_file.absolute(), 'w') as f:
            f.write(datetime.now().isoformat()+'\n')
            f.write(res.text)

    def _is_cache_fresh(self, cache_file) -> bool:
        with open(cache_file.absolute()) as f:
            return datetime.fromisoformat(f.readline().strip()) + self.freshness >= datetime.now()

    def _get_cache(self, day: date) -> DayType:
        with open(self.cache_year(day.year, forced=False)) as f:
            f.readline()  # pass cache date
            return DayType(int(f.readline(day.timetuple().tm_yday)[-1]))



