import pytest
import requests
import json
from settings import login, user,url_category


# structirize json file
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# 1 Test Get list of categories
def get_status_of_categories():
    r = requests.get(url_category, auth=login)
    assert r.status_code == 200
    return r



r = get_status_of_categories()
print("CurrentCode is", r)
jprint(r.json())


# 2 Create Category
def create_new_category():
    r = requests.post(url_category, auth=login, data=user)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r.status_code != 201
    if(r.status_code == 201):
        print("Pet Created")
    else:
        print("Current status is: " f'{r.status_code}.', "Category already exists, type another type of category")


create_new_category()

# Making a get request
response = requests.get('https://api.github.com/')

# print response
print(response)

# print check if an error has occurred
print(response.raise_for_status())




