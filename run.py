import requests
import sys


link = input("Enter an URL WebSite : \n")


f = requests.get(link)
response_time = requests.get(link).elapsed.total_seconds()

print(f.text)
print("Temps de réponse de la page : ", response_time)
