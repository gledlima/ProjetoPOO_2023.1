import json
accountsList = []

def saveChanges():
    with open('Conta.txt', 'w') as file:
        for a in accountsList:
            file.write("%s %s %s %s\n" % (a['login'], a['password'], a['name'], a['email']))

def newAccount(aLogin, aPassword, aName, aEmail):
    global accountsList
    newAccountDict = {'login': aLogin, 'password': aPassword, 'name': aName, 'email': aEmail}
    accountsList.append(newAccountDict)

def editAccount(accountNumber, field, newValue):
    global accountsList
    accountsList[accountNumber][field] = newValue

def show(accountNumber):
    global accountsList
    print('Account', accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print('       Login:', thisAccountDict['login'])
    print('       Password:', thisAccountDict['password'])
    print('       Name:', thisAccountDict['name'])
    print('       Email:', thisAccountDict['email'])
    print()

with open("Conta.txt", "r") as file:
    for user in file:
        u = user.split()
        login = u[0]
        password = u[1]
        name = u[2]
        email = u[3]
        newAccount(login, password, name, email)
    file.close()

while True:               
    print()
    print('Pressione a para criar uma conta')
    print('Pressione b para excluir uma conta')
    print('Pressione c para mostrar todas as contas')
    print('Pressione d para editar uma conta')
    print('Pressione x para sair')
    print()

    action = input('Oque você quer fazer? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'a':
        print('Nova conta:')
        userLogin = input('Qual seu login? ')
        userPassword = input('Qual sua senha? ')
        userName = input('Qual seu username? ')
        userEmail = input('Qual seu email? ')

        userAccountNumber = len(accountsList)
        newAccount(userLogin, userPassword, userName, userEmail)
        saveChanges()
        print('Conta criada com sucesso!')

    elif action == 'b':
        print('Exclusão de conta:')
        provLogin = input('Qual seu login? ')
        userPassword = input('Qual sua senha? ')
        nAccounts = len(accountsList)
        for a in accountsList:
            if a['login'] == provLogin and a['password'] == userPassword:
                accountsList.remove(a)
                break
                saveChanges()
            else:
                print('Credenciais inválidas. Não foi possível excluir a conta.')

    elif action == 'c':
        print('Lista de Contas:')
        nAccounts = len(accountsList)
        for accountNumber in range(nAccounts):
            show(accountNumber)

    elif action == 'd':
        print('Edição de conta:')
        provLogin = input('Qual seu login? ')
        userPassword = input('Qual sua senha? ')
        nAccounts = len(accountsList)
        for accountNumber in range(nAccounts):
            if accountsList[accountNumber]['login'] == provLogin and accountsList[accountNumber]['password'] == userPassword:
                print('Escolha o campo que deseja editar:')
                print('1. Login')
                print('2. Senha')
                print('3. Email')
                field_choice = int(input('Opção: '))
                if field_choice == 1:
                    new_login = input('Digite o novo login: ')
                    editAccount(accountNumber, 'login', new_login)
                    print('Login alterado com sucesso!')
                elif field_choice == 2:
                    new_password = input('Digite a nova senha: ')
                    editAccount(accountNumber, 'password', new_password)
                    print('Senha alterada com sucesso!')
                elif field_choice == 3:
                    new_email = input('Digite o novo email: ')
                    editAccount(accountNumber, 'email', new_email)
                    print('Email alterado com sucesso!')
                else:
                    print('Opção inválida.')
                break
                saveChanges()
            else:
                print('Credenciais inválidas. Não foi possível editar a conta.')
        
    elif action == 'x':
        print('Programa fechado')
        saveChanges()
        break

print('Done')

