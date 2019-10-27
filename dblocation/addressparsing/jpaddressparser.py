from .jpaddressparserdata import JpAddressParserData


class JpAddressParser:
    def __init__(self, address):
        ad = JpAddressParserData()
        pos = ad.EatSigns(address, 0)
        self.Pref = ad.GetAddressPref(address, pos)
        pos = ad.EatSigns(address, pos + len(self.Pref))
        self.Gun = ad.GetAddressGun(address, pos)
        pos = ad.EatSigns(address, pos + len(self.Gun))
        self.City = ad.GetAddressCity(address, pos)
        pos = ad.EatSigns(address, pos + len(self.City))

        if ad.IsSeireiCity(self.City) or self.City == "":
            self.Ku = ad.GetAddressKu(address, pos)
            pos = ad.EatSigns(address, pos + len(self.Ku))
        else:
            self.Ku = ""

        self.Other = address[pos:len(address)]

    def __str__(self):
        return self.Pref + "/" + self.Gun + "/" + self.City + "/" + self.Ku + "/" + self.Other
