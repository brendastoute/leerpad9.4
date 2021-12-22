import json
data = {"path": ""}

# game info:
def load_game():
    with open("save.json", "r") as file:
            save_data = json.load(file)
            file.close()
            return save_data

def save_game(save_data):
    with open("save.json", "w") as file:
        json.dump(save_data, file)



#game itself:

def gamestart():
    pathdecide = input("there is a forest on your left and a water cave behind you wich way do you go?\n[l]eft,[b]ehind\n")
    if pathdecide == "l" or pathdecide =="left":
        data["path"] = "forest"
        save_game(data)
        print("you decide the forest")
        
        forest()
    elif pathdecide =="b" or pathdecide =="behind":
        data["path"] = "behind"
        save_game(data)
        print("you decided behind you")
        cave()

# forest path

def forest():
    spiderattack = input("SPIDERS ARE CRAWLING TO YOU WHAT IS YOUR ACTION\n[f]ight,[r]un\n")
    if spiderattack == "fight" or spiderattack =="f":
        data["path"] = "fight"
        save_game(data)

    if spiderattack =="run" or spiderattack =="r":
        data["path"] = "run"
        save_game(data)
        print ("you decide to run away from the spiders but you trip the spiders catch up and you die")
       



def fight():
    print("you turn around to fight the nasty beasts")
    attack = input("what kind of aproach will you do?\n[f]ist or[k]ick\n")
    if attack == "f" or attack == "fist":
        print("YOU GRAB THE ONE OF THE SPIDERS LEGS RIP IT OUT AND SMACK THE OTHER SPIDERS WITH IT")
        data["path"] = "fist"
        save_game(data)
        fist()

    elif attack == "k" or attack == "kick":
        print("""you tried to kick the spider but it bites into you and you dont feel so well the spiders back off
        after a little bit you fall on the ground and slowely lose consciousness 
        
        you died""")
        data["path"] = "kick"
        save_game(data)


def fist():
    print("you proudly put your foot on one of the spiders as you celibrate your victory you hear a strange noice")
    investigate= input("do you investigate?\n[y]es,[n]o\n")
    if investigate == "yes" or investigate =="y":
        data["path"] == "investigate"
        save_game(data)
        print("decide to investigate the noice and get SLASHED from the dark and die ...... you died")

    elif investigate == "no" or investigate == "n":
        data["path"] = "noinvest"
        save_game(data)
        print("you decide not to investigate and move on .... to be continued")



def cave():
    noise= input("""you decide to dive down in the cave behind you
    you can hear some noises in the cave do you go towards it?\n[y]es, [n]o\n""")
    if noise == "yes" or noise == "y":
        data["path"] = "yesnoise"
        print("you decide to go look and out of the dark A SHARK ATTACKS YOU..... you died")
        save_game(data)
    elif noise == "no" or noise == "n":
        print ("you decide not to check it out and keep swimming")
        data["path"] = "nonoise"
        save_game(data)
        nocheck()

def nocheck():
    print ("while swimming you see a hatch but it has a number code with a piece of text next to it")
    test = ""
    try:
        test = int(input("the text says WHAT IS THE square root OF 49\n"))
    except : 
        print("why you writing letters try again")
        nocheck()

    if test == 7: 
        print ("YOU DID IT YOU, you opened the hatch and live another day... to be continued")
        data["path"] = "win"
        save_game(data)

    elif test < 7 :
        print ("close but not good enough.. you ran out of breath")
        data["path"] = "death"
        save_game(data)

    elif test > 7 :
        print ("close but not good enough.. you ran out of breath")
        data["path"] = "death"
        save_game(data)
    



# the start

def check():
    #checks were you are and reacts to that
    print("you decided to continue")
    #forest
    if savedata["path"] == "forest":
        forest()
    elif savedata["path"] == "fight":
        fight()
    elif savedata["path"] == "run":
        print ("i am sorry but you died")
        startgame()
    elif savedata["path"] == "fist":
        fist()
    elif savedata["path"] == "kick":
        print("i am sorry but you died")
        startgame()
    elif savedata["path"] == "investigate":
        print("i am sorry but you died")
        startgame()
    elif savedata["path"] == "noinvest":
        print("you already beat the game .. GOOD JOB, you can only try again and choise a diffrent path")
        startgame()
    #cave
    elif savedata["path"] =="behind":
        cave()
    elif savedata["path"] =="yesnoise":
        print ("i am sorry but you died")
        startgame()
    elif savedata["path"] == "nonoise":
        nocheck()
    elif savedata["path"] == "win":
        print("you won remember you didnt drown you can try again tho")
        startgame()
    elif savedata["path"] == "death":
        print("i am sorry but you died")
        startgame()

def startgame(): 
    global start,savedata
    start = input("would you like to start were you left off?\n[1]yes,[2]no?\n")



    if start =="1" or start == "yes":
        savedata = load_game()
        check()
        


    elif start =="2" or start == "no":
        gamestart()
        


startgame()
    