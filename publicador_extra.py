from package.funcoes_jb import publicar_extra, get_tokens
from package.imagens import img_extra
from time import sleep

lojas = get_tokens()
img = img_extra()

for loja in lojas.keys():
    try:
        token = lojas.get(loja)
        publicar_extra(loja,img,token[0])
    except KeyError:
        print(f'Página {loja} {token[1]} atualizou o token.')
        sleep(60)
        lojas = get_tokens()
        token = lojas.get(loja)
        print('Novos Tokens foram carregados com sucesso.')
        try: publicar_extra(loja,img,token[0])
        except: continue
    except FileNotFoundError:
        print('Imagem ou Mensagem não encontrada, consulte o Log de Erros.')
        break
    


