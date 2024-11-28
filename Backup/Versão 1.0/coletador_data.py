import facebook
import json

token = ''
with open('token.txt', 'r') as arquivo:
        token = arquivo.read()

graph = facebook.GraphAPI(access_token = token)

all_pages = {}
paginas = graph.get_connections('me','accounts')

all_pages = paginas.get('data')

with open('data.json', 'w', encoding='utf8') as arquivo:
        json.dump(paginas, arquivo, indent=2, ensure_ascii=False)