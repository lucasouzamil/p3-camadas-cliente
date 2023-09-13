def cria_pacotes(bytearray):


    payloads=[]
    qnt_pacote=len(str(bytearray).lower().split("x"))//50
    for i in list(range(0, qnt_pacote)):
        payloads.append(bytearray[i*50:(i+1)*50])
    payloads.append(bytearray[qnt_pacote*50:])

    qntdpayloads = len(payloads)
    pacotes = {'bytearray':[],'inteiro':[]}
    pacotes['inteiro'].append([[0,qnt_pacote+1,12+3,0,0,0,0,0,0,0,0,0],[],[255,255,255]])
    pacotes['bytearray'].append(bytes([0,qnt_pacote+1,12+3,0,0,0,0,0,0,0,0,0])+bytes([255,255,255]))
    for n in range(0, qntdpayloads):
        head = [0]*12
        head[0]=n+1
        head[1]=qnt_pacote+1
        head[2]=12+3+len(payloads[n])
        eop=[255,255,255]
        payload=payloads[n]
        pacotes['bytearray'].append(bytes(head)+payload+bytes(eop))
        pacotes['inteiro'].append([head,payload,eop])
    for pacote in pacotes['bytearray']:
        print(pacote)
        print('')


""" letra=b'\x05\x055\x00\x00\x00\x00\x00\x00\x00\x00\x00'
qnt_pacote=str(letra).lower().split("x")
print(len(qnt_pacote)) """


cria_pacotes(b'\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef')
#cria_pacotes(lista)

#print('x7fx80x81x82x83x84x85x86x87x88x89x8ax8bx8cx8dx8ex8fx90x91x92x93x94x95x96x97x98x99x9ax9bx9cx9dx9ex9fxa0xa1xa2xa3xa4xa5xa6xa7xa8xa9xaaxabxacxadxaexafxb0'.count('x'))