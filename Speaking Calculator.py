import pyttsx3 


engine=pyttsx3.init("sapi5")
voice=engine.getProperty("voices")
engine.setProperty("voices",voice[0])

def say(audio):
    engine.say(audio)
    engine.runAndWait()

say("HAI , It Is A Speaking Calculator.")

print(" ")
say("Enter The First Number")
v=int(input("Enter The First Number  : "))
say(v)

say("Enter The Second Number")
p=int(input("Enter The Second Number : "))
say(p)

print(" ")

print("The Operators = +    -   /   *   %   // \n")
say("Choose The Operator")
vp=str(input("Enetr Your Operator : "))
say(vp)

print(" ")



if(vp=="+"):
    print("The Answer Is : ",v+p,"\n")
    a=v+p
    say(a)
    
elif(vp=="-"):
    print("The Answer Is : ",v-p,"\n")
    a=v-p
    say(a)
elif(vp=="*"):
    print("The Answer Is : ",v*p,"\n")
    a=v*p
    say(a)
elif(vp=="/"):
    print("The Answer Is : ",v/p,"\n")
    a=v/p
    say(a)
elif(vp=="//"):
    print("The Answer Is : ",v//p,"\n")
    a=v//p
    say(a)
elif(vp=="%"):
    print("The Answer Is : ",v%p,"\n")
    a=v%p
    say(a)
else:
    print("You Entered Invalued Operators . Please Try Again")
    say("You Entered Invalued Operators . Please Try Again")
