from enum import IntEnum
from datetime import date
from functools import lru_cache
from typing import Optional
import requests

URL = 'https://isdayoff.ru/'
DATE_FORMAT = '%Y%m%d'


class DayType(IntEnum):
    WORKING = 0
    NOT_WORKING = 1


@lru_cache
def check(day: date) -> Optional[DayType]:
    req = requests.get(URL+day.strftime(DATE_FORMAT))
    if req.status_code != 200:
        return None
    return DayType(int(req.text))


def today() -> Optional[DayType]:
    return check(date.today())