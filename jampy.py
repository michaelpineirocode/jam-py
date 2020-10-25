INTEGERS = "0123456789"
STRING_DELLIMINATOR = '"'

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

    def symbols(self):
        return "()[]}{,;:+-*&!=o"

    def seperate(self):
        self.tokens = []
        ignore = " \t"
        
        while True:
            
            if self.current_char() == None:
                if self.forward() != "end of sequence":
                    self.forward()
                else:
                    break
            elif self.current_char() in ignore:
                self.forward()
            elif self.current_char() in self.symbols():
                self.testDuo()
            elif self.current_char() in STRING_DELLIMINATOR:
                self.addString()
            elif self.next_char() == -1:
                break

        for i in range(len(self.tokens)):
            print(self.tokens[i].display()) #print the return of the display attribute in each token
            

    def testDuo(self):
        duoPairs = {
            'o': 'r',
            '!': '=',
            '+': '=',
            '-': '=',
            '=': '=',
            "&": "&",
        }

        char = self.current_char()
        
        if char in duoPairs.keys():
            if self.next_char() == duoPairs[char]:
                self.tokens.append(Token("bichar operator", char + self.next_char()))
            elif char != duoPairs[char]:
                self.tokens.append(Token("onechar operator", char))
        else:
            self.tokens.append(Token("symbol", char))
        
        self.forward()

    def addString(self):
        kw_string=[]
        start_pos = self.pos
        while True:
            self.forward()
            if self.current_char() == STRING_DELLIMINATOR:
                endString = self.pos
                self.forward()
                break
        for i in range(endString - (start_pos - 1)):
            kw_string.append(self.text[start_pos + i])
        kw_string = "".join(kw_string)
            
        self.tokens.append(Token("string", kw_string))

