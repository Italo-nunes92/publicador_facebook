from pathlib import Path
from datetime import datetime

LOCAL_RAIZ = Path('\\\\192.42.103.17\\propaganda\\publicador_facebook')
MENSAGENS = LOCAL_RAIZ / 'msg'
IMAGENS = LOCAL_RAIZ / 'img'
ERROS = LOCAL_RAIZ / 'erros'
JSON = LOCAL_RAIZ / 'json'

hr = datetime.today()
data_hora = format(hr, '%d/%m/%Y %H:%M:%S')
dia_mes_ano = format(hr, '%d/%m/%Y')
hora_atual = hr.hour

