
from dblocation.address.iaddressfetch import IAddressFetch
from dblocation.address.addressdata import AddressData
from dblocation.addressparsing.jpaddressparser import JpAddressParser
import urllib


class LocationApiUseCase:
    def __init__(self, addressFetch: IAddressFetch):
        self.__addressFetch = addressFetch

    def __convertAsOk(self, addressData: AddressData):
        id = '"Id":"{id}"'.format(id=addressData.Id)
        code = '"Code":"{code}"'.format(code=addressData.Code)
        zipcode = '"Zipcode":"{zipcode}"'.format(zipcode=addressData.Zipcode)
        coord = '"Coord":{{"Lat":{lat},"Lon":{lon}}}'.format(lat=addressData.Latitude, lon=addressData.Longitude)
        addr = '"Address":{{"Pref":"{pref}","Gun":"{gun}","City":"{city}","Ku":"{ku}","Other":"{other}"}}'.format(
            pref=urllib.parse.quote(addressData.Prefecture),
            gun=urllib.parse.quote(addressData.Gun),
            city=urllib.parse.quote(addressData.City),
            ku=urllib.parse.quote(addressData.Ku),
            other=urllib.parse.quote(addressData.Other))
        kana = '"AddressKana":{{"Pref":"{pref}","Gun":"{gun}","City":"{city}","Ku":"{ku}","Other":"{other}"}}'.format(
            pref=urllib.parse.quote(addressData.PrefectureKana),
            gun=urllib.parse.quote(addressData.GunKana),
            city=urllib.parse.quote(addressData.CityKana),
            ku=urllib.parse.quote(addressData.KuKana),
            other=urllib.parse.quote(addressData.OtherKana))
        return '{"result":"ok","data":{' + id + ',' + code + ',' + zipcode + ',' + coord + ',' + addr + ',' + kana + '}}'

    def __throwError(self, detail):
        return '{{"result":"error","message":"{message}"}}'.format(message=detail)

    def __convert(self, addressData: AddressData):
        if addressData is None:
            return self.__throwError('not_found')
        return self.__convertAsOk(addressData)

    def Get(self, zipcode, address):
        if len(zipcode) == 7:
            return self.__convert(self.__addressFetch.GetByZipcode(zipcode))
        jpAddress = JpAddressParser(address)
        return self.__convert(self.__addressFetch.GetByAddress(jpAddress.Pref, jpAddress.City, jpAddress.Ku, jpAddress.Other))


