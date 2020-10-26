import jampy as jam #imports main tokenizer file
import os
import settings as s

while True:
    text = input("# ")

    if text == "echo on":
        s.ECHO = True 
        continue
    elif text == "echo off":
        s.ECHO = False
        continue
    if text == "debug on":
        s.DEBUG = True
        continue
    elif text == "debug off":
        s.DEBUG = False
        continue
    elif text == "clear":
        os.system("cls")
        continue

    if s.ECHO == True:
        print(text)

    jam.Tokenizer(text, s.DEBUG) #pass jam tokenizer
