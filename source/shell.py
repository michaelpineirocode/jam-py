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
        try:
            os.system("cls")
        except:
            print("cannot clear")
        continue
    elif text == "help":
        f = open("help.txt", "r")
        print(f.read())
        f.close()
        continue
    elif text == "insert":
        path = input("Path: ")
        try:
            script = open(path, "r").read()
            jam.Tokenizer(str(script), s.DEBUG)
            continue
        except:
            print("Invalid path")
            continue    

    if s.ECHO == True:
        print(text) 

    jam.Tokenizer(str(text), s.DEBUG) #pass jam tokenizer
