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

def show(communityNumber):
    global communityList
    print('Community', communityNumber)
    thisAcommunityList = communityList[communityNumber]
    print('       Name:', thisAcommunityList['name'])
    print('       Decription:', thisAcommunityList['description'])
    print('       Members:', len(thisAcommunityList['member']))
    if len(thisAcommunityList['member']) > 0:
        print('       Admin:', thisAcommunityList['member'][0]['username'])
    else:
        print('       Admin: -NONE-')
    print()

def showMember(index1, index2):
    global communityList
    members = communityList[index1]['member']
    print('       Member','(',index2,')',':', members[index2]['username'])




#Bloco de funções de manipulação de conta
def newAccount(aLogin, aPassword, aName, aEmail):
    global accountsList
    aFollower = []
    newAccountDict = {'login': aLogin, 'password': aPassword, 'name': aName, 'email': aEmail, 'follower': aFollower}
    accountsList.append(newAccountDict)

def followAccount(index, name):
    global accountsList
    newMember = {'name': name}
    accountsList[index]['follower'].append(newMember)




#Bloco de funções de manipulação do txt
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
        print('Pressione A para criar uma comunidade')
        print('Pressione B para excluir uma comunidade')
        print('Pressione C para seguir uma comunidade')
        print('Pressione D para deixar de seguir uma comunidade')
        print('Pressione E para mostrar todas as comunidades')
        print('Pressione F para mostrar seguidores de uma comunidade')
        print('Pressione G para editar uma comunidade')
        print('Pressione Q para retornar ao menu')
        print('Pressione X para retornar ao menu')
        print()

        action = input('Oque você quer fazer? ')
        action = action.lower()
        action = action[0]
        print()


        if action == 'a':
            time.sleep(0.5)
            print('Criação de comunidade:')
            cname = input('Insira o nome da comunidade: ')
            for community in communityList:
                if community['name'] == cname:
                    print('Esse nome de comunidade já está em uso. Por favor, escolha outro nome.')
                    break
            else:
                cdescription = input('Insira a descrição da comunidade: ')
                cmember = []
                newCommunity(cname, cdescription)


        elif action == 'b':
            time.sleep(0.5)
            print('Exclusão de comunidade:')
            communityName = input('Insira o nome da comunidade que deseja excluir: ')
            community_found = False

            for community in communityList:
                if community['name'] == communityName:
                    provLogin = input('Insira o login: ')
                    provPassword = input('Insira a senha: ')
                    for b in accountsList:
                        if b['login'] == provLogin and b['password'] == provPassword:
                            provName = b['name']
                            if len(community['member']) == 0 or provName == community['member'][0]['username']:
                                communityList.remove(community)
                                print('Comunidade excluída com sucesso!')
                                community_found = True
                                break
                            else:
                                print('Você não tem permissão para excluir esta comunidade.')
                    else:
                        print('Credenciais inválidas, tente novamente')
                    break
            else:
                if not community_found:
                    print('A comunidade inserida é inválida ou não existe.')


        elif action == 'c':
            time.sleep(0.5)
            print('Seguir comunidade:')
            name = input('Insira o nome da comunidade que deseja seguir: ')
            index = 0
            for a in communityList:
                if a['name'] == name:
                    provLogin = input('Insira o login: ')
                    provPassword = input('Insira a senha: ')
                    for b in accountsList:
                        if b['login'] == provLogin and b['password'] == provPassword:
                            followCommunity(index, b['name'])
                            print('Comunidade seguida com sucesso!')
                    break
                index+=1
            else:
                print('Nome inválido, tente novamente')


        elif action == 'd':
            time.sleep(0.5)
            print('Deixar de seguir uma comunidade:')
            communityName = input('Insira o nome da comunidade que deseja deixar de seguir: ')
            account_found = False
            community_found = False

            for community in communityList:
                if community['name'] == communityName:
                    community_found = True
                    provLogin = input('Insira o login: ')
                    provPassword = input('Insira a senha: ')
                    for b in accountsList:
                        if b['login'] == provLogin and b['password'] == provPassword:
                            for member in community['member']:
                                if member['username'] == b['name']:
                                    community['member'].remove(member)
                                    print('Deixou de seguir a comunidade com sucesso!')
                                    account_found = True
                                    break

            if not community_found:
                print('O nome da comunidade inserida é inválido, tente novamente')
            elif not account_found:
                print('Você não é um membro desta comunidade ou suas credenciais são inválidas.')

        
        elif action == 'e':
            time.sleep(0.5)
            print('Lista de comunidades:')
            nCommunity = len(communityList)
            for aCommunityNumber in range(0, nCommunity):
                show(aCommunityNumber)


        elif action == 'f':
            time.sleep(0.5)
            print('Mostrar membros:')
            name = input('Insira o nome da comunidade que deseja exibir membros: ')
            index = 0
            print()
            print('Community Name: ', name)
            for a in communityList:
                if a['name'] == name:
                    nummembers = len(a['member'])
                    for b in range(0, nummembers):
                        showMember(index, b)
                    break 
                index+=1

        
        elif action == 'g':
            time.sleep(0.5)
            print('Editar comunidade:')
            communityName = input('Insira o nome da comunidade que deseja editar: ')
            community_found = False

            for community in communityList:
                if community['name'] == communityName:
                    community_found = True
                    provLogin = input('Insira o login: ')
                    provPassword = input('Insira a senha: ')
                    for b in accountsList:
                        if b['login'] == provLogin and b['password'] == provPassword:
                            provName = b['name']
                            if len(community['member']) == 0 or provName == community['member'][0]['username']:
                                newCname = input('Insira o novo nome da comunidade: ')
                                newCdescription = input('Insira a nova descrição da comunidade: ')
                                community['name'] = newCname
                                community['description'] = newCdescription
                                print('Comunidade editada com sucesso!')
                            else:
                                print('Você não tem permissão para editar esta comunidade.')
                            break
                    else:
                        print('Credenciais inválidas, tente novamente')
                    break

            if not community_found:
                print('A comunidade inserida é inválida ou não existe.')


        elif action == 'q':
            main.menu()


        elif action == 'x':
            print('Programa fechado!')
            time.sleep(0.5)
            sys.exit()


        time.sleep(0.5)
        saveChangesCommunity()

print('Done')


if __name__ == '__main__':
    operations()
