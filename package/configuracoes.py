
from datetime import datetime
from pathlib import Path

LOCAL_RAIZ = Path(__file__).absolute().parent.parent
MENSAGENS = LOCAL_RAIZ / 'msg'
IMAGENS = LOCAL_RAIZ / 'img'
EXTRA = LOCAL_RAIZ / 'extra'
ERROS = LOCAL_RAIZ / 'erros'
JSON = LOCAL_RAIZ / 'json'
ENV = LOCAL_RAIZ / 'package' / '.env'

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

