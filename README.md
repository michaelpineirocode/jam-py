

# JAMPY ![alt text](https://github.com/michaelpineirocode/jam-py/blob/main/jampypic-removebg-preview.png?raw=true)

Jam-py is a <b>proof of concept/educational experience</b> to learn the fundementals of compiled interpreted programming languages. It is developed inside of Python, but the same approaches can be made in lower level programming languages. I am interested to see if I can implement a similar project in C++ in the future. I currently plan on creating a lexer and a parser, and then I may come back to create an interpretor in the future.

# Install
Jampy relies on the "os" module for the "clear" command within the shell. So, "clear" will not work on Linux or Unix systems until I get around to fixing that issue.
To install jampy, 

# Shell commands
The shell utilizes the following specialized commands:
>echo on/off - reprint the command.
>debug on/off - turns on debug mode. As of now, debug only displays tokens registered by the tokenizer.
>clear - clears the shell. Only works with Windows computers, as of now.
>help - prints the list of commands and descriptions

# Dependencies
Jampy relies on the following dependencies:
>built-in "os" module.
>python3 and up.

# Motivation

Jam-py is one of my ongoing projects to learn about interpreted programming languages. It has uses in many forms though, through the development of a lexer and parser, which have use cases including but not limited to translators, grammer checkers, and interpreted programming languages.

# Build Status

Working, not functional

# Limitations

<b>There cannot be a term that starts with the name of words in our namespace.</b> For example, "define" and "functionality" could not be variable names, because they contain the key words "def" and "function" at the beginning. I do not think that this issue is massive, though, and I may be able to change it later.

<b>It is slow.</b> The text is interpreted using python, to make a language that is less easy to understand. It performs the way that a 'high level' programming language should(slowly), yet is written in a way that is 'lower level' (more complicated).

# Demo
Once I make a release, I will include a demo - probably a link to a jupyter or collabratory notebook. I am not yet sure how to implement this. Or, you can just download it.


# Contact
I can be contacted via the following email:<b> michaelpineiro.code@gmail.com </b>
