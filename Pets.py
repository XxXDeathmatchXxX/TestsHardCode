import pytest
import requests
import json
from settings import login, url_pets, user_pet, user_pet_new, url_pets_new
from colorama import init, Fore

init(autoreset=True)


# structirize json file
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# 1 Test Get list of pets
def get_status_of_pets():
    print(Fore.CYAN + "get_status_of_pets() is running now")
    r = requests.get(url_pets, auth=login)
    assert r.status_code == 200
    print(Fore.CYAN + "Function get_status_of_pets() ends ")
    return r



r = get_status_of_pets()
print("CurrentCode is", r)
jprint(r.json())



# 2 Create Category
def create_new_pet():
    print(Fore.CYAN + "create_new_pet() is running now")
    r = requests.post(url_pets, auth=login, json=user_pet)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(Fore.CYAN + 'ERROR: %s' % e)

    if(r.status_code == 201):
        assert r.status_code == 201
        print(r.status_code)
        print(Fore.GREEN + "Function create_new_pet succeeded, Pet Created")
    elif(r.status_code != 201):
        print(Fore.BLUE + "Function Create_new_category failed. Current status is: " f'{r.status_code}.', Fore.BLUE+
              "pet already exists, ""enter another type of category")
    print(Fore.CYAN + "Function create_new_pet() ends ")

create_new_pet()



# 3
def get_status_of_pets_by_id():
    print(Fore.CYAN + "get_status_of_pets_by_id() is running now")
    number = input('Enter id number:')
    r = requests.get(url_pets + str(number), auth=login)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(Fore.CYAN + "ERROR this id " f'{number}' " does not exist: %s" % e)
    print(r.json())
    print(Fore.CYAN + "Function get_status_of_pets_by_id() ends")

# get_status_of_pets_by_id()







# 4
def put_pet_by_id():
    print(Fore.CYAN + "put_pet_by_id() is running now")
    r = requests.put(url_pets_new, auth=login, json=user_pet_new)

    try:
      r.raise_for_status()
    except requests.exceptions.HTTPError as e:
     print('ERROR: %s' % e)
     assert r.status_code == 201
    if (r.status_code == 200):
        print("Category Updated")
    else:
        print("Current status is: " f'{r.status_code}.', "Pet already exists, type another type of Pet")
    print(r.json())
    print(Fore.CYAN + "Function put_pet_by_id() ends")


put_pet_by_id()


# 5
def delete_pet_by_id():
    print(Fore.CYAN +"Function delete_pet_by_id() is running now")
    number = input(Fore.GREEN + 'Which id number do you want to delete:')
    r = requests.delete(url_pets + str(number), auth=login)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(Fore.YELLOW + "ERROR this id " f'{number}' " does not exist anymore or it never exist before: %s" % e)
    if(r.status_code == 204):
        print(Fore.GREEN + "You've delete line successfully, status code: "f'{r.status_code}')

    else:
        print(Fore.YELLOW + "Line does not exist, status code:"f'{r.status_code}')

    print(Fore.CYAN + "Function Function delete_pet_by_id() ends")

# delete_pet_by_id()