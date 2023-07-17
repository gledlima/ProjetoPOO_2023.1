communtyList = []

def newCommunit(Cname, Cdescrition):
    global communtyList
    Cmember = []
    newCommunit = {'name': Cname, 'descrition': Cdescrition, 'member': Cmember}
    communtyList.append(newCommunit)

def followCommunit(index, username, email):
    global communtyList
    nemMember = {'username': username, 'email' : email}
    communtyList[index]['member'].append(nemMember)

def show(communtyNumber):
    global communtyList
    print('Account', communtyNumber)
    thisAcommuntylist = communtyList[communtyNumber]
    print('       name:', thisAcommuntylist['name'])
    print('       decription:', thisAcommuntylist['descrition'])
    print('       members:', len(thisAcommuntylist['member']))
    print()

def showMember(index1, index2):
    global communtyList
    members = communtyList[index1]['member']
    print('       community name: ', communtyList[index1]['name'])
    print('       member: ', members[index2]['username'])
    print('       email: ', members[index2]['email'])
    print()

while True:
    print()
    print('Pressione a para criar uma comunidade')
    print('Pressione b para mostrar todas as comunidades')
    print('Pressione c para seguir uma comunidade')
    print('Pressione d para mostrar seguidores de uma comunidade')
    print('Pressione x para sair')
    print()

    action = input('Oque você quer fazer? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'a':
        print('Criação de comunidade:')
        cname = input('Insira o nome da comunidade: ')
        cdescrition = input('insira a descricao da comunidade: ')
        cmember = []
        newCommunit(cname, cdescrition)

    elif action == 'b':
        print('Lista de Contas:')
        ncommunit = len(communtyList)
        for acomunitNumber in range(0, ncommunit):
            show(acomunitNumber)

    elif action == 'c':
        print('Seguir comunidade:')
        name = input('Insira o nome da comunidade que deseja seguir: ')
        index = 0
        for a in communtyList:
            if a['name'] == name:
                name = input('Insira seu nome: ')
                email = input('Insira seu email ')
                followCommunit(index, name, email)
                break
            index+=1

    elif action == 'd':
        print('Mostrar membros:')
        name = input('Insira o nome da comunidade que deseja exibir membros: ')
        index = 0
        for a in communtyList:
            if a['name'] == name:
                members = len(a['member'])
                for b in range(0, members):
                    showMember(index, b)
                break 
            index+=1
                

    elif action == 'x':
        break    

print('Done')
