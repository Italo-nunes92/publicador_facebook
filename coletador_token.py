import facebook
import json

token = ''

LOCAL_RAIZ = '\\\\192.42.103.17\\propaganda\\publicador_facebook\\'

with open(f'{LOCAL_RAIZ}token.txt', 'r') as arquivo:
        token = arquivo.read()

graph = facebook.GraphAPI(access_token = token)

all_pages = {}
paginas = graph.get_connections('me','accounts?limit=50')

for p in paginas.get('data'):
        all_pages.update({p['name']:p['access_token']})

with open(f'{LOCAL_RAIZ}novos_tokens.json', 'w', encoding='utf8') as arquivo:
        json.dump(all_pages, arquivo, indent=2, ensure_ascii=False)
