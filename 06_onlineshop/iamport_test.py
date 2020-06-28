import requests

url = "https://api.iamport.kr/users/getToken"
imp_key = '6656791780160842'
imp_secret = 'g4dWk9QWNpAxkGg8HqOLgg1nnkdGymoOrBLMKCIy1j5lZmuHMis2ztpWODDm01brCXdnzWVAf1WfnqWa'
headers = {
    'imp_key':imp_key,
    'imp_secret':imp_secret
}
req = requests.post(url, data= headers)
print(req.status_code)
print(req.text)