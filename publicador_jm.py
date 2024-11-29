from package.funcoes_jb import publicar_post, get_tokens,excluir_publicacao
from package.imagens import selecionar_imagem
from time import sleep

lojas = get_tokens()
img = selecionar_imagem()

for loja in lojas.keys():
    try:
        token = lojas.get(loja)
        publicar_post(loja,img,token[0])
    except KeyError:
        print(f'Página {loja} {token[1]} atualizou o token.')
        sleep(10)
        lojas = get_tokens()
        token = lojas.get(loja)
        print('Novos Tokens foram carregados com sucesso.')
        publicar_post(loja,img,token[0])
    except FileNotFoundError:
        print('Imagem ou Mensagem não encontrada, consulte o Log de Erros.')
        break
    

# for loja in lojas.keys():
#     token = lojas.get(loja)
#     excluir_publicacao(loja,token[0],'28/11/2024-12')
