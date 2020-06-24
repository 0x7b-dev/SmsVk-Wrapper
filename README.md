# SmsVk-Wrapper

### Русский

Обёртка для API сервиса smsvk.net

### Установка
Вы можете воспользоваться pip для установки
```
$ pip install SmsVk-Wrapper --upgrade
```
Или установить используя исходники
```
pip install git+https://github.com/Spec122/SmsVk-Wrapper
```


### English

Wrapper for smsvk.net API

### Installation
You can install package using pip
```
$ pip install SmsVk-Wrapper --upgrade
```
Or from source
```
pip install git+https://github.com/Spec122/SmsVk-Wrapper
```

### Example / Пример
```python
from smsvk.actions import SmsVk
from smsvk.services import SmsService

# Your token / Ваш токен
sms = SmsVk("Your Token")

# Check your balance / Выводит баланс
sms.getBalance()

# Get activation id and number for Telegram / Получаем id активации и номер на примере Телеграмма
id, number = sms.getNumber(SmsService().Telegram)

# Get status with SMS / Получаем статус и СМС
print(sms.getStatus(id))

# Get one more sms / Запрашиваем еще одну смс
sms.setNumberNewCode(id)

# When finished working with number / Когда завершили работу с номером
sms.setNumberFinish(id)

# If number already used / Если номер уже использован
sms.setNumberUsed(id)
```
