import json
import time
import main
import sys
profileList = []
accountsList = []
communityList = []




#Bloco de funções de manipulação do perfil
def newProfile(pName, profileList):
    pMessages = []
    pPosts = []
    newProfile = {'name': pName, 'messages': pMessages, 'posts': pPosts}
    profileList.append(newProfile)

def addMessage(index, message):
    global profileList
    newMessage = {'message': message}
    profileList[index]['messages'].append(newMessage)

def addPost(index, post):
    global profileList
    newPost = {'post': post}
    profileList[index]['posts'].append(newPost)

##def acessPerfil()



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

def searchprofile(name, profileList, accountList, communityList):

    for data in profileList:
        if data['name'] == name:
            for data2 in accountList:
                if data2['name'] == name:
                    profileData = {'username' : data2['login'], 'name' : data2['name'], 'email' : data2['email'], 'follower' : data2['follower']}
                    return profileData
            
            for data2 in communityList:
                if data2['name'] == name:
                    profileData = {'name': data2['name'], 'descrition' : data2['description'], 'member' : data2['member'], 'admin' : data2['admin']}
                    return profileData
        
    return 0




#Bloco de funções de manipulação txt
def saveChangesdata(archive, data):
    with open(archive, "w") as file:
        json.dump(data, file, indent=2)

def loadDataFromJSON(archive):
    try:
        with open(archive, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    except json.JSONDecodeError:
        data = []

    return data




#Função de operações
def operations():
    while True:
        accountsList = loadDataFromJSON("Conta.json")
        profileList = loadDataFromJSON("Perfil.json")
        communityList = loadDataFromJSON("Comunidade.json")
        print()
        print()
        print('Pressiona A para acessar suas mensagens')
        print('Pressione B para enviar uma mensagem')
        print('Pressione C para acessar seus posts')
        print('Pressione D para fazer um post')
        print('Pressione E para acessar seu perfil')
        print('Pressione K para buscar e acessar um perfil')
        print('Pressione Q para voltar ao menu')
        print('Pressione X para fechar o programa')
        print()

        action = input('Oque você quer fazer? ')
        action = action.lower()
        action = action[0]
        print()


        if action == 'a':
            print('Caixa de mensagens:')
        

        elif action == 'b':
            print('Enviar mensagem:')


        elif action == 'c':
            print('Mural de posts:')


        elif action == 'd':
            print('Fazer um post:')
        

        elif action == 'e':
            print('Acessar seu perfil:')
            
            
        elif action == 'k':
            print('Buscar e acessar perfil')
            name = input('Insira o nome do perfil a ser buscado: ')
            profileData = searchprofile(name, profileList, accountsList, communityList)
            while profileData == 0 and name != 'x':
                name = input('Perfil não encontrado ou perfil incorreto. Inisira novamente o o nome de perfil ou digite x para retornar: ')
                profileData = searchprofile(name, profileList, accountsList, communityList)

            if name != 'x':
                print(profileData)
            


        elif action == 'q':
            main.menu()


        elif action == 'x':
            print('Programa fechado!')
            time.sleep(0.5)
            sys.exit()


        else:
            print('Opção inválida, tente novamente!')

        
        time.sleep(0.5)
        saveChangesdata('Perfil.json', profileList)
        saveChangesdata('Conta.json', accountsList)
        saveChangesdata('Comunidade.json', communityList)

print('Done')

if __name__ == '__main__':
    operations()
