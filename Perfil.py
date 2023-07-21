import json
import time
import main
import sys
profileList = []
accountsList = []




#Bloco de funções de manipulação do perfil
def newProfile(pName):
    global profileList
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




#Bloco de funções de manipulação txt
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

def saveChangesProfile():
    with open("Perfil.json", "w") as file:
        json.dump(profileList, file, indent=2)

def loadProfilesFromJSON():
    global profileList
    try:
        with open("Perfil.json", "r") as file:
            profileList = json.load(file)
    except FileNotFoundError:
        profileList = []
    except json.JSONDecodeError:
        profileList = []




#Função de operações
def operations():
    while True:
        loadAccountsFromJSON()
        loadProfilesFromJSON()
        print()
        print()
        print('Pressiona A para acessar suas mensagens')
        print('Pressione B para enviar uma mensagem')
        print('Pressione C para acessar seus posts')
        print('Pressione D para fazer um post')
        print('Pressione E para acessar um perfil')
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
            print('Acessar perfil:')


        elif action == 'q':
            main.menu()


        elif action == 'x':
            print('Programa fechado!')
            time.sleep(0.5)
            sys.exit()


        else:
            print('Opção inválida, tente novamente!')

        
        time.sleep(0.5)
        saveChangesAccount()
        saveChangesProfile()


if __name__ == '_main_':
    operations()