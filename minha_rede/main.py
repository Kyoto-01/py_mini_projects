from pprint import pprint
from re import compile


def validarIP(ip):
    ip_regex = compile('^((?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?\\.){3}(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?))$')
    return ip_regex.match(ip)


def cadastrarDispositivo():
    csv_disp = open('dispositivos.csv', 'a')

    hostname = input('Hostname: ')
    ip = input('IP: ')
    so = input('Sistema Operacional: ')
    descricao = input('Descrição: ')

    if (((ip not in listarDispositivos()) and validarIP(ip))
            and (hostname.replace(' ', '') + so.replace(' ', '') + descricao.replace(' ', '')).isalnum()):
        csv_disp.write(f'{hostname},{ip},{so},{descricao}\n')
    else:
        print('\nERRO -> Certifique-se de que:\n\t- O IP ainda não foi registrado.'
              '\n\t- O IP está escrito no formato: [0-255].[0-255].[0-255].[0-255]'
              '\n\t- As informações de hostname, sistema operacional e descrição não contém caracteres especiais'
              '(com exceção do espaço).')

    csv_disp.close()


def listarDispositivos():
    csv_disp = open('dispositivos.csv', 'r')
    dict_disp = {}

    for disp in csv_disp.read().splitlines():
        infos = disp.split(',')
        dict_disp[infos[1]] = {
            'hostname': infos[0],
            'so': infos[2],
            'descricao': infos[3]
        }

    csv_disp.close()
    return dict_disp


def procurarDispositivo():
    dispositivos = listarDispositivos()
    ip = input('IP do dispositivo: ')
    print()
    if ip in dispositivos:
        return dispositivos[ip]
    else:
        return 'Dispositivo não encontrado'


opcao = '0'
while opcao != '4':
    print(f'\n{" MINHA REDE ":=^100}\n')
    print('O que deseja fazer?')
    print('*\tCadastrar novo dispositivo [ Digite 1 ]',
          '*\tListar dispositivos cadastrados [ Digite 2 ]',
          '*\tProcurar um dispositivo [ Digite 3 ]',
          '*\tSair [ Digite 4 ]', sep='\n')

    opcao = input('\nSua opção: ')
    print()

    if opcao == '1':
        cadastrarDispositivo()
    elif opcao == '2':
        pprint(listarDispositivos())
    elif opcao == '3':
        pprint(procurarDispositivo())
    elif opcao != '4':
        print('Ops! Opção inválida!')
