# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 23:20:55 2024

@author: Sam
"""

import requests
print(requests.get('https://iss.moex.com/iss/securities.json?q=Yandex').json())






