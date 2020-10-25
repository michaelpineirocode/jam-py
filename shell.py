import jampy as jam #imports main tokenizer file

ECHO = True

while True:
    text = input("# ")

    if text == "echo on":
        ECHO = True
        continue
    elif text == "echo off":
        ECHO = False
        continue

    if ECHO == True:
        print(text)

    jam.Tokenizer(text) #pass jam tokenizer
    
