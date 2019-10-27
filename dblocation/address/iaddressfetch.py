from abc import ABCMeta, abstractmethod


class IAddressFetch(metaclass=ABCMeta):
    @abstractmethod
    def GetByZipcode(self, zipcode):
        pass

    @abstractmethod
    def GetByAddress(self, pref, city, ku, other):
        pass
