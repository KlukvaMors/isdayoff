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
    print('Но выходные будут ' + str(calendar.next(date.today(), DayType.NOT_WORKING)))
elif calendar.today() == DayType.NOT_WORKING:
    print('Ура, выходной день!')
    print('Но работать надо ' + str(calendar.next(date.today(), DayType.WORKING)))
```

### Функциональность

- Поддержка стран: Россия, Беларусь, Украина, Казахстан
- Поддержка кеширования результатов (по умолчанию включена)



### TODO

- добавить страны: США
- добавить тип: Предпраздничный день
- уйти от зависмостей в внешних библиотек (requests)

