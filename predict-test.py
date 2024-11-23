#!/usr/bin/env python
# coding: utf-8

import requests

url = 'http://localhost:9696/predict'
customer_id = 'xyz-123'

customer = {
 'country': 'germany',
 'gender': 'male',
 'credit_score': 655,
 'age': 52,
 'tenure': 9,
 'balance': 144696.75,
 'products_number': 1,
 'credit_card': 1,
 'active_member': 1,
 'estimated_salary': 49025.79
 }

response = requests.post(url, json=customer).json()
print(response)

if response['churn'] == True:
    print('sending promo email to %s' % customer_id)
else:
    print('not sending promo email to %s' % customer_id)
