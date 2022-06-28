import time
import vol

def out(speech,gender,rate):
    print("")
    if(gender==1):
        print("Saira: ",end="")
    elif(gender==0):
        print("David: ",end="")
    else:
        pass
    print("%s"%speech)
    print("")
    import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', rate)
    engine.setProperty('voice', voices[gender].id)
    engine.say(" %s " % speech)
    engine.runAndWait()

#just for printing but not speaking admin8882757385
def outp(speech,gender,rate):
    import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', rate)
    engine.setProperty('voice', voices[gender].id)
    engine.say(" %s " % speech)
    engine.runAndWait()
    

#def cmd():
    #listening = True
    #while listening == True:
        #j = voice()
        #codevreaker.jk(j)

def prior(say,gender,rate):
    vol.v("all apps", 0.2)
    out("%s" % say,gender,rate)
    vol.v("all apps", 1.0)




