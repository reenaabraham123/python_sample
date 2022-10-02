import pyttsx3
n = int(input("Enter a number"))
txt = ""
for i in range(1,11):
    mul = i*n;
    txt+= str(i) + "*" + str(n) + "=" + str(mul) +"\n"
engine = pyttsx3.init()
engine.say(txt)
engine.runAndWait()