import json

import requests
from .exceptions import NoBalance, NoNumbers, Error


class SmsVk():
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'http://smsvk.net/stubs/handler_api.php?api_key={0}'.format(self.api_key)

    def getBalance(self):
        response = requests.get(url=self.url + '&action=getBalance').text.split(":")
        return response[1]

    def getNumbersStatus(self):
        response = requests.get(url=self.url + '&action=getNumbersStatus')
        return json.loads(response.text)

    def getNumber(self, service):
        service = getattr(service, '__service_short_name').split('_')[0]
        response = requests.get(url=self.url + '&action=getNumber&service={0}'.format(service)).text
        if 'ACCESS_NUMBER' in response:
            splited = response.split(':')
            return splited[1], splited[2]
        elif 'NO_NUMBERS' in response:
            raise NoNumbers
        elif 'NO_BALANCE' in response:
            raise NoBalance

    def getStatus(self, numberID):
        response = requests.get(url=self.url + '&action=getStatus&id={0}'.format(str(numberID))).text
        return response


    def __setNumberStatus(self, status, numberID):
        response = requests.get(url=self.url + '&action=setStatus&status={0}&id={1}'.format(str(status), str(numberID))).text
        if 'ERROR' in response:
            raise Error
        return response

    def setNumberReady(self, numberID):
        self.__setNumberStatus(status=1, numberID=numberID)

    def setNumberNewCode(self, numberID):
        self.__setNumberStatus(status=3, numberID=numberID)

    def setNumberFinish(self, numberID):
        self.__setNumberStatus(status=6, numberID=numberID)

    def setNumberUsed(self, numberID):
        self.__setNumberStatus(status=8, numberID=numberID)
