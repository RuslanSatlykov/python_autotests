import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5b8bff00c6ba9a9715c0e0d3ad789f02'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 33745

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

#def test_part_of_response():
    #response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    #assert response_get.json()["data"][0]["name"] == 'Кринжикc'


#@pytest.mark.parametrize('key, value', [('name', 'Кринжикc'), ('trainer_id', TRAINER_ID), ('id', '321691' )])
#def test_parametrize(key, value):
    #response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})   
    #assert response_parametrize.json()["data"][0][key] == str(value)


def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers/33745', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["trainer_name"] == 'Кринжик'


    #'{"id":"33745","trainer_name":"Кринжик","level":"5","pokemons":["258517","279058","258241","321772","274808","262197","279057","258575","261999","258612","310063","259528","258625","258600","321769","258622","275791","279083","279112","279087","283493","290096","290685","310061","321690","321687","321761","310062","321737","321691","321678","321756","323355","262204","261995","262202","258222","258627","258630","258465","258623","258798","258817","258171","258475","258460","259741","274807"],"pokemons_alive":["321769","290096","290685","321761","323355"],"pokemons_in_pokeballs":[{"id":"321769","name":"Фроу2","stage":"1","photo_id":43,"attack":2,"trainer_id":"33745","status":1,"in_pokeball":1}],"get_history_battle":"0","is_premium":false,"premium_duration":0,"avatar_id":2,"city":"Уфа"}'