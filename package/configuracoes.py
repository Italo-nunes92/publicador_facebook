from pathlib import Path
from datetime import datetime

LOCAL_RAIZ = Path('\\\\192.42.103.17\\propaganda\\publicador_facebook')
MENSAGENS = LOCAL_RAIZ / 'msg'
IMAGENS = LOCAL_RAIZ / 'img'
ERROS = LOCAL_RAIZ / 'erros'
JSON = LOCAL_RAIZ / 'json'

hr = datetime.today()

def getDataHora():
    hr = datetime.today()
    data_hora = format(hr, '%d/%m/%Y %H:%M:%S')
    return data_hora

def getDiaMesAno():
    hr = datetime.today()
    dia_mes_ano = format(hr, '%d/%m/%Y')
    return dia_mes_ano

def getHoraAtual():
    hr = datetime.today()
    hora_atual = hr.hour
    return hora_atual