import main
import json
import time
import sys
communityList = []
accountsList = []




# Bloco de funções de manipulação da comunidade
def newCommunity(Cname, Cdescription):
    global communityList
    Cmember = []
    newCommunity = {'name': Cname, 'description': Cdescription, 'member': Cmember}
    communityList.append(newCommunity)

def followCommunity(index, username):
    global communityList
    newMember = {'username': username}
    communityList[index]['member'].append(newMember)




# Bloco de funções de manipulação da conta
def newAccount(aLogin, aPassword, aName, aEmail):
    global accountsList
    aFollower = []
    newAccountDict = {'login': aLogin, 'password': aPassword, 'name': aName, 'email': aEmail, 'follower': aFollower}
    accountsList.append(newAccountDict)

def followAccount(index, name):
    global accountsList
    newMember = {'name': name}
    accountsList[index]['follower'].append(newMember)

def editAccount(accountNumber, field, newValue):
    global accountsList
    accountsList[accountNumber][field] = newValue

def deleteAccount(accountNumber):
    global accountsList
    account_name = accountsList[accountNumber]['name']
    del accountsList[accountNumber]
    for community in communityList:
        community['member'] = [member for member in community['member'] if member['username'] != account_name]

def show(accountNumber):
    global accountsList
    print('Account', accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print('       Login:', thisAccountDict['login'])
    print('       Password:', thisAccountDict['password'])
    print('       Name:', thisAccountDict['name'])
    print('       Email:', thisAccountDict['email'])
    print('       Followers:', len(thisAccountDict['follower']))
    print()

def showFollower(index1, index2):
    global accountsList
    members = accountsList[index1]['follower']
    print('       Follower','(',index2,')',':', members[index2]['name'])

def removeAccountFromFollowers(username):
    global accountsList
    for account in accountsList:
        account['follower'] = [follower for follower in account['follower'] if follower['name'] != username]

def removeAccountFromCommunities(username):
    global communityList
    for community in communityList:
        community['member'] = [member for member in community['member'] if member['username'] != username]

def updateUsernameInFollowers(oldUsername, newUsername):
    global accountsList
    for account in accountsList:
        for follower in account['follower']:
            if follower['name'] == oldUsername:
                follower['name'] = newUsername

def updateUsernameInMembers(oldUsername, newUsername):
    global communityList
    for community in communityList:
        for member in community['member']:
            if member['username'] == oldUsername:
                member['username'] = newUsername




# Bloco de funções de manipulação txt
def saveChangesAccount():
    with open("Conta.json", "w") as file:
        json.dump(accountsList, file, indent=2)

def loadAccountsFromJSON():
    global accountsList
    try:
        with open("Conta.json", "r") as file:
            accountsList = json.load(file)
    except FileNotFoundError:
        accountsList = []
    except json.JSONDecodeError:
        accountsList = []

def saveChangesCommunity():
    with open("Comunidade.json", "w") as file:
        json.dump(communityList, file, indent=2)

def loadCommunitiesFromJSON():
    global communityList
    try:
        with open("Comunidade.json", "r") as file:
            communityList = json.load(file)
    except FileNotFoundError:
        communityList = []
    except json.JSONDecodeError:
        communityList = []




# Função de operações
def operations():
    while True:
        loadAccountsFromJSON()
        loadCommunitiesFromJSON()
        print()
        print()
        print('Pressione A para criar uma conta')
        print('Pressione B para excluir uma conta')
        print('Pressione C para seguir uma conta')
        print('Pressione D para deixar de seguir uma conta')
        print('Pressione E para mostrar todas as contas')
        print('Pressione F para mostrar os seguidores de uma conta')
        print('Pressione G para editar uma conta')
        print('Pressione Q para voltar ao menu')
        print('Pressione X para fechar o programa')
        print()

        action = input('O que você quer fazer? ')
        action = action.lower()
        action = action[0]
        print()


        if action == 'a':
            time.sleep(0.5)
            print('Nova conta:')
            userLogin = input('Qual seu login? ')
            for a in accountsList:
                if a['login'] == userLogin:
                    print('Esse login já está em uso, tente novamente')
                    break
            else:
                userPassword = input('Qual sua senha? ')
                userName = input('Qual seu username? ')
                for b in accountsList:
                    if b['name'] == userName:
                        print('Esse username já está em uso, tente novamente')
                        break
                else:
                    userEmail = input('Qual seu email? ')
                    for c in accountsList:
                        if c['email'] == userEmail:
                            print('Esse email já está em uso, tente novamente')
                            break
                    else:
                        newAccount(userLogin, userPassword, userName, userEmail)
                        print('Conta criada com sucesso!')


        elif action == 'b':
            time.sleep(0.5)
            print('Exclusão de conta:')
            provLogin = input('Qual seu login? ')
            provPassword = input('Qual sua senha? ')
            removed_accounts = []
            for a in accountsList:
                if a['login'] == provLogin and a['password'] == provPassword:
                    removed_accounts.append(a['name'])
                    accountsList.remove(a)
                    removeAccountFromFollowers(a['name'])
                    removeAccountFromCommunities(a['name'])
                    print('Conta excluída com sucesso!')
                    break
            else:
                print('Credenciais inválidas. Não foi possível excluir a conta.')


        elif action == 'c':
            time.sleep(0.5)
            print('Seguir conta:')
            provName = input('Insira o username da conta que deseja seguir: ')
            index = 0
            account_found = False
            for a in accountsList:
                if a['name'] == provName:
                    provLogin = input('Insira seu Login: ')
                    provPass = input('Insira sua Senha: ')
                    for b in accountsList:
                        if b['login'] == provLogin and b['password'] == provPass:
                            follower_names = [follower['name'] for follower in a['follower']]
                            if b['name'] in follower_names:
                                print('Você já está seguindo essa conta.')
                            else:
                                a['follower'].append({'name': b['name']})
                                print('Seguido com sucesso!')
                            account_found = True
                            break
                    else:
                        print('Credenciais inválidas, tente novamente')
                    break
                index += 1
            if not account_found:
                print('O username inserido é inválido, tente novamente')


        elif action == 'd':
            time.sleep(0.5)
            print('Deixar de seguir uma conta:')
            provName = input('Insira o username da conta que deseja deixar de seguir: ')
            index = 0
            account_found = False

            for a in accountsList:
                if a['name'] == provName:
                    provLogin = input('Insira seu Login: ')
                    provPass = input('Insira sua Senha: ')
                    for b in accountsList:
                        if b['login'] == provLogin and b['password'] == provPass:
                            follower_names = [follower['name'] for follower in a['follower']]
                            if b['name'] not in follower_names:
                                print('Você não está seguindo essa conta.')
                            else:
                                a['follower'] = [follower for follower in a['follower'] if follower['name'] != b['name']]
                                print('Deixou de seguir com sucesso!')
                            account_found = True
                            break
                    else:
                        print('Credenciais inválidas, tente novamente')
                    break
                index += 1
            if not account_found:
                print('O username inserido é inválido, tente novamente')


        elif action == 'e':
            time.sleep(0.5)
            print('Lista de Contas:')
            nAccounts = len(accountsList)
            for accountNumber in range(nAccounts):
                show(accountNumber)


        elif action == 'f':
            time.sleep(0.5)
            print('Mostrar seguidores:')
            name = input('Insira a conta que deseja exibir seguidores: ')
            index = 0
            print()
            print('Account Name: ', name)
            for a in accountsList:
                if a['name'] == name:
                    numfollowers = len(a['follower'])
                    for b in range(0, numfollowers):
                        showFollower(index, b)
                    break 
                index+=1


        elif action == 'g':
            time.sleep(0.5)
            print('Edição de conta:')
            provLogin = input('Qual seu login? ')
            userPassword = input('Qual sua senha? ')
            nAccounts = len(accountsList)
            for accountNumber in range(nAccounts):
                if accountsList[accountNumber]['login'] == provLogin and accountsList[accountNumber]['password'] == userPassword:
                    print('Escolha o campo que deseja editar:')
                    print('1. Login')
                    print('2. Senha')
                    print('3. Username')
                    print('4. Email')
                    field_choice = int(input('Opção: '))
                    if field_choice == 1:
                        new_login = input('Digite o novo login: ')
                        for a in accountsList:
                            if a['login'] == new_login:
                                print('Esse login já está em uso, tente novamente')
                                break
                        else:
                            editAccount(accountNumber, 'login', new_login)
                            print('Login alterado com sucesso!')
                    elif field_choice == 2:
                        new_password = input('Digite a nova senha: ')
                        editAccount(accountNumber, 'password', new_password)
                        print('Senha alterada com sucesso!')
                    elif field_choice == 3:
                        new_name = input('Digite o novo username: ')
                        for b in accountsList:
                            if b['name'] == new_name:
                                print('Esse username já está em uso, tente novamente')
                                break
                        else:
                            old_username = accountsList[accountNumber]['name']
                            editAccount(accountNumber, 'name', new_name)
                            updateUsernameInFollowers(old_username, new_name)
                            updateUsernameInMembers(old_username, new_name)
                            print('Username alterado com sucesso!')
                    elif field_choice == 4:
                        new_email = input('Digite o novo email: ')
                        for c in accountsList:
                            if c['email'] == new_email:
                                print('Esse email já está em uso, tente novamente')
                                break
                        else:
                            editAccount(accountNumber, 'email', new_email)
                            print('Email alterado com sucesso!')
                    else:
                        print('Opção inválida.')
                    break
            else:
                print('Credenciais inválidas. Não foi possível editar a conta.')


        elif action == 'q':
            main.menu()


        elif action == 'x':
            print('Programa fechado!')
            time.sleep(0.5)
            sys.exit()


        time.sleep(0.5)
        saveChangesAccount()
        saveChangesCommunity()

print('Done')


if __name__ == '__main__':
    operations()
