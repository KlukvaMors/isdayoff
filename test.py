import unittest
from isdayoff import DayType, ProdCalendar
from datetime import timedelta, date
import calendar


class HolidaysTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ru = ProdCalendar(locale='ru', freshness=timedelta(days=1))
        self.ua = ProdCalendar(locale='ua', freshness=timedelta(days=1))
        self.by = ProdCalendar(locale='by', freshness=timedelta(days=1))
        self.us = ProdCalendar(locale='us', freshness=timedelta(days=1))
        self.curr_year = date.today().year

    def test_russian_holidays(self):
        self.assertEqual(self.ru.check(date(self.curr_year, 1, 1)), DayType.NOT_WORKING)
        self.assertEqual(self.ru.check(date(self.curr_year, 1, 7)), DayType.NOT_WORKING)
        self.assertEqual(self.ru.check(date(self.curr_year, 2, 23)), DayType.NOT_WORKING)
        self.assertEqual(self.ru.check(date(self.curr_year, 3, 8)), DayType.NOT_WORKING)
        self.assertEqual(self.ru.check(date(self.curr_year, 5, 1)), DayType.NOT_WORKING)
        self.assertEqual(self.ru.check(date(self.curr_year, 5, 9)), DayType.NOT_WORKING)
        self.assertEqual(self.ru.check(date(self.curr_year, 6, 12)), DayType.NOT_WORKING)
        self.assertEqual(self.ru.check(date(self.curr_year, 11, 4)), DayType.NOT_WORKING)

    def test_ukrainian_holidays(self):
        self.assertEqual(self.ua.check(date(self.curr_year, 1, 1)), DayType.NOT_WORKING)
        self.assertEqual(self.ua.check(date(self.curr_year, 1, 7)), DayType.NOT_WORKING)
        self.assertEqual(self.ua.check(date(self.curr_year, 3, 8)), DayType.NOT_WORKING)
        self.assertEqual(self.ua.check(date(self.curr_year, 5, 1)), DayType.NOT_WORKING)
        self.assertEqual(self.ua.check(date(self.curr_year, 5, 9)), DayType.NOT_WORKING)
        self.assertEqual(self.ua.check(date(self.curr_year, 6, 28)), DayType.NOT_WORKING)
        self.assertEqual(self.ua.check(date(self.curr_year, 8, 24)), DayType.NOT_WORKING)
        self.assertEqual(self.ua.check(date(self.curr_year, 10, 14)), DayType.NOT_WORKING)
        self.assertEqual(self.ua.check(date(self.curr_year, 12, 25)), DayType.NOT_WORKING)

    def test_belorussian_holidays(self):
        self.assertEqual(self.by.check(date(self.curr_year, 1, 1)), DayType.NOT_WORKING)
        self.assertEqual(self.by.check(date(self.curr_year, 1, 7)), DayType.NOT_WORKING)
        self.assertEqual(self.by.check(date(self.curr_year, 3, 8)), DayType.NOT_WORKING)
        self.assertEqual(self.by.check(date(self.curr_year, 5, 1)), DayType.NOT_WORKING)
        self.assertEqual(self.by.check(date(self.curr_year, 5, 9)), DayType.NOT_WORKING)
        self.assertEqual(self.by.check(date(self.curr_year, 7, 3)), DayType.NOT_WORKING)

    def test_usa_holidays(self):
        self.assertEqual(self.us.check(date(self.curr_year, 1, 1)), DayType.NOT_WORKING)
        self.assertEqual(self.us.check(calendar.Calendar(0).monthdatescalendar(self.curr_year, 1)[3][0]),
                         DayType.NOT_WORKING)
        self.assertEqual(self.us.check(calendar.Calendar(0).monthdatescalendar(self.curr_year, 2)[3][0]),
                         DayType.NOT_WORKING)
        self.assertEqual(self.us.check(calendar.Calendar(0).monthdatescalendar(self.curr_year, 5)[-1][0]),
                         DayType.NOT_WORKING)
        self.assertEqual(self.us.check(date(self.curr_year, 7, 4)), DayType.NOT_WORKING)

        self.assertEqual(self.us.check(calendar.Calendar(0).monthdatescalendar(self.curr_year, 9)[1][0]),
                         DayType.NOT_WORKING)
        self.assertEqual(self.us.check(calendar.Calendar(0).monthdatescalendar(self.curr_year, 10)[2][0]),
                         DayType.NOT_WORKING)
        self.assertEqual(self.us.check(date(self.curr_year, 11, 11)), DayType.NOT_WORKING)
        self.assertEqual(self.us.check(calendar.Calendar(3).monthdatescalendar(self.curr_year, 11)[4][0]),
                         DayType.NOT_WORKING)
        self.assertEqual(self.us.check(date(self.curr_year, 12, 25)), DayType.NOT_WORKING)


if __name__ == '__main__':
    unittest.main()
