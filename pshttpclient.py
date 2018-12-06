import requests


response = requests.get('http://google.com')

print(response.status_code)
print()
print(response.headers)
print()
print(response.content)