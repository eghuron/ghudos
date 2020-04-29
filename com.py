import os
import platform
from datetime import datetime
from time import sleep

from colorama import Fore

path = varLimp = varRmDir = varDel = ''


def name():  # Nome do sistema para nao ficar criando varias vezes
    print(Fore.RED + 'G', end='')
    print(Fore.YELLOW + 'H', end='')
    print(Fore.GREEN + 'U', end='')
    print(Fore.WHITE + '-', end='')
    print(Fore.CYAN + 'D', end='')
    print(Fore.BLUE + 'O', end='')
    print(Fore.MAGENTA + 'S' + Fore.RESET, end='')


def logo():  # Função só para conseguir deixar o logo bonitinho KKK nem precisava disso
    print('Inciando o ', end='')
    name()
    print('...')


def find_sys():
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


# FUNÇÕES DO SISTEMA #

def ajuda():  # Chama a função ajuda
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


def ver():  # Chama a função ver
    name()
    print(' - Versão 1.0.1')


def horas():  # Chama a função horas/data
    agora = datetime.now()
    print(f'{agora.hour}:{agora.minute}:{agora.second} {agora.day}/{agora.month}/{agora.year}')


def limpar():  # Chama a função de limpar a tela e mostra o logo
    os.system(varLimp)
    name()
    print('')


def listar():  # Chama a funcao de listar o diretorio atual
    global path
    dirlist = os.listdir('./' + path)

    nome_arquivo = []  # Lista com os nomes dos arquivos
    tam_arquivo = []  # Lista com os tamanho dos arquivos
    tipo_arquivo = []  # Lista com os tipos dos arquivos

    for i in dirlist:
        nome_arquivo.append(os.path.basename(path + i))  # Adiciona os nomes em uma lista
    for i in dirlist:
        tam_arquivo.append(os.path.getsize(path + i))  # Adiciona o tamanho dos arquivos em uma lista
    for i in range(0, len(nome_arquivo)):  # Adiciona o tipo dos arquivos em uma lista
        sep_arquivo = nome_arquivo[i].split('.')  # Lista com o o arquivo e a extenção separadas
        ext = sep_arquivo[-1]  # A extensão é o ultimo elento
        tipo_arquivo.append(ext)

    print(f'{"  NOME":<24} {"TAMANHO":<16} {"TIPO"}')
    for c in range(0, len(nome_arquivo)):
        if tipo_arquivo[c] == nome_arquivo[c]:
            tipo_arquivo[c] = 'DIR'
        # O tamanho dos arquivos eh salvo em bytes por isso eu multiplico por 1/1024
        print(f'  {nome_arquivo[c]:<22} {tam_arquivo[c] * (1 / 1024):.3f}{"kB":<12} {tipo_arquivo[c]}')
    print(f'\n  {"":>24}Total {sum(tam_arquivo) * (1 / 1024):.3f}kB')

    # liberar memoria do sistema
    nome_arquivo.clear()
    tam_arquivo.clear()
    tipo_arquivo.clear()


def ir(comando):  # Chama a função de ir ate um diretorio
    global path

    dirlist = os.listdir("./" + path)
    nome_arquivo = []  # Lista com os nomes dos arquivos

    string_path = [comando[3:len(comando) + 1]]
    for i in dirlist:
        nome_arquivo.append(os.path.basename(i))  # Adiciona os nomes em uma lista

    if string_path[0] in nome_arquivo:  # Verifica se o sub-diretório que o usuário digitou está no diretório atual
        path = path + string_path[0] + "/"  # Aletra o path do sistema
        os.system('cd ' + path)
        nome_arquivo.clear()  # Liberar memoria
    elif string_path[0] == '..':  # Função de voltar
        if path != '':  # Verifica se o usuário não está no diretório raiz
            os.system('cd ..')
            tam_string = path.split('/')  # Cria um lista com o todos os caminhos separados por /
            path = path[:-(len(tam_string[-2]) + 1)]  # O novo path é ele menos(-) o diretório que o usuário estava
        else:
            print('Fim do diretório raiz')
    else:
        print('O sistema não achou esse diretório')


def crdir(comando):  # Chama a função de criar sub-diretórios em um diretório
    global path

    new_path = path.replace('/', '\\')
    dir_list = os.listdir('./' + path)
    nome_arquivo = []  # Lista com os nomes dos arquivos no diretorio
    nomes_pr = ['com.py', 'main.py']

    string_dir = [comando[6:len(comando) + 1].replace('/', '\\')]
    for i in dir_list:
        nome_arquivo.append(os.path.basename(i))  # Adiciona os nomes em uma lista

    if string_dir[0] not in nomes_pr:
        if string_dir[0] in nome_arquivo:  # Verifica se o sub-diretorio que o usuario escreveu ja existia
            print(f'O diretório {string_dir[0]} já existe, não foi possível cria-lo.')
        elif string_dir[0] == '..':  # Verifica se o nome da pasta é '..' para que não tenha conflito com o comando IR
            print('Esse nome é invalido.')
        else:
            os.system('mkdir ' + new_path + string_dir[0])
            print(f'A pasta {string_dir[0]} foi criada!')
    else:
        print('Não é permitido criar pastas com esse nome.')


def delete(comando):  # Chama a função de deletar algum arquivo ou diretório
    global path

    newpath = path.replace('/', '\\')
    dirlist = os.listdir('./' + path)
    nome_arquivo = []
    tipo_arquivo = []
    nomes_pr = ['com.py', 'main.py']  # Lista com os nomes proibidos de serem deletados
    string_del = [comando[8:len(comando) + 1].replace('/', '\\')]

    for i in dirlist:
        nome_arquivo.append(os.path.basename(i))
    for i in range(0, len(nome_arquivo)):  # Adiciona o tipo dos arquivos em uma lista
        sep_arquivo = nome_arquivo[i].split('.')  # Lista com o o arquivo e a extenção separadas
        ext = sep_arquivo[-1]  # A extensão é o ultimo elento
        tipo_arquivo.append(ext)

    if string_del[0] in nomes_pr and path == '':  # Impede que o usuário tente deletar os arquivos do 'sistema'
        print('Está tentando me deletar!')
    else:

        if string_del[0] in nome_arquivo:  # Verifica se ja existe o arquivo no diretório atual
            i = nome_arquivo.index(string_del[0])
            # Verifica o tipo do arquivo, se é um diretório ou um arquivo qualquer.
            if tipo_arquivo[i] == nome_arquivo[i]:
                os.system(varRmDir + newpath + string_del[0])
                print(f'O diretório {string_del[0]} foi deletado!')
            else:
                os.system(varDel + newpath + string_del[0])
                print(f'O arquivo {string_del[0]} foi deletado!')
        else:
            print('Não foi possível deletar o arquivo.')


def sair():
    print('ByeBye <3')
    sleep(1)
