#public variables. the deliminators do not need to be, but in case I want to change them later.
INTEGERS = "0123456789"
STRING_DELIMINATOR = '"'
EOL_DELIMINATOR = ';'

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

    def __init__(self, text, debug):
        self.text = text #pulls the text
        self.debug = debug # enables debug mode
        self.pos = 0 #current position
        self.current_char() #pulls the character at 0 in the string
        self.seperate() #starts the main seperator

    def current_char(self):
        if self.pos < len(self.text):
            return self.text[self.pos]

    def next_char(self, distance):
        if self.pos < len(self.text) - 1:
            return self.text[self.pos + distance]
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
        symbols = "()[]}{,:+-*&!|=/.><"
        bools = "TF"
        function_identifiers = "fd"

        while True:
            
            char = self.current_char()

            if char == None:
                if self.forward() != "end of sequence":
                    self.forward()
                else:
                    break
            elif char in ignore:
                self.forward()
            elif char in symbols:
                self.addOperators()
            elif char == STRING_DELIMINATOR:
                self.addString()
            elif char in statements and self.addStatements() != -1:
                self.addStatements()
            elif char == EOL_DELIMINATOR:
                self.semicolon()
            elif char in INTEGERS:
                self.addInt()
            elif char in function_identifiers and self.addFunction() != -1:
                self.addFunction()
            elif char in bools:
                self.addBool()
            elif char == 'i' and self.addInclude() != -1:
                self.addInclude()
            elif char == -1:
                break
            else:
                self.addExpression()
        
        if self.debug == True:
            for i in range(len(self.tokens)):
                print(self.tokens[i].display()) #print the return of the display attribute in each token
        
        Parser(self.tokens, self.debug)

    def addOperators(self):
        
        relational_operators = { #list of all two word combos 
            '|': '||',
            '!': '!=',
            '+': '+=',
            '-': '-=',
            '=': '==',
            "&": "&&",
            "<": "<=",
            ">": ">="                                                                                                                                                                                                      
            }
            
        char = self.current_char()
        if char in relational_operators.keys():
            if self.next_char(1) == relational_operators[char][1]:
                if char == '<' or char == '>' or char == '=' or char == '!':
                    self.tokens.append(Token("relational operator", char + self.next_char(1)))
                elif char == '&' or char == '|':
                    self.tokens.append(Token("logical operator", char + self.next_char(1)))
                elif char == "-" or char == "+":
                    self.tokens.append(Token("arithmetic operator", char + self.next_char(1)))
                self.forward()
            elif char == "=":
                self.tokens.append(Token("assignment", char))
            elif char == '+' or char == '-' or char:
                self.tokens.append(Token("arithmetic operator", char))
        elif char == '*' or char =='/':
            self.tokens.append(Token("arithmetic operator", char))
        else:
            self.tokens.append(Token("symbol", char))

        self.forward()
                
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
            "f": "for",
            "i": "if"
        }
    
        starting_char = char
        if char in possible_statements_from_char.keys():
            state = []
            for i in range(len(possible_statements_from_char[char])):
                if self.pos + i < len(self.text):
                    state.append(self.next_char(i))
            if str("".join(state)) == possible_statements_from_char[char]:
                self.tokens.append(Token("statement", possible_statements_from_char[char]))
                for i in range(len(possible_statements_from_char[char])):
                    self.forward()
            else:
                return -1

    def semicolon(self):
        self.tokens.append(Token("eol deliminator", EOL_DELIMINATOR))
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
        self.tokens.append(Token("integer", number))
        self.forward()

    def addFunction(self):
        char = self.current_char()
        funct = {
        "d": "def",
        "f": "function"
        }
        
        if char in funct.keys():
            state = []
            for i in range(len(funct[char])):
                if self.pos + i < len(self.text):
                    state.append(self.next_char(i))
                else:    
                    break
            if str("".join(state)) == funct[char]:
                self.tokens.append(Token("function", funct[char]))
                for i in range(len(funct[char])):
                    self.forward()
            else:
                return -1

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

    def addInclude(self):
        
        state = []
        if self.next_char(1) == 'm':
            for i in range(len("import")):
                if i + len("import") < len(self.text):
                    state.append(self.next_char(i))
                else:
                    break
            if str("".join(state)) == "import":
                self.tokens.append(Token("module", "import"))
                for i in range(len("import")):
                    self.forward()
            else:
                return -1
        
        elif self.next_char(1) == 'n':
            for i in range(len("include")):
                if i + len("include") < len(self.text):
                    state.append(self.next_char(i))
                else:
                    break
            if str("".join(self.text)) == "include":
                self.tokens.append(Token("module", "include"))
                for i in range(len("include")):
                    self.forward()
        else:
            return -1

class Parser:
    def __init__(self, tokens, debug):
        self.tokens = tokens
        self.debug = debug
        self.pos = 0
