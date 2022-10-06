
import requests

url = "http://localhost:9696/predict"

card = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}
respose = requests.post(url, json=card).json()


print(respose)