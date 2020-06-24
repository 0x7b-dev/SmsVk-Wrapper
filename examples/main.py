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

# If number already used / Если номер уже использован
sms.setNumberUsed(id)