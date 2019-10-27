#!/usr/bin/env python3
# coding: utf-8

from locationapiusecase import LocationApiUseCase
from dblocation.address.addressfetchsqlite import AddressFetchSqlite
import urllib.parse
import os

addressFetch = AddressFetchSqlite(os.path.dirname(os.path.abspath(__file__)) + "/Address")
usecase = LocationApiUseCase(addressFetch)

print("Content-Type: text/html; charset=UTF-8\n\n")
params = urllib.parse.parse_qs(urllib.parse.unquote(os.environ.get('QUERY_STRING')))
zipcode = params['zipcode'][0] if ('zipcode' in params) else ''
address = params['address'][0] if ('address' in params) else ''
print(usecase.Get(zipcode, address))

