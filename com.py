import os, sys, platform
from colorama import Fore
from datetime import datetime, timezone
from time import sleep

path = varLimp = varRmDir = varDel = ''

def name(): #Nome do sistema para nao ficar criando varias vezes
    print(Fore.RED +'G', end ='')
    print(Fore.YELLOW +'H', end ='')
    print(Fore.GREEN +'U', end ='')
    print(Fore.WHITE +'-', end ='')
    print(Fore.CYAN +'D', end ='')
    print(Fore.BLUE +'O', end ='')
    print(Fore.MAGENTA +'S' + Fore.RESET, end ='')

def logo(): #Função só para conseguir deixar o logo bonitinho KKK nem precisava disso
    print('Inciando o ', end = '')
    name()
    print('...')

def sisFind():
    global varLimp, varDel, varRmDir
    sis = platform.system()

    if sis.lower() == 'windows':
        varLimp = 'cls'
        varDel = 'del '
        varRmDir = 'rd /s /q '
    else:
        varLimp = 'clear'
        varDel = 'rm '
        varRmDir = 'rm - r '
        
##FUNÇÕES DO SISTEMA##

def ajuda(): #Chama a função ajuda
    print('''
    Seja bem-vindo a tela de ajuda do GHU-DOS
    Temos uma gama infinita de comandos, aqui vão alguns deles!
    CRDIR   Cria um sub-diretório dentro de um diretório.
    DATA    Exibe a data atual.
    DELETAR Deleta um arquivo ou um sub-diretório de um diretório
    HORAS   Exibe o horário local.
    IR      Comando que permite ir de um diretorio a outro, escrevendo 'ir ..' faz voltar
    LIMPAR  Limpa a tela.
    LISTAR  Exibe uma lista de arquivos e subdiretórios em um diretório.
    VER     Exibe a versão do sistema.
    ''')

def ver(): #Chama a função ver
    name()
    print(' - Versão 1.0')

def horas(): #Chama a função horas/data
    agora = datetime.now()
    print(f'{agora.hour}:{agora.minute}:{agora.second} {agora.day}/{agora.month}/{agora.year}')

def limpar(): #Chama a função de limpar a tela e mostra o logo
    os.system(varLimp)
    name()
    print('')

def listar(): #Chama a funcao de listar o diretorio atual
    global path
    dirlist = os.listdir('./' + path)
    
    nomeArquivo = [] #Lista com os nomes dos arquivos
    tamArquivo = [] #Lista com os tamanho dos arquivos
    tipoArquivo = [] #Lista com os tipos dos arquivos
    
    for i in dirlist:
        nomeArquivo.append(os.path.basename(path+i)) #Adiciona os nomes em uma lista
    for i in dirlist:
        tamArquivo.append(os.path.getsize(path+i)) #Adiciona o tamanho dos arquivos em uma lista
    for i in range(0,len(nomeArquivo)): #Adiciona o tipo dos arquivos em uma lista
        sepArquivo = nomeArquivo[i].split('.') #Lista com o o arquivo e a extenção separadas
        ext = sepArquivo[-1] # A extensão é o ultimo elento
        tipoArquivo.append(ext)
    
    print(f'{"  NOME":<24} {"TAMANHO":<16} {"TIPO"}')
    for c in range(0, len(nomeArquivo)):
        if tipoArquivo[c] == nomeArquivo[c]:
            tipoArquivo[c] = 'DIR'
        print(f'  {nomeArquivo[c]:<22} {tamArquivo[c]*(1/1024):.3f}{"kB":<12} {tipoArquivo[c]}')#O tamanho dos arquivos eh salvo em bytes por isso eu multiplico por 1/1024
    print(f'\n  {"":>24}Total {sum(tamArquivo)*(1/1024):.3f}kB') #O tamanho dos arquivos eh salvo em bytes por isso eu multiplico por 1/1024
    
    #liberar memoria do sistema
    nomeArquivo.clear()
    tamArquivo.clear() 
    tipoArquivo.clear()

def ir(comando): #Chama a função de ir ate um diretorio
    global path
    
    dirlist = os.listdir("./" + path)
    nomeArquivo = [] #Lista com os nomes dos arquivos
   
    stringPath = [comando[3:len(comando) + 1]]
    for i in dirlist:
        nomeArquivo.append(os.path.basename(i)) #Adiciona os nomes em uma lista

    if stringPath[0] in nomeArquivo: #Verifica se o sub-diretório que o usuário digitou está no diretório atual
        path = path + stringPath[0] + "/" #Aletra o path do sistema
        os.system('cd ' + path)
        nomeArquivo.clear() #Liberar memoria
    elif stringPath[0] == '..':  #Função de voltar
        if path != '': #Verifica se o usuário não está no diretório raiz
            os.system('cd ..')
            tamString = path.split('/') #Cria um lista com o todos os caminhos separados por /
            path = path[:-(len(tamString[-2])+1)] #O novo path é ele menos(-) o diretório que o usuário estava
        else:
            print('Fim do diretório raiz')
    else:
        print('O sistema não achou esse diretório')

def crdir(comando): #Chama a função de criar sub-diretórios em um diretório
    global path

    newpath =path.replace('/','\\')
    dirlist = os.listdir('./' + path)
    nomeArquivo = [] #Lista com os nomes dos arquivos no diretorio
    nomesPr = ['com.py', 'main.py']

    stringDir = [comando[6:len(comando) + 1].replace('/','\\')]
    for i in dirlist:
        nomeArquivo.append(os.path.basename(i)) #Adiciona os nomes em uma lista

    if stringDir[0] not in nomesPr:
        if stringDir[0] in nomeArquivo: #Verifica se o sub-diretorio que o usuario escreveu ja existia
            print(f'O diretório {stringDir[0]} já existe, não foi possível cria-lo.')
        elif stringDir[0] == '..': #Verifica se o nome da pasta é '..' para que não tenha conflito com o comando IR
            print('Esse nome é invalido.')
        else:
            os.system('mkdir ' + newpath + stringDir[0])
            print(f'A pasta {stringDir[0]} foi criada!')
    else:
        print('Não é permitido criar pastas com esse nome.')

def delete(comando): #Chama a função de deletar algum arquivo ou diretório
    global path

    newpath =path.replace('/','\\')
    dirlist = os.listdir('./' + path)
    nomeArquivo = []
    tipoArquivo = []
    nomesPr = ['com.py', 'main.py'] #Lista com os nomes proibidos de serem deletados
    stringDel = [comando[8:len(comando) + 1].replace('/','\\')]
   
    for i in dirlist:
        nomeArquivo.append(os.path.basename(i))
    for i in range(0,len(nomeArquivo)): #Adiciona o tipo dos arquivos em uma lista
        sepArquivo = nomeArquivo[i].split('.') #Lista com o o arquivo e a extenção separadas
        ext = sepArquivo[-1] # A extensão é o ultimo elento
        tipoArquivo.append(ext)
    
    if stringDel[0] in nomesPr and path == '': #Impede que o usuário tente deletar os arquivos do 'sistema'
        print('Está tentando me deletar!')
    else: 

        if stringDel[0] in nomeArquivo: #Verifica se ja existe o arquivo no diretório atual
            i = nomeArquivo.index(stringDel[0])
            if tipoArquivo[i] == nomeArquivo[i]: #Verifica o tipo do arquivo, se é um diretório ou um arquivo qualquer.
                os.system(varRmDir + newpath + stringDel[0])
                print(f'O diretório {stringDel[0]} foi deletado!')
            else:
                os.system(varDel + newpath +  stringDel[0])
                print(f'O arquivo {stringDel[0]} foi deletado!')
        else:
            print('Não foi possível deletar o arquivo.')
def sair():
    print('ByeBye <3')
    sleep(1)

