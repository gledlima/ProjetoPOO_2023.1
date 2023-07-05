communtyList = []

def newCommunit(Cname, Cdescrition, Cmember):
    global communtyList
    newCommunit = {'name': Cname, 'descrition': Cdescrition, 'member': Cmember}
    communtyList.append(newCommunit)
   
def show(communtyNumber):
    global communtyList
    print('Account', communtyNumber)
    thisAcommuntylist = communtyList[communtyNumber]
    print('       name', thisAcommuntylist['name'])
    print('       decrition:', thisAcommuntylist['descrition'])
    print('       member:', thisAcommuntylist['member'])
    print()



while True:
    print()
    print('Pressione g para criar uma comunidade')
    print('Pressione d para mostrar todas as comunidades')
    print('Pressione x para sair')
    print()

    action = input('Oque você quer fazer? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'g':
        print('Criação de comunidade:')
        cname = input('insira o nome da comunidade ')
        cdescrition = input('insira a descricao da comunidade ')
        cmember = input('membros ')
        newCommunit(cname, cdescrition, cmember)

    elif action == 'd':
        print('Lista de Contas:')
        ncommunit = len(communtyList)
        for acomunitNumber in range(0, ncommunit):
            show(acomunitNumber)

    elif action == 'x':
        break    

print('Done')