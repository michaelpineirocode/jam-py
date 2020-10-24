INTEGERS = "0123456789"

class Token:
    def __init__(self, KW_type, value):
        self.KW_type = KW_type
        self.value = value


    def display(self):
        if self.value:
            return {self.KW_type: self.value}
        else:
            return {self.KW_type: None}
    

class Tokenizer:

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.posValue = None
        self.current_char()
        self.tokens = []
        self.duoPairs = {
            'o': 'r',
            '!': '=',
            '+': '=',
            '-': '=',
            '=': '=',
            "&": "&",
        }

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
            print("End of sequence")

    def back(self):
        if self.pos > 0:
            self.pos -= 1
        else:
            print("Start of sequence")

    def seperate(self):
        ignore = " \t"
        symbols = "()[]}{,;:+-*&!=o"
        
        while True:
            
            if self.current_char() == None:
                if self.forward() != "end of sequence":
                    self.forward()
                else:
                    break
            elif self.current_char() in ignore:
                self.forward()
            elif self.current_char() in symbols:
                self.testDuo()
            elif self.current_char() in INTEGERS:
                self.addInt()
            elif self.next_char() == -1:
                break

        for i in range(len(self.tokens)):
            print(self.tokens[i].display())
            

    def testDuo(self):

        if self.current_char() in duoPairs.keys():
            if self.next_char() == duoPairs.get(self.current_char()):
                self.tokens.append(Token("operator","{self.current_char()}{self.next_char()}"))
                if self.next_char() != -1:
                    self.forward()
            else:
                self.tokens.append(Token("operator", self.current_char()))
                if self.next_char() != -1:
                    self.forward()

    def addInt(self):
        self.tokens.append(Token("int", int(self.current_char())))
        self.forward()

tk = Tokenizer(" + - = ! 1 3 -= 1 +")

tk.seperate()
