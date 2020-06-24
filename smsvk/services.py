class ServiceModel:
    @property
    def short_name(self):
        return self.__service_short_name

    @property
    def count(self):
        return self.__count_slot

    @count.setter
    def count(self, value):
        self.__count_slot = int(value)


def object_factory(name, base_class, argnames):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key not in argnames:
                raise TypeError('Argument {} not valid for {}'.format(key, self.__class__.__name__))
            setattr(self, key, value)
        base_class.__init__(self)

    newclass = type(name, (base_class,), {'__init__': __init__})
    return newclass


class ServiceStorage:
    names = {
        'VkCom': 'vk',
        'Netflix': 'nf',
        'Google': 'go',
        'Imo': 'im',
        'Telegram': 'tg',
        'Instagram': 'ig',
        'Facebook': 'fb',
        'WhatsApp': 'wa',
        'Viber': 'vi',
        'AliBaba': 'ab',
        'KakaoTalk': 'kt',
        'Microsoft': 'mm',
        'Naver': 'nv',
        'ProtonMail': 'dp'
    }


class SmsService:
    def __init__(self):
        for name, short_name in ServiceStorage.names.items():
            object = object_factory(
                name,
                base_class=ServiceModel,
                argnames=['__service_short_name', '__count_slot']
            )(__service_short_name=short_name, __count_slot=0)
            setattr(self, '_' + name, object)

    @property
    def VkCom(self):
        """
        :rtype: smsvk.ServiceModel
        """
        return self._VkCom

    @property
    def Whatsapp(self):
        """
        :rtype: smsvk.ServiceModel
        """
        return self._Whatsapp

    @property
    def Viber(self):
        """
        :rtype: smsvk.ServiceModel
        """
        return self._Viber

    @property
    def Telegram(self):
        """
        :rtype: smsvk.ServiceModel
        """
        return self._Telegram

    @property
    def Google(self):
        """
        :rtype: smsvk.ServiceModel
        """
        return self._Google

    @property
    def Imo(self):
        """
        :rtype: smsvk.ServiceModel
        """
        return self._Imo

    def Instagram(self):
        """
        :rtype: smsvk.ServiceModel
        """
        return self._Instagram

    @property
    def KakaoTalk(self):
        """
        :rtype: smsvk.ServiceModel
        """
        return self._KakaoTalk

    @property
    def AliBaba(self):
        """
        :rtype: smsvk.ServiceModel
        """
        return self._AliBaba

    def Netflix(self):
        """
        :rtype: smsvk.ServiceModel
        """
        return self._Netflix

    def Facebook(self):
        """
        :rtype: smsvk.ServiceModel
        """
        return self._Facebook

    def Microsoft(self):
        """
        :rtype: smsvk.ServiceModel
        """
        return self._Naver

    def Naver(self):
        """
        :rtype: smsvk.ServiceModel
        """
        return self._Microsoft

    def ProtonMail(self):
        """
        :rtype: smsvk.ServiceModel
        """
        return self._ProtonMail
