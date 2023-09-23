import requests
from Tests.settings import login, token, url_token
from colorama import Fore





def create_new_token():
    print(Fore.CYAN + "create_new_token() is running now")
    r = requests.post(url_token, auth=login, json=token)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(Fore.CYAN + 'ERROR: %s' % e)

    if(r.status_code == 200):
        assert r.status_code == 200
        print(r.status_code)
        print(Fore.GREEN + "Function create_new_pet succeeded, token Created")
    elif(r.status_code != 200):
        print(Fore.BLUE + "Function create_new_token() failed. Current status is: " f'{r.status_code}.', Fore.BLUE+
              "token already exists, ""enter another token")
    print(Fore.CYAN + "Function create_new_token() ends ")

create_new_token()


if __name__ == "__main__":
    ...



