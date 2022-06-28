from __future__ import print_function

import os
import subprocess

import speech_recognition as sr
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

import voice


def vp(f,pica):
    output = subprocess.check_output(('TASKLIST', '/FO', 'CSV')).decode()
    pro = []
    y=pro
    output = output.replace('"', '').split('\r\n')
    keys = output[0].split(',')
    proc_list = [i.split(',') for i in output[1:] if i]
    # make dict with proc names as keys and dicts with the extra nfo as values
    proc_dict = dict((i[0], dict(zip(keys[1:], i[1:]))) for i in proc_list)
    for name, values in sorted(proc_dict.items(), key=lambda x: x[0].lower()):
        pro.append(name)
    p = len(pro)
    for i in range(0, p):
        name = pro[i]
        k = name.lower()
        if (f in k):
            print(name)
            he = name.replace(".exe", "")
            print(he, "hhhh")
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:

                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                if session.Process and session.Process.name() == "%s.exe" % he:
                    volume.SetMasterVolume(pica, None)
                    print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
        if("all" in f):
            he = name.replace(".exe", "")
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                if session.Process and session.Process.name() == "%s.exe" % he:
                    volume.SetMasterVolume(pica, None)
                    print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())


def v(f,pica):
    output = subprocess.check_output(('TASKLIST', '/FO', 'CSV')).decode()
    pro = []
    y=pro
    output = output.replace('"', '').split('\r\n')
    keys = output[0].split(',')
    proc_list = [i.split(',') for i in output[1:] if i]
    # make dict with proc names as keys and dicts with the extra nfo as values
    proc_dict = dict((i[0], dict(zip(keys[1:], i[1:]))) for i in proc_list)
    for name, values in sorted(proc_dict.items(), key=lambda x: x[0].lower()):
        pro.append(name)
    p = len(pro)
    for i in range(0, p):
        name = pro[i]
        k = name.lower()
        if("all" in f):
            he = name.replace(".exe", "")
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                if session.Process and session.Process.name() == "%s.exe" % he:
                    volume.SetMasterVolume(pica, None)
        if (f in k):
            he = name.replace(".exe", "")
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                if session.Process and session.Process.name() == "%s.exe" % he:
                    volume.SetMasterVolume(pica, None)
                    print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
        
                    

def prior(say):
        v("all apps",0.2)
        voice.out("%s"%say)
        v("all apps",1.0)
