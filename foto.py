import facebook
import json
import filtro_das_chaves
from pathlib import Path
from funcoes import exibirPublicacao


if __name__ == '__main__':
        
    numero_da_loja = input('Digite o Numero da loja: ')  
    post_selecionado = input('Digita o dia + img + .png: ')
    arquivo_select = f'{numero_da_loja}.json' 

    LOCAL = Path().absolute()
    TOKENS_ARQUIVO = LOCAL / 'tokens_lojas.json'
    POSTAGEM_LOJA = LOCAL / 'postagens' / arquivo_select

    try:
        with open(TOKENS_ARQUIVO, 'r', encoding='utf8') as arquivo:
            tokens = json.load(arquivo)
            
        with open(POSTAGEM_LOJA, 'r', encoding='utf8') as arquivo:
            posts = json.load(arquivo)
        
    except FileNotFoundError: 
        print('Tokens não encontrados')   
    
    pag = facebook.GraphAPI(tokens.get(numero_da_loja))
    # exibirPublicacao(pag, posts.get(post_selecionado))
    print(pag.get_object(id=posts.get(post_selecionado)))
    


    
