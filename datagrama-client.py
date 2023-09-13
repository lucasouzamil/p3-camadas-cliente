#####################################################
# Camada Física da Computação
#Carareto
#11/08/2022
#Aplicação
####################################################


#esta é a camada superior, de aplicação do seu software de comunicação serial UART.
#para acompanhar a execução e identificar erros, construa prints ao longo do código! 

from funcao import cria_pacotes
from enlace import *
import time
import numpy as np
import random
import time

# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#use uma das 3 opcoes para atribuir à variável a porta usada
#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
serialName = "COM3"                   # Windows(variacao de)


def main():
    try:
        print('')
        print("Iniciou o main")
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        com1 = enlace(serialName)
    
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        com1.enable()
        #Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        print("Abriu a comunicação")
        print('')

        #Endereco da imagem a ser transmitida
        imageR = open("img/helloworld.jpg",'rb').read()
        #print(imageR)
        # Carrega imagem
        print("Carregando imagem para transmissão:")
        print(f" - {imageR}")
        print("-"*35)
        #txBuffer = imagem em bytes!
        pacotes = cria_pacotes(b'\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef')
        
        print('Enviando byte de sacrificio')
        com1.sendData(np.asarray(b'x00'))    #enviar byte de lixo
        time.sleep(.05)
        com1.rx.clearBuffer()

        print('Esperando byte de sacrificio')
        rxBuffer, nRx = com1.getData(1)
        time.sleep(.05)
        com1.rx.clearBuffer()

        print('Iniciando transmissão de pacotes')
        i = 0
        while i < len(pacotes['bytearray']):
            txBuffer = pacotes['bytearray'][i]
            print(f'Enviou --->  {txBuffer}')
            com1.sendData(np.asarray(txBuffer)) 
            time.sleep(.05)

            rxBuffer, nRx = com1.getData(15)
            time.sleep(.05)
            print(rxBuffer)
            int_list = [int(byte) for byte in rxBuffer]
            if (int_list[0] == i) and int_list[-3:]==[255,255,255]:
                i+=1
            com1.rx.clearBuffer()
            
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
