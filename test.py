import unittest
from isdayoff import DayType, ProdCalendar
from datetime import timedelta, date


class HolidaysTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ru = ProdCalendar(locale='ru', freshness=timedelta(days=1))
        self.ua = ProdCalendar(locale='ua', freshness=timedelta(days=1))
        self.by = ProdCalendar(locale='by', freshness=timedelta(days=1))
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


if __name__ == '__main__':
    unittest.main()
