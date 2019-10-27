
class AddressData:
    def __init__(self, id, code, zipcode, longitude, latitude, prefecture, gun, city, ku, other, prefectureKana, gunKana, cityKana, kuKana, otherKana):
        self.Id = id
        self.Code = code
        self.Zipcode = zipcode
        self.Longitude = longitude
        self.Latitude = latitude
        self.Prefecture = prefecture
        self.Gun = gun
        self.City = city
        self.Ku = ku
        self.Other = other
        self.PrefectureKana = prefectureKana
        self.GunKana = gunKana
        self.CityKana = cityKana
        self.KuKana = kuKana
        self.OtherKana = otherKana

    def __str__(self):
        return "(" + \
            str(self.Id) + "," + self.Code + "," + self.Zipcode + ",(" + str(self.Latitude) + " " + str(self.Longitude) + ")," + \
            self.Prefecture + "," + self.Gun + "," + self.City + "," + self.Ku + "," + self.Other + ")"
