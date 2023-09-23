from requests.auth import HTTPBasicAuth

login = HTTPBasicAuth('admin', 'admin')
user_category = {
        "name": "Cats"
    }

url_category = "http://91.210.171.73:8080/api/category/"
user_id = {
  "name": "back"
}
user_new = {
  "name": "18"
}

url_category_new = "http://91.210.171.73:8080/api/category/233/"
url_pets = "http://91.210.171.73:8080/api/pet/"
url_pets_new = "http://91.210.171.73:8080/api/pet/120/"
user_pet = {
"name": "Doc",
  "photo_url": "string",
  "category": {
    "name": "Cats"
  },
  "status": "available"
}

user_pet_new = {
"name": "RobAgain",
  "photo_url": "string",
  "category": {
    "name": "Cats"
  },
  "status": "available"
}

url_token = "http://91.210.171.73:8080/api/api/token/auth/"
token = {
  "token": "dfdf"
}


if __name__ == "__main__":
    ...
