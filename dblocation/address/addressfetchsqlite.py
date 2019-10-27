
from .iaddressfetch import IAddressFetch
from .addressdata import AddressData
import sqlite3


class AddressFetchSqlite(IAddressFetch):

    def __init__(self, datebaseName):
        self.__connection = sqlite3.connect(datebaseName)
        self.__cursor = self.__connection.cursor()
        self.__colIndex = {}
        for col in self.__cursor.execute("PRAGMA TABLE_INFO(Address)"):
            self.__colIndex[col[1]] = col[0]

    def __GetCoord(self, str):
        return str.replace("POINT(", "").replace(")", "").split()

    def GetByZipcode(self, zipcode):
        self.__cursor.execute('SELECT * FROM address WHERE Zipcode=?', (zipcode,))
        fetched = self.__cursor.fetchall()
        if len(fetched) == 0:
            return None
        data = fetched[0]
        coord = self.__GetCoord(data[self.__colIndex["Coordinate"]])
        return AddressData(
            data[self.__colIndex["Id"]],
            data[self.__colIndex["Code"]], data[self.__colIndex["Zipcode"]],
            coord[0], coord[1],
            data[self.__colIndex["Prefecture"]], data[self.__colIndex["Gun"]], data[self.__colIndex["City"]], data[self.__colIndex["Ku"]], data[self.__colIndex["Other"]],
            data[self.__colIndex["PrefectureKana"]], data[self.__colIndex["GunKana"]], data[self.__colIndex["CityKana"]], data[self.__colIndex["KuKana"]], data[self.__colIndex["OtherKana"]])

    def GetByAddress(self, pref, city, ku, other):
        if len(pref) <= 2:
            if len(other) <= 0:
                self.__cursor.execute('SELECT * FROM address WHERE City=? AND Ku=?', (city, ku))
            else:
                self.__cursor.execute('SELECT * FROM address WHERE City=? AND Ku=? AND ? LIKE Other || "%"', (city, ku, other))
        else:
            if len(other) <= 0:
                self.__cursor.execute('SELECT * FROM address WHERE Prefecture=? AND City=? AND Ku=?', (pref, city, ku))
            else:
                self.__cursor.execute('SELECT * FROM address WHERE Prefecture=? AND City=? AND Ku=? AND ? LIKE Other || "%"', (pref, city, ku, other))

        fetched = self.__cursor.fetchall()
        if len(fetched) == 0:
            return None

        data = fetched[0]
        coord = self.__GetCoord(data[self.__colIndex["Coordinate"]])
        return AddressData(
            data[self.__colIndex["Id"]],
            data[self.__colIndex["Code"]], data[self.__colIndex["Zipcode"]],
            coord[0], coord[1],
            data[self.__colIndex["Prefecture"]], data[self.__colIndex["Gun"]], data[self.__colIndex["City"]], data[self.__colIndex["Ku"]], data[self.__colIndex["Other"]],
            data[self.__colIndex["PrefectureKana"]], data[self.__colIndex["GunKana"]], data[self.__colIndex["CityKana"]], data[self.__colIndex["KuKana"]], data[self.__colIndex["OtherKana"]])
