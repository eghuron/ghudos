from os import system 
from time import sleep
import com

#Detectar o sistema atual
com.sisFind()
#Perfumaria para iniciar o sistema
system(com.varLimp) #Limpa o terminal do Windows (Lembrar de verificar o sys do usuario)
com.logo() #Imprime a logo do sistema
sleep(1)


while True:
    label = 'G:/' + com.path + '>'  #Label original do sistema
    commando = str(input(label)) #input de comandos do sistema

    #Testando qual comando foi inserido.
    if commando.lower() == 'ajuda':
        com.ajuda()
    elif commando.lower() == 'ver':
        com.ver()
    elif commando.lower() == 'horas' or commando.lower() == 'data':
        com.horas()
    elif commando.lower() == 'limpar':
        com.limpar()
    elif commando.lower() == 'listar':
        com.listar()
    elif commando.lower() == 'ir' or commando.lower() == 'crdir' or commando.lower() == 'deletar':
        print('Nenhum diretório informado')
    elif commando.lower()[0:3] == 'ir ':
        com.ir(commando)
    elif commando.lower() == 'sair':
        com.sair()
        break
    elif commando.lower()[0:6] == 'crdir ':
        com.crdir(commando)
    elif commando.lower()[0:8] == 'deletar ':
        com.delete(commando)
    else:
        print(f'"{commando}" não é um comando interno do sistema') #mensagem de erro quando o usuario tenta usar um comando invalido
