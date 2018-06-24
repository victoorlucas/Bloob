# -*- coding: utf-8 -*-   #Para evitar erros com acentuação no python

#  CONEXÃO COM O SERVER QUE COMUNICA COM ARDUINO   #
import socket #Biblioteca para conexao por sockets
import os     #Biblioteca que permitem que você interferencia com o SO subjacente em que o Python está sendo executado para o uso de funções corelacionadas ao SO
 
HOST = raw_input("Server IP:") #Campo de IP do servidor
PORTA = 7000 #Porta destinada para a comunicação
 
tcpSOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criação do socket
destinoCONEXAO = (HOST, PORTA)
tcpSOCKET.connect(destinoCONEXAO) #Solicitacao de conexao ao servidor


#  API PARA REQUISIÇÕES VINDAS DE FORA  #
from flask import Flask #Biblioteca para uso do HTTP/Criação da API
from flask import jsonify #Biblioteca para enviar responses JSON

app = Flask(__name__) 

@app.route("/temp", methods=['GET']) #Cria uma nova rota para requisições da temperatura
def temp():    
    tcpSOCKET.send(1) #Envia ao servidor a opção 1 para temperatura
    temperatura = tcpSOCKET.recv(1024) #Recebe a temperatura vinda do servidor
    response = jsonify(temperatura=temperatura) #Envia ao cliente um JSON com a temperatura
    response.headers.add('Access-Control-Allow-Origin', '*') #Permite conexões sem credenciais

    return response

@app.route("/agua", methods=['GET']) #Cria uma nova rota para requisições da temperatura
def agua():    
    tcpSOCKET.send(2) #Envia ao servidor a opção 2 para nível de água
    agua = tcpSOCKET.recv(1024) #Recebe a temperatura vinda do servidor
    response = jsonify(agua=agua) #Envia ao cliente um JSON com o nível de água
    response.headers.add('Access-Control-Allow-Origin', '*') #Permite conexões sem credenciais

    return response

if __name__ == "__main__":
    app.run() #Inicia a aplicação