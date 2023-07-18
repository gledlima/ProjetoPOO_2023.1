import json
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
    print('       Community Name: ', communityList[index1]['name'])
    print('       Member: ', members[index2]['username'])
    print('       Email: ', members[index2]['email'])
    print()




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
def saveChanges():
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
while True:
    print()
    print('Pressione a para criar uma comunidade')
    print('Pressione b para excluir uma comunidade')
    print('Pressione c para mostrar todas as comunidades')
    print('Pressione d para seguir uma comunidade')
    print('Pressione e para deixar de seguir uma comunidade')
    print('Pressione f para mostrar seguidores de uma comunidade')
    print('Pressione x para sair')
    print()

    action = input('Oque você quer fazer? ')
    action = action.lower()
    action = action[0]
    print()


    if action == 'a':
        print('Criação de comunidade:')
        cname = input('Insira o nome da comunidade: ')
        for community in communityList:
            if community['name'] == cname:
                print('Esse nome de comunidade já está em uso. Por favor, escolha outro nome.')
                saveChanges()
                break
        else:
            cdescription = input('Insira a descrição da comunidade: ')
            cmember = []
            newCommunity(cname, cdescription)


    elif action == 'b':
        print('Exclusão de comunidade:')
        communityName = input('Insira o nome da comunidade que deseja excluir: ')
        community_found = False

        for community in communityList:
            if community['name'] == communityName:
                communityList.remove(community)
                print('Comunidade excluída com sucesso!')
                community_found = True
                saveChanges()
                break

        if not community_found:
            print('A comunidade inserida é inválida ou não existe.')


    elif action == 'c':
        print('Lista de comunidades:')
        nCommunity = len(communityList)
        for aCommunityNumber in range(0, nCommunity):
            show(aCommunityNumber)


    elif action == 'd':
        print('Seguir comunidade:')
        name = input('Insira o nome da comunidade que deseja seguir: ')
        index = 0
        for a in communityList:
            if a['name'] == name:
                name = input('Insira seu nome: ')
                followCommunity(index, name)
                saveChanges()
                break
            index+=1
        else:
            print('Nome inválido, tente novamente')


    elif action == 'e':
        print('Deixar de seguir uma comunidade:')
        communityName = input('Insira o nome da comunidade que deseja deixar de seguir: ')
        account_found = False

        for community in communityList:
            if community['name'] == communityName:
                username = input('Insira seu nome: ')
                email = input('Insira seu email: ')
                for member in community['member']:
                    if member['username'] == username and member['email'] == email:
                        community['member'].remove(member)
                        print('Deixou de seguir a comunidade com sucesso!')
                        account_found = True
                        saveChanges()
                        break
                else:
                    print('Não foi possível encontrar suas credenciais de membro na comunidade.')
                break

        if not account_found:
            print('A comunidade inserida é inválida ou você não é um membro dela.')


    elif action == 'f':
        print('Mostrar membros:')
        name = input('Insira o nome da comunidade que deseja exibir membros: ')
        index = 0
        for a in communityList:
            if a['name'] == name:
                nummembers = len(a['member'])
                for b in range(0, nummembers):
                    showMember(index, b)
                break 
            index+=1
                

    elif action == 'x':
        saveChanges()
        break    

print('Done')
