communityList = []

def newCommunity(Cname, Cdescription):
    global communityList
    Cmember = []
    newCommunity = {'name': Cname, 'description': Cdescription, 'member': Cmember}
    communityList.append(newCommunity)

def followCommunity(index, username, email):
    global communityList
    nemMember = {'username': username, 'email' : email}
    communityList[index]['member'].append(nemMember)

def show(communityNumber):
    global communityList
    print('Community', communityNumber)
    thisAcommunityList = communityList[communityNumber]
    print('       Name:', thisAcommunityList['name'])
    print('       Decription:', thisAcommunityList['description'])
    print('       Members:', len(thisAcommunityList['member']))
    print()

def showMember(index1, index2):
    global communityList
    members = communityList[index1]['member']
    print('       Community Name: ', communityList[index1]['name'])
    print('       Member: ', members[index2]['username'])
    print('       Email: ', members[index2]['email'])
    print()

while True:
    print()
    print('Pressione a para criar uma comunidade')
    print('Pressione b para excluir uma comunidade')
    print('Pressione c para mostrar todas as comunidades')
    print('Pressione d para seguir uma comunidade')
    print('Pressione e para mostrar seguidores de uma comunidade')
    print('Pressione x para sair')
    print()

    action = input('Oque você quer fazer? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'a':
        print('Criação de comunidade:')
        cname = input('Insira o nome da comunidade: ')
        cdescription = input('insira a descricao da comunidade: ')
        cmember = []
        newCommunity(cname, cdescription)

    elif action == 'c':
        print('Lista de Contas:')
        ncommunit = len(communityList)
        for acomunitNumber in range(0, ncommunit):
            show(acomunitNumber)

    elif action == 'd':
        print('Seguir comunidade:')
        name = input('Insira o nome da comunidade que deseja seguir: ')
        index = 0
        for a in communityList:
            if a['name'] == name:
                name = input('Insira seu nome: ')
                email = input('Insira seu email ')
                followCommunity(index, name, email)
                break
            index+=1

    elif action == 'e':
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
        break    

print('Done')
