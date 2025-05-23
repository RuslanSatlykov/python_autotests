import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5b8bff00c6ba9a9715c0e0d3ad789f02'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN} 

body_registration = {"trainer_token": TOKEN, "email": "Satlykov555@yandex.ru", "password": "Satcutcut123"}

body_confirmation = {"trainer_token": TOKEN}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''
'''response_confirmation = requests.post(url = f'{URL}/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

#body_create = {"name": "Scandic", "photo_id": 36}
#response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
#print(response_create.text)
#message = response_create.json()['message']
#print(message)

#body_rename = {"pokemon_id": "323355", "name": "Scandic2", "photo_id": 37}
#response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
#print(response_rename.text)
#message = response_rename.json()['message']
#print(message)

#body_add_pokeball = {"pokemon_id": "321769"}
#response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
#print(response_add_pokeball)
#message = response_add_pokeball.json()['message']
#print(message)
