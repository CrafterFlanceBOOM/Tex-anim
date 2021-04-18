import time,os, keyboard

from os.path import expanduser


framedist = 3 #x Seconds, not x milliseconds
version = "1.0 prototype"
name = "texanim"
frames=[]

savedata = [frames,framedist]
def frame(action):
    print(action)
    time.sleep(framedist)
    os.system("cls")
def createframe(action):
    frames.append(action)

print("WELCOME TO Texanim ANIMATON", version)
print("PRESS A TO START ANIMATIN'             ")
print("\n\n\n\n\n Hatcap St.")
keyboard.wait("a")
os.system("cls")
while True:
    f = input("Frame Dist (seconds):")
    os.system("cls")
    try:
        framedist = int(f)
        
    except:
        print("Unvaild Int")
        
    else:
        break

while True:

    print("ANIMATION EDITOR FD:",framedist)
    print("Type in: command playanimation to play your animation or command savedata for exporting your savedata (BETA)")
    f = input("")
    if f == "command playanimation":
        
        for i in frames:
            frame(i)
    if f == "command savedata":
        name = input("Name For savedata (warning if you type a name of another project, it will overwrite):")
        
        home = expanduser("~")
        user_dir = os.path.join(home, name+".texanimfile")
        f = open(user_dir, "w")
        f.write(str(savedata))
        f.close()

    try:
        frames.remove("command playanimation") 
        frames.remove("command savedata")         
    except ValueError:
        al=2
    createframe(f)

        