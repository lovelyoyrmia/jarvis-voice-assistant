from os import startfile
from time import sleep
from keyboard import press
from keyboard import write
from pyautogui import click

def whatsappMessage(name,message):
    startfile('C:\\Users\\user\\AppData\\Local\\WhatsApp\\WhatsApp.exe')

    sleep(10)

    # Coordinat text field search
    click(x=353, y=169)

    sleep(2)

    write(name)

    sleep(2)

    # Coordinat press the name
    click(x=306, y=292)

    sleep(5)

    click(x=660, y=660)

    write(message)

    press('enter')

def whatsappOpenChat(name):

    startfile('C:\\Users\\user\\AppData\\Local\\WhatsApp\\WhatsApp.exe')

    sleep(10)

    # Coordinat text field search
    click(x=353, y=169)

    sleep(1)

    write(name)

    sleep(1)

    # Coordinat press the name
    click(x=306, y=292)

def whatsappCall(name):
    startfile('C:\\Users\\user\\AppData\\Local\\WhatsApp\\WhatsApp.exe')

    sleep(10)

    click(x=353, y=169)

    sleep(1)

    write(name)

    sleep(1)

    click(x=306, y=292)

    sleep(2)

    click(x=1027, y=105)

def whatsappVideoCall(name):

    startfile('C:\\Users\\user\\AppData\\Local\\WhatsApp\\WhatsApp.exe')

    sleep(5)

    click(x=353, y=169)

    sleep(1)

    write(name)

    sleep(1)

    click(x=306, y=292)

    sleep(2)

    click(x=984, y=125)
