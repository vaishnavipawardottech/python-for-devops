import requests
import pprint

# print(dir(requests))

# 4 GET, PUT, UPDATE, DELETE (HTTP methods)
# 200 status code - ok
url = "https://dummy-json.mock.beeceptor.com/todos"
response = requests.get(url=url)
pprint.pprint(response.json())

# to iterate a list
for item in data:

    # to iterate a Dictionary
    for key, value in item.items():
        print(value)