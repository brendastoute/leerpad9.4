import json, os, yaml

class tools:
    def check_dir():
        try:
            for root, dirs, files in os.walk(".\\"):
                if "ID" not in dirs:
                    os.mkdir(".\\ID\\")
                    return "Created Path: ID" 

                if "key.yml" not in files:
                    with open("key.yml", "w") as file:
                        tools.key({"IDs": []})
                    return "Created File: key.yml"
                    
                else:
                    return "FileCreationError: Path ID or File key.yml could not be created or already exist"
        
        except:
            return "os.walk could not return any"

    def save(save_data):
        with open(f".\\ID\\{save_data['name']}.json", "w") as file:
            json.dump(save_data, file)

    def key(key_data):
        with open("key.yml", "w") as file:
            yaml.dump(key_data, file)
            

for _ in range(2):
    tools.check_dir()


up = 0
down = 0
save_data = {}
key_data = yaml.load(open("key.yml", "r"), Loader=yaml.FullLoader)

name = input("What's your Name?\n")
save_data["name"] = name
key_data["IDs"].append(name)

def plus():
    global up
    up += 1

def minus():
    global down
    down += 1

def start():
    experience = input("""what is your experience?
    [a]1/2 years , [b]3/5 years or [c] 6 or more \n
    """) 
    if experience == "a":
        save_data["exp"] = "1/2 years"
        minus()
        what()
    elif experience == "b":
        save_data["exp"] = "3/5 years"
        plus()
        what()
    elif experience =="c":
        save_data["exp"] = "6 or more years"
        plus()
        what()


def what():
    mchobby = input("""what do you do/what are you?
    [a] builder,
    [b] pvp,
    [c] redstone user,    
    [d] none of the above \n """)
    
    if mchobby == "a":
        save_data["mchobby"] = "builder"
        plus()
        mob()
    elif mchobby == "b":
        save_data["mchobby"] = "pvp"
        plus()
        mob()
    elif mchobby == "c":
        save_data["mchobby"] = "redstone user"
        plus()
        mob()
    elif mchobby == "d":
        save_data["mchobby"] = "None"
        minus()
        mob()


def mob():
    favmob = input("""what is your favorite mob?
    [a] zombie,
    [b] pig,
    [c] enderman,
    [d] creeper \n
    """)
    if favmob == "zombie" or favmob == "a":
        save_data["mob"] = "zombie"
        minus()
        result()
    elif favmob == "pig" or favmob =="b":
        save_data["mob"] = "pig"
        plus()
        result()
    elif favmob == "enderman" or favmob =="c":
        save_data["mob"] = "enderman"
        plus()
        result()
    elif favmob == "creeper" or favmob == "d":
        save_data["mob"] = "creeper"
        minus()
        result()



def result():
    if up > down:
        tools.save(save_data)
        tools.key(key_data)
        print ("you are accepted")
    else:
        print("i am sorry but no")

start()

