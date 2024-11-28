import json
import coletador_token


arquivos_bruto = {}
filtro = {}
nova_lista = {}
ordenado = []
lista_ordenada = {}

LOCAL_RAIZ = '\\\\192.42.103.17\\propaganda\\publicador_facebook\\Backup\\Versão 1.0\\'

with open(f'{LOCAL_RAIZ}novos_tokens.json', 'r') as arquivo:
        arquivos_bruto = json.load(arquivo)

with open(f'{LOCAL_RAIZ}lojas_numeros.json', 'r') as arquivo:
        filtro = json.load(arquivo)


for i in filtro:
        filtragem = {filtro.get(i): arquivos_bruto.get(i)}
        
        nova_lista.update(filtragem)
        
ordenado = sorted(nova_lista.items())

for i in range(len(ordenado)):
    lista_ordenada[ordenado[i][0]] = ordenado[i][1]


LOCAL_RAIZ = '\\\\192.42.103.17\\propaganda\\publicador_facebook\\Backup\\Versão 1.0\\'
with open(f'{LOCAL_RAIZ}tokens_lojas.json', 'w', encoding='utf8') as arquivo:
                json.dump(lista_ordenada, arquivo, indent=2, ensure_ascii=False)

