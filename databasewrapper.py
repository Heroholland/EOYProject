#Repl.it Database Wrapper for Python
import requests, json

class Database:
    def __init__(self):
        self.headers = {'content-type': 'application/json'}
        self.baseurl = "https://ade66e7d-240d-4753-a3e8-a48b00a9a1ae-00-3a21mbvjcxet7.riker.replit.dev"
    def insert(self, key: str, value) -> str:
        json = {"action": "insert", "key": str(key), "value": str(value)}
        response = requests.post(f"{self.baseurl}/execute", json=json, headers=self.headers)
        return response.text
    def replace(self, key: str, value) -> str:
        json = {"action": "insert","key": str(key), "value": str(value)}
        response = requests.post(f"{self.baseurl}/execute", json=json, headers=self.headers)
        return response.text
    def delete(self, key: str) -> str:
        json = {"action": "delete", "key": str(key)}
        response = requests.post(f"{self.baseurl}/execute", json=json, headers=self.headers)
        return response.text
    def read(self, key: str) -> str:
        json = {"key": str(key)}
        response = requests.post(f"{self.baseurl}/read", json=json, headers=self.headers)
        return response.text
    def readall(self) -> json:
        response = requests.post(f"{self.baseurl}/readall", headers=self.headers)
        return response.json()