import jampy as jam #imports main tokenizer file

ECHO = True
DEBUG = False
while True:
    text = input("# ")

    if text == "echo on":
        ECHO = True 
        continue
    elif text == "echo off":
        ECHO = False
        continue
    if text == "debug on":
        DEBUG = True
        continue
    elif text == "debug off":
        DEBUG = False
        continue

    if ECHO == True:
        print(text)

    jam.Tokenizer(text, DEBUG) #pass jam tokenizer
