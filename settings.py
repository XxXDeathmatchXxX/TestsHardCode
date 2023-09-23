from requests.auth import HTTPBasicAuth


login = HTTPBasicAuth('admin', 'admin')
user = {

        "name": "15"
    }

url_category = "http://91.210.171.73:8080/api/category/"
user_id = {

  "name": "back"
}

user_new = {


  "name": "16"
}


url_category_new = "http://91.210.171.73:8080/api/category/230/"

url_pets = "http://91.210.171.73:8080/api/pet/"

user_pet = {
  "name": "22",
  "photo_url": "22",
  "category": {
    "name": "115"
  },
  "status": "22"
}