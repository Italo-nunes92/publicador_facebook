# Publicador Facebook

Esse projeto auxilia na publicação das paginas do facebook, fazendo publicações simultâneas em todas as páginas que você tem administração através de um Token obtido na pagina de Developers do Facebook.
Ao invés de publicar em cada página manualmente, você define um grupo de páginas na aplicação e ela faz a postagem em cada página com uma mensagem e uma imagem pré-definida. 
Por exemplo, no caso ela está configurada para executar em 4 horários no dia durante a semana,  quando a aplicação é executada, ela identifica o horário e o dia para selecionar a imagem que será publicada, depois ela vai em cada página e seleciona a mensagem especifica com um canal de atendimento, como no exemplo, ela vai pegar a mensagem com a WhatsApp de atendimento daquela página e publica. A única manutenção que é preciso fazer é toda semana alimentar com novas imagens.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

Você precisa ter o Python Instalado em sua maquina, Python 3.10 ou superior, uma IDE, preferível VS Code, e algumas bibliotecas listada a baixo:

```
pip install facebook-sdk
pip install python-dotenv
pip install Pillow
pip install requests
```

### 🔧 Instalação

Primeiramente dentro da pasta "package" crie um arquivo ".env" para definir seu token em uma variável de ambiente:
.env:
```
token = "SeuTokenEntreAspas"
```

Depois execute o arquivo "criar_grupo.py" quando executado ele começará a listar as primeiras 50 páginas que seu token tem acesso, você deve indicar para cada página uma numeração de ordem de publicação desejada ou "0" para não incluir a página no grupo de postagem:
```
Digite "0" para remover a página da lista
Pagina 1 = Nº: (DIGITE O NUMERO DA ORDEM)
```
```
Página 1 = Nº: 0 (NÃO SERÁ INCLUIDA NO GRUPO)
Página 2 = Nº: 01 (SERÁ A PRIMEIRA NA ORDEM)
Página 3 = Nº: 02 (SERÁ A SEGUNDA NA ORDEM)
Página 4 = Nº: 05 (SERÁ A TERCEIRA, CASO NÃO TENHA 03 E A 04)
```

Configure as mensagem na pasta "msg".
o arquivo ".txt" deve começar com ("loja + "NUMERO DA ORDEM" + .txt) lembrando que o numero que você indicou na ordem é a referência para buscar o arquivo ".txt":
```
loja01.txt (SERÁ A MENSAGEM DA PAGINA "Página 1" DEFINIDA NA ORDEM)
```
Exemplo da mensagem "loja01.txt":
```
Os melhores produtos para sua casa estão aqui na SUA EMPRESA! 🏡 

Quer saber mais? É só entrar em contato! 🤗 

📲 WhatsApp: https://wa.me/ "NUMERO DA SUA LOJA DA PÁGINA 01"

SLOGAM DA SUA EMPRESA! ❤
```
### ⚙️ Configurando o cronograma e as imagens

Na pasta "package" configure o arquivo "imagens.py" os horários e os nomes das imagens que será publicada nas funções a baixo:

selecionar_imagem():
```
cronogama =[
        ['img01.jpg','img11.jpg','img20.jpg','img02.jpg'],
        ['img12.jpg','img21.jpg','img03.jpg','img13.jpg'],
        ['img22.jpg','img04.jpg','img14.jpg','img23.jpg'],
        ['img05.jpg','img15.jpg','img24.jpg','img06.jpg'],
        ['img16.jpg','img25.jpg','img07.jpg','img17.jpg'],
        ['img26.jpg','img08.jpg','img18.jpg','img27.jpg'],
        ['img09.jpg','img19.jpg','img28.jpg','img10.jpg']
    ]
```
As linhas dessa matriz equivalem aos dias da semana, sendo a linha "0" Segunda-feira, as colunas equivalem a ordem dos horários, sendo 4 colunas para 4 horários ao longo do dia.

Os horários você define na mesma função "selecionar_imagem()" logo a baixo da variável "cronograma"

```
if hora_atual in range(0,11): # ENTRE AS 00:00HS ATÉ 10:59HS
        img = 0
    elif hora_atual in range(11,15): # ENTRE AS 11:00HS ATÉ 14:59HS
        img = 1
    elif hora_atual in range(15,19): # ENTRE AS 15:00HS ATÉ 18:59HS
        img = 2
    else:   # ENTRE AS 19:00HS ATÉ 23:59HS
        img = 3
```
Por padrão, o recomendado pelo Facebook é imagens JPG, com tamanho menor que 1mb, porém caso queira usar PNG, você deve mudar na matriz "cronograma" a extensão dos arquivos para "imgXX.png" e descomentar a linha a baixo:
```
compactar_imagem(img) 
```
Essa função vai reduzir o tamanho da imagem para otimizar a postagem na página, configure da maneira que desejar na função "compactar_imagem()" dentro do arquivo "imanges.py"

compactar_imagem():
```
    imagem = Image.open(img)
    imagem_reduzida = imagem.resize((1000,1000)) # Dimensão da imagem
    imagem_reduzida.save(img,dpi=(72,72)) # Qualidade da imagem
```

Pronto, chegando nesse ponto, você já tem a aplicação configurada para executar o arquivo "publicador_jm.py".

Caso não tenha ainda o token do facebook, [Clique Aqui](https://developers.facebook.com/docs/facebook-login/guides/access-tokens?locale=pt_BR#pagetokens), e leia a documentação do facebook para obter e configurar um token de acesso da aplicação API do Grupo Meta.

## ⚙️ Executando o arquivo "publicador_jm.py"

Você pode configurar uma tarefa no Agendador do seu computador, para executar no horário definido ou utilizar outra maneira para executar.

Caso necessite de empacotar em arquivo ".exe" você deve instalar o Pyinstaller
```
pip install pyinstaller
```
Execute esta linha, já está definida com todos os arquivos necessários.
```
pyinstaller --noconfirm --onefile -c --add-data="package/configuracoes.py:." --add-data="package/funcoes_jb.py:." --add-data="package/imagens.py:." --add-data="package/local.py:." publicador_jm.py
```

### 🔩 Excluindo uma publicação.

Execute o arquivo "deletar_post.py" e digite a data e apenas a hora que foi publicado, a aplicação exibe a imagem da postagem e perguntará se deseja excluir, confirme e a postagem será excluida de todas as páginas.

```
Digite "DD/MM/AAAA-H" da publicacao para exclusão: 01/01/2025-9  # DATA FOI 01/01/2025 E A POSTAGEM FOI REALIZADA AS 9:25HS POREM BASTA INSERIR APENAS A HORA E IGNONAR OS MINUTOS FICA SEGUIDO DE UM TRAÇO "-9"
```
```
Deseja realmente excluir? [1]SIM ou [2]NÃO: # DIGITE "sim" PARA EXCLUIR, OU "não" PARA SAIR
```


## 🎁 Considerações

O projeto tirou um peso de todos os gerentes que trabalham na empresa, disponibilizando tempo para outras atividades, tirando o trabalho de postarem manualmente em suas páginas e centralizando na matriz, assim filtramos falhas de postagem e conseguimos controlar os erros, caso aconteça uma alteração de preço ou outro tipo de ocorrência.

Obrigado pela atenção, e espero que aproveitem para tirar uma boa experiência desse projeto



---
⌨️ com ❤️ por [Italo Nunes](https://github.com/Italo-nunes92) 😊
