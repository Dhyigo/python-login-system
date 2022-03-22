from time import sleep

lista_nome = []
lista_senha = []
lugar = 0

opcao = str(input('[ 1 ]. CRIAR CONTA.\n'
                  '[ 2 ]. ENTRAR\n'
                  '[ 3 ]. SAIR\n'
                  'DIGITAR OPÇÃO: '
                  )).strip()

while True:

    ### criar usuário

    if opcao == '1':
        novo_nome = str(input('\nCRIAR USUÁRIO: ')).strip()
        nova_senha = str(input('CRIAR SENHA: ')).strip()
        if novo_nome not in lista_nome:

            lista_nome.append(novo_nome)
            lista_senha.append(nova_senha)
            print('SALVANDO INFORMAÇÕES', end='')
            sleep(0.5)
            print('.', end='')
            sleep(0.5)
            print('.', end='')
            sleep(0.5)
            print('.')

            opcao = str(input('\n[ 1 ]. CRIAR CONTA.\n'
                              '[ 2 ]. ENTRAR\n'
                              '[ 3 ]. SAIR\n'
                              'DIGITAR OPÇÃO: '
                              )).strip()

        else:
            print('\n\033[33mUSUÁRIO JÁ EXISTE!\033[m')


    ### login
    elif opcao == '2':

        login_nome = str(input('\nUSUÁRIO: ')).strip()

        if login_nome in lista_nome:

            login_senha = str(input('SENHA: ')).strip()

            for i in lista_nome:

                if login_nome in lista_nome[lugar]:
                    break

                lugar += 1

            if login_nome in lista_nome[lugar] and login_senha in lista_senha[lugar]:
                print('\n\033[32mLOGIN EFETUADO COM SUCESSO!\033[m\nSEJA BEM VINDO {}\n'
                      .format(login_nome.capitalize()))
                break
            else:
                print('\n\033[31mSENHA INVÁLIDA!!\nTENTE NOVAMENTE.\033[m\n')
        else:
            opcao = str(input('\n\033[31mUSUÁRIO NÃO EXISTE\nTENTE CRIAR UMA CONTA.\033[m\n \n'
                              '[ 1 ]. CRIAR CONTA.\n'
                              '[ 2 ]. ENTRAR\n'
                              '[ 3 ]. SAIR\n'
                              'DIGITAR OPÇÃO: '
                              )).strip()
    ### sair
    elif opcao == '3':
        break

    else:
        print('\033[33mOPÇÃO INVALIDA!!\033[m')
        opcao = str(input('\nTENTE UMA DAS OPCÕES ABAIXO.\n'
                          '[ 1 ]. CRIAR CONTA.\n'
                          '[ 2 ]. ENTRAR\n'
                          '[ 3 ]. SAIR\n'
                          'DIGITAR OPÇÃO: '
                          )).strip()
