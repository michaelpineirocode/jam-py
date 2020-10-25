#public variables. the deliminators do not need to be, but in case I want to change them later.
INTEGERS = "0123456789"
STRING_DELIMINATOR = '"'
EOF_DELIMINATOR = ';'

class Token:
    def __init__(self, KW_type, value):  #takes a type and a value
        self.KW_type = KW_type
        self.value = value

    def display(self):
        if self.value:
            return {self.KW_type: self.value} #if there is a value, displays the type and value
        else:
            return {self.KW_type: None} #displays just the type

class Tokenizer:

    def __init__(self, text):
        self.text = text #pulls the text
        self.pos = 0 #current position
        self.current_char() #pulls the character at 0 in the string
        self.seperate() #starts the main seperator

    def current_char(self):
        if self.pos < len(self.text):
            return self.text[self.pos]

    def next_char(self):
        if self.pos < len(self.text) - 1:
            return self.text[self.pos + 1]
        else:
            return -1

    def previous_char(self):
        if self.pos > 0:
            return self.text[self.pos - 1]
        else:
            return -1

    def forward(self):
        if self.pos < len(self.text):
            self.pos += 1
        else:
            return "end of sequence"

    def back(self):
        if self.pos > 0:
            self.pos -= 1
        else:
            print("Start of sequence")

    def seperate(self):
        self.tokens = []
        ignore = " \t\n"
        statements = "iwlrf"
        symbols = "()[]}{,:+-*&!=o."
        bools = "TF"

        while True:
            
            char = self.current_char()

            if char == None:
                if self.forward() != "end of sequence":
                    self.forward()
                else:
                    break
            elif char in ignore:
                self.forward()
            elif char in symbols and self.testDuo() != -1:
                self.testDuo()
            elif char == STRING_DELIMINATOR:
                self.addString()
            elif char in statements and self.addStatements() != -1:
                self.addStatements()
            elif char == EOF_DELIMINATOR:
                self.semicolon()
            elif char in INTEGERS:
                self.addInt()
            elif char in bools:
                self.addBool()
            elif char == -1:
                break
            else:
                self.addExpression()

        for i in range(len(self.tokens)):
            print(self.tokens[i].display()) #print the return of the display attribute in each token

    def testDuo(self):
        '''
        This function is complicated, so I will explain it here. I start off with
        a switch table of possible values depending on the first letter presented. 
        Then, I test to see if the character matches up with the switch table. If it does,
        then I check if the next character is a corresponding value in the table. If so,
        it appends and moves forward so that it will 'skip' the second character. Then I test
        if the character is only a key value and also not an 'o' (because o is not an operator),
        and if so it is an operator but only one character. Finally, if none of those are true,
        such as being a parenthesis, it will label it as a 'symbol,' although I am going to change
        that later.
        '''
        
        duoPairs = { #list of all two word combos 
            'o': 'r',        ''' I want to change this later, to be like the statements, and change && to 'and' '''
            '!': '=',
            '+': '=',
            '-': '=',
            '=': '=',
            "&": "&",
        }

        char = self.current_char() #sets the current character so that I do not need to recalculate
        
        if char in duoPairs.keys(): #tests if the character is in switch table
            if self.next_char() == duoPairs[char]: #tests if next character is the corresponding value
                self.tokens.append(Token("bichar operator", char + self.next_char()))
                self.forward() #moves forward once, to the next character
            elif char != duoPairs[char] and char != "o" and char != '!': #if it's a key but not a value and the key isn't o
                self.tokens.append(Token("onechar operator", char))
            else:
                self.back()
                return -1
        else:
            self.tokens.append(Token("symbol", char)) #if not just consider it a symbol(to be changed later)
        
        self.forward() #moves forward to the next text

    def addString(self):
        kw_string=[]
        start_pos = self.pos
        while True:
            self.forward()
            if self.current_char() == STRING_DELIMINATOR:
                endString = self.pos
                self.forward()
                break
        for i in range(endString - (start_pos - 1)):
            kw_string.append(self.text[start_pos + i])
        kw_string = "".join(kw_string)
            
        self.tokens.append(Token("string", kw_string))
        self.forward()

    def addStatements(self):
        char = self.current_char()
        possible_statements_from_char = {
            "w": "while",
            "r": "return",
            "l": "let",
            "f": "for"
        }
    
        starting_char = char
        if char in possible_statements_from_char.keys():
            state = []
            for i in range(len(possible_statements_from_char[char])):
                char = self.current_char()
                if char == possible_statements_from_char[starting_char][i]:
                    state.append(char)
                    self.forward()
                else:
                    backpedal = i
                    break
            state = "".join(state)
            if state == possible_statements_from_char[starting_char]:
                self.tokens.append(Token("statement", state))
            else:
                for i in range(backpedal):
                    self.back()
                    return -1

    def semicolon(self):
        self.tokens.append(Token("eof deliminator", EOF_DELIMINATOR))
        self.forward()

    def addInt(self):
        number = []
        while True:
            char = self.current_char()
            if str(char) in INTEGERS:
                number.append(self.text[self.pos])
                self.forward()
            else:
                break

        number = "".join(number)
        self.tokens.append(Token("integer", int(number)))
        self.forward()

    def addBool(self):
        KW_True = "True"
        KW_False = "False"
        state = []
        if self.current_char() == KW_True[0]:
            for i in range(len(KW_True)):
                char = self.current_char()
                if char == KW_True[i]:
                    state.append(char)
                    self.forward()
                else:
                    backpedal = i
                    break
            state = "".join(state)
            if state == KW_True:
                self.tokens.append(Token("Bool", state))
            else:
                for i in range(backpedal):
                    self.back()
        else:
            for i in range(len(KW_False)):
                char = self.current_char()
                if char == KW_False[i]:
                    state.append(char)
                    self.forward()
                else:
                    backpedal = i
                    break
            state = "".join(state)
            if state == KW_False:
                self.tokens.append(Token("Bool", state))
            else:
                for i in range(backpedal):
                    self.back()

    def addExpression(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_-" #should this be public?
        expression = []
        while True:
            char = self.current_char()
            if str(char) in letters:
                expression.append(char)
                self.forward()
            else:
                break
        expression = "".join(expression)
        self.tokens.append(Token("expression", expression))
