# -*- coding: utf-8 -*-
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'income':2, 'age':9, 'loan':6, 'LTI':7})

print(r.json())