## Производственный календарь

Обёртка на API https://isdayoff.ru/. Чисто для ленивых программистов. Автор данной библиотеки не связан с API.

### **Установка**

 **Unix/Lunix**

переходим в нужную папку для установки и выполняем команды

```sh
git clone https://github.com/KlukvaMors/isdayoff.git
pip install -r isdayoff/requirements.txt
mv isdayoff/isdayoff.py .
rm -rf isdayoff
```



### Функциональность

- Проверка любого дня на статус выходного/рабочего
- Поддержка стран: Россия, Беларусь, Украина, Казахстан, США (только на федеральном уровне)
- Поддержка кеширования результатов (по умолчанию включена)



### **Базовые примеры**

Выходной ли сегодня в США?

```python
from isdayoff import ProdCalendar, DayType
from datetime import date, timedelta

calendar = ProdCalendar(locale='us')

if calendar.today() == DayType.WORKING:
    print('Рабочий день')
elif calendar.today() == DayType.NOT_WORKING:
    print('Выходной')
```

Когда наступит ближайший выходной (относительно сегодня)?

```python
calendar.next(date.today(), DayType.NOT_WORKING))
```

Когда был ближайший рабочий день (относительно сегодня)?

```python
calendar.previous(date.today(), DayType.WORKING))
```

Проверть любой другой день

```python
calendar.check(date(2020, 9, 17))== DayType.WORKING # True
```



### **Кеширование**

Исходный API https://isdayoff.ru/ относительно медленно отвечает на запросы. Именно поэтому в этой библиотеке предусмотрено кеширование, которое работает по умолчанию. Отключается кеширование таким способом:

```python
calendar = ProdCalendar(cache=False)
```

Данные кеша хранятся в папке `<папка установки>/cache`. Установить другое место можно:

```python
calendar = ProdCalendar(cache_dir='your/another_place/for/cache')
```

Понятно, что данные кеша могут устареть. Поэтому следует регулярно обновлять данные кеша. По умолчанию установлено обновление каждые 30 дней, но вы можете сделать чаще.

```python
calendar = ProdCalendar(freshness=timedelta(days=7))
```



### TODO

- добавить тип: Предпраздничный день

