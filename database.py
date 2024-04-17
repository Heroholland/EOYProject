#Repl.it Database Wrapper
import requests

url = "https://ade66e7d-240d-4753-a3e8-a48b00a9a1ae-00-3a21mbvjcxet7.riker.replit.dev/"

class Database:
    def __init__(self):
        self.headers = {'content-type': 'application/json'}
    def insert(self, key, value):
        json = {"action": "insert", "key": str(key), "value": str(value)}
        response = requests.post(url + "/execute", json=json, data=json, headers=self.headers)
        return response.text
    def replace(self, key, value):
        json = {"action": "insert","key": str(key), "value": str(value)}
        response = requests.post(url + "/execute", json=json, data=json, headers=self.headers)
        return response.text
    def delete(self, key):
        json = {"action": "delete", "key": str(key)}
        response = requests.post(url + "/execute", json=json, data=json, headers=self.headers)
        return response.text
    def read(self, key):
        json = {"key": str(key)}
        response = requests.post(url + "/read", json=json, data=json, headers=self.headers)
        return response.text