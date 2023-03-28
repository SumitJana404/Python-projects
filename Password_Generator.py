import string
import random               

def passwordgenerator(passlen):

    #s=string.ascii_letters                    #storing all ascii letters in s
    #print(s)
    s2=string.ascii_uppercase                   #storing all uppercase letters in s2
    #print(s2)
    s3=string.ascii_lowercase                   #storing all lowercase letters in s3
    #print(s3)
    s4=string.digits                            #storing all digits in s4
    #print(s4)
    s5=string.punctuation                       #storing all punctuation in s5
    #print(s5)


    all=[]                 #creating an empty list
    all.extend(list(s2))   #adding s2 in all
    all.extend(list(s3))   #adding s3 in all
    all.extend(list(s4))   #adding s4 in all
    all.extend(list(s5))   #adding s5 in all
    #print(all)

    random.shuffle(all)    #shuffling all elements
    #print("Shuffled: ")
    #print(all)

    #print("Password as List:")
    #print(all[0:passlen])

    print("Your Password is:",end=" ")
    print("".join(all[0:passlen]))

    fp=open("password.txt","a")
    fp.close()


while True:
    passlen=int(input("Enter Password Length : "))
    passwordgenerator(passlen)

    a=input("Do You want to continue (Yes/No) : ")
    if(a.lower()=='no'):
        exit()
        

    

