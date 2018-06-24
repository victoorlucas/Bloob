# -*- coding: utf-8 -*-   #Para evitar erros com acentuação no python
import socket #Biblioteca para conexao por sockets
import thread #Biblioteca para o uso de threads e assim processamento paralelo
import os     #Biblioteca que permitem que você interferencia com o SO subjacente em que o Python está sendo executado para o uso de funções corelacionadas ao SO
import serial #Biblioteca para conexao serial com o arduino 

HOST = ''                     #Campo de IP do servidor, como o codigo se refere ao proprio servidor, logo esta vazio
PORTA = 7000                  #Porta destinada para a comunicação
PORTA_SERIAL = '/dev/ttyUSB0' #porta serial para a comunicação com o arduino
BAUD_RATE = 9600              #Taxa de Baud para estabelecimento da comunicação serial com o arduino
 
conSerial = serial.Serial(PORTA_SERIAL, BAUD_RATE) #Estabelecimento da comunicacao com o arduino via serial
os.system("clear")            #limpeza de tela
 
def conecta(conexao, cliente):              #trecho operacional do sistema onde o servidor fará a interconeção do cliente com o arduino
 
    print("IP conectado | Porta",   cliente) # exibicao do Ip do cliente e a porta de comunicacao
 
    while True: 
        dados = conexao.recv(1024)          #recepcao dos dados enviados pelo cliente, no caso a opcao no qual deseja monitorar determinado parametro
        if not dados: break   
        print ("Cliente para Arduino: ", dados)
        conSerial.write(dados)              #Envio dos dados fornecidos pelo cliente para o arduino
        leitura = conSerial.readline()      #Recebimento da respectivas leituras dos sensores
        print ("Arduino para Cliente: ",leitura)
        conexao.send(leitura)               #Envio da leitura dos sensores do arduino para o cliente
    
 
    print ('Cliente encerrou conexao', cliente)
    print ("Terminando...")
    conSerial.close() #fim da conexao serial com o arduino
    conexao.close()   #Fim da conexao tcp com o cliente
    thread.exit()     #Fim da Thread
    SystemExit
 
tcpSOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criação do socket
conexaoORIGEM = (HOST, PORTA)
tcpSOCKET.bind(conexaoORIGEM) #Estabelecimento da alocacao de uma porta com um IP, o dito Bind
tcpSOCKET.listen(1)           #Servidor se mantem em estado de espera ate a solicitacao de conexao por parte do cliente

print ("|====================================================|")
print ("|                   Servidor online                  |")
print ("|====================================================|")

while True:
 
    conexao, cliente = tcpSOCKET.accept()
    thread.start_new_thread(conecta, tuple([conexao, cliente]))
 
tcpSOCKET.close()