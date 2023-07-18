import json
import time
import main
import sys
communityList = []
accountsList = []




#Bloco de funções de manipulação da comunidade
def newCommunity(Cname, Cdescription):
    global communityList
    Cmember = []
    newCommunity = {'name': Cname, 'description': Cdescription, 'member': Cmember}
    communityList.append(newCommunity)

def followCommunity(index, username):
    global communityList
    newMember = {'username': username}
    communityList[index]['member'].append(newMember)




#Bloco de funções de manipulação da conta
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




#Bloco de funções de manipulação txt
def saveChangesAccount():
    with open("Conta.txt", "w") as file:
        for a in accountsList:
            file.write("%s %s %s %s\n" % (a['login'], a['password'], a['name'], a['email']))
            numFollowers = len(a['follower'])
            file.write("%i\n" % numFollowers)
            for b in a['follower']:
                file.write(b['name'])
                file.write("\n")

def saveChangesCommunity():
    with open("Comunidade.txt", "w") as file:
        for a in communityList:
            file.write("%s\n%s\n" % (a['name'], a['description']))
            numFollowers = len(a['member'])
            file.write("%i\n" % numFollowers)
            for b in a['member']:
                file.write(b['username'])
                file.write("\n")

with open("Conta.txt", "r") as file:
    index = 0
    for user in file:
        u = user.split()
        login = u[0]
        password = u[1]
        name = u[2]
        email = u[3]
        newAccount(login, password, name, email)

        next_line = next(file)
        num_followers = int(next_line.strip())

        for follower in range(num_followers):
            next_line = next(file)
            account = next_line.strip()
            followAccount(index, account)
        index += 1 

with open("Comunidade.txt", "r") as file:
    index = 0
    while True:
        name = file.readline().strip()
        description = file.readline().strip()
        
        if not name or not description:
            break
        
        newCommunity(name, description)

        num_members = int(file.readline().strip())

        for member in range(num_members):
            member_account = file.readline().strip()
            followCommunity(index, member_account)
        index += 1

            


#Função de operações
def operations():
    while True:
        print()
        print()
        print('Pressione A para criar uma conta')
        print('Pressione B para excluir uma conta')
        print('Pressione C para seguir uma conta')
        print('Pressione D para deixar de seguir uma conta')
        print('Pressione E para mostrar todas as contas')
        print('Pressione F para mostrar os seguidores de uma conta')
        print('Pressione G para editar uma conta')
        print('Pressione Q para retornar ao menu')
        print('Pressione X para fechar o programa')
        print()

        action = input('Oque você quer fazer? ')
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
                    accountsList.remove(a)
                    removed_accounts.append(a['name'])
                    print('Conta excluída com sucesso!')
            if removed_accounts:
                for a in accountsList:
                    followers = a['follower']
                    a['follower'] = [follower for follower in followers if follower['name'] not in removed_accounts]
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
            name = input('Insira a conta que deseja exibir membros: ')
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
                                print('Esse login ja está em uso, tente novamente')
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
                                print('Esse username ja está em uso, tente novamente')
                                break
                        else:
                            editAccount(accountNumber, 'name', new_name)
                            print('Username alterado com sucesso!')
                    elif field_choice == 4:
                        new_email = input('Digite o novo email: ')
                        for c in accountsList:
                            if c['email'] == new_email:
                                print('Esse email ja está em uso, tente novamente')
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
            time.sleep(0.5)
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
