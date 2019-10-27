#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.parse
import os
from locationapiusecase import LocationApiUseCase
from dblocation.address.addressfetchsqlite import AddressFetchSqlite

addressFetch = AddressFetchSqlite(os.path.dirname(os.path.abspath(__file__)) + "/Address")
usecase = LocationApiUseCase(addressFetch)


params = urllib.parse.parse_qs(urllib.parse.unquote(os.environ.get('QUERY_STRING')))
zipcode = params['zipcode'][0] if ('zipcode' in params) else ''
address = params['address'][0] if ('address' in params) else ''

result = usecase.Get(zipcode, address)

print('Content-Type: application/json; charset=utf-8\n\n')
print(result)
