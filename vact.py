import calendar
import datetime
import time as tic
def day(date):
    if("/" in date):
        date=date.replace("/"," ")
    bobeeprn = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[bobeeprn])


def date():
    from datetime import datetime
    now = datetime.now()
    da = ("%s %s %s" % (now.month, now.day, now.year))
    jo = now.month
    ho = now.day
    lo = now.year
    date = '%s %s %s' % (ho, jo, lo)
    return date

def time(mode):
    """ 'all' for hour, minute and second in format hh:mm:ss
        'hour' for only hour 
        'min' for only minute
        'sec' for only sec"""
    if(mode=="all"):
        import time as tic
        from datetime import datetime

        now = datetime.now()
        time=("%s:%s:%s" % (now.hour, now.minute, now.second))
        return time
    elif(mode=="hour"):
        import time as tic
        from datetime import datetime

        now = datetime.now()
        time=("%s" % now.hour)
        time=int(time)
        return time
    elif(mode=="min"):
        import time as tic
        from datetime import datetime

        now = datetime.now()
        time=("%s"%now.minute)
        time=int(time)
        return time
    elif(mode=="sec"):
        import time as tic
        from datetime import datetime

        now = datetime.now()
        time=("%s" %now.second)
        time=int(time)
        return time
    else:
        import time as tic
        from datetime import datetime
        now = datetime.now()
        time=("%s:%s:%s" % (now.hour, now.minute, now.second))
        tic.sleep(1)
        return time

j=date()

def daynow():
    date=j
    bobeeprn = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[bobeeprn])
    
#print(day(time()))




h="""

N.O.T.E: corpentropy is not responsible for what anyone/anything uses this software for. Thankyou for using Entropy! 

0. !close  <appname>                       (will close the app <appname>)
1. !open   <appname>                       (will open the app <appname>) [may not work sometimes]
2. !screenshot                             (screenshot of computer screen will be shown to you)
3. !vl     <appname>                       (will set the volume of app to low)
4. !vm     <appname>                       (will set the volume of app to medium
5. !vf     <appname>                       (will set the volume of app to full)
6. !vr                                     (this command will reset volume of all the apps to normal level)
5. !mute   <appname>                       (will mute the volume of app to low)
6. !unmute <appname>                       (will unmute the volume of app to low)
7. !play                                   (play paused media on the computer)
8. !pause                                  (pause media playing on the computer)
9. !lock                                   (this command will lock the computer, bring it back to windows login screen)
10.!say female <what you want to say>      (a female voice will say <what u want to say)   (ex: !say female hi)
10.!say male <what you want to say>        (a male voice will say <what u want to say)   (ex: !say male hello how are you)
11.!hide                                   (this will hide entropy window on your computer, for more convenience)
12.!s  <what u want to search>             (search anything on google using this command)
13.!write <what u want to type>            (type anything u want using this command)   (ex:!write I can see you) [may not work sometimes]
14.!keylogger <number of minutes>          (this will email you a log of keys typed on the keyboard for the number of minutes you specified)
15.!sleep                                  (this will put your computer to sleep)
16.!restart                                (this will restart your computer)
17.!shutdown                               (this will shutdown your computer)
18.!fix                                    (if your computer has become unresponsive then this will try to fix it)
19.!link   <your_link>                     (this will open the link on your computer)                             
20.!close current                          (this will close the window/app currently being used/opened on your computer)
21.!picture                                (this will take a picture from your computer's webcam)

"""