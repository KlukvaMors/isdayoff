"""Производственный календарь.  Обёртка на API https://isdayoff.ru/. Есть кеширование результатов"""
from enum import IntEnum
from datetime import date, timedelta
from functools import lru_cache
from typing import Optional
import requests
from joblib import Memory

URL = 'https://isdayoff.ru/'
DATE_FORMAT = '%Y%m%d'
CACHE_DIR = "cache"

memory = Memory(CACHE_DIR)


class DayType(IntEnum):
    WORKING = 0
    NOT_WORKING = 1


@memory.cache
def check(day: date) -> Optional[DayType]:
    req = requests.get(URL+day.strftime(DATE_FORMAT))
    if req.status_code != 200:
        return None
    return DayType(int(req.text))


def today() -> Optional[DayType]:
    return check(date.today())
