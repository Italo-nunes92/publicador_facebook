from package.funcoes_jb import get_tokens, excluir_publicacao, conectar_token_pag, abrir_postagens
from package.imagens import exibirPublicacao
import os

lojas = get_tokens()
primeiraVez = True


while primeiraVez:
    selecao = input('Digite "DD/MM/AAAA-H" da publicacao para exclusão:')
    for loja in lojas.keys():
        token = lojas.get(loja)
        
        
        if primeiraVez == True:
            pag = conectar_token_pag(token[0])
            post = abrir_postagens(loja)
            
            primeiraVez = exibirPublicacao(pag , post.get(selecao))
            if primeiraVez == False: 
                escolha = input('Deseja realmente excluir? [1]SIM ou [2]NÃO: ')
                if escolha == '2' : break
        if primeiraVez is False:        
            excluir_publicacao(loja,token[0],selecao)
    if primeiraVez is True :
        print('Publicação inválida')
        input('...')
        os.system('cls')

