import requests
from django.conf import settings

def get_token():
    access_data = {
        'imp_key':settings.IAMPORT_KEY,
        'imp_secret':settings.IAMPORT_SECRET
    }
    url = "https://api.iamport.kr/users/getToken"
    req = requests.post(url, data=access_data)
    access_res = req.json()

    if access_res['code'] is 0:
        return access_res['response']['access_token']
    else:
        return None

def payments_prepare(order_id, amount, *args, **kwargs):
    pass

def find_transaction(order_id, *args, **kwargs):
    pass