## Производственный календарь

Обёртка на API https://isdayoff.ru/. Чисто для ленивых программистов. 

### **Установка**

 **Unix/Lunix**

переходим в нужную папку для установки и выполняем команды

```sh
git clone https://github.com/KlukvaMors/isdayoff.git
pip install -r isdayoff/requirements.txt
mv isdayoff/isdayoff.py .
rm -rf isdayoff
```

### **Пример**

```python
from isdayoff import ProdCalendar, DayType
from datetime import date

calendar = ProdCalendar()

if calendar.today() == DayType.WORKING:
    print('Мля, сегодня работать...')
elif calendar.today() == DayType.NOT_WORKING:
    print('Ура, выходной день!')

# закешируем результаты на январь 2020,
# так как каждый раз обращаться с серверу слишком долго
calendar.cache_month(2020, 1)

first_day = date(2020, 1, 1)
if calendar.check(first_day) == DayType.NOT_WORKING:
    print('Отдыхай, рабочий день будет '+str(calendar.next_work_day(first_day)))
```

### TODO

- добавить страны: Беларусь, Украина, Казахстан
- добавить тип: Предпраздничный день

