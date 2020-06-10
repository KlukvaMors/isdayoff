## Производственный календарь

Обёртка на API https://isdayoff.ru/. Чисто для ленивых программистов. Требуется установка [requests](https://pypi.org/project/requests/)



**Пример**

```python
from isdayoff import DayType
import isdayoff
from datetime import date

if isdayoff.check(date(2020, 1, 1)) == DayType.NOT_WORKING:
    print("УРА!")
```



В качестве бонуса добавлено кеширование результатов.

### TODO

- реализовать все возможности API

