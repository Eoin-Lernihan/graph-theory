import sys
import argparse


class RegularMatch:
    """class for doing simple regular expression matches"""
    
    def __init__(self, pattern):
    # True if this is an accept state. 
        self.word = pattern

    def compile(self):
        self.checker = self.word
        self.containsMatch = "." in self.checker
        self.endsWithMatch = self.checker.endswith('$')
        self.startsWithMatch = self.checker.startswith('^')
        self.exactMatch = self.startsWithMatch and self.endsWithMatch

        self.digitMatch = ("\d" ==self. checker)
        self.notDigitMatch = ("\D" == self.checker)
        if self.digitMatch or self.notDigitMatch:
            self.checker = "0|1|2|3|4|5|6|7|8|9"
        self.characterMatch = ("\w" == self.checker)
        self.notCharacterMatch = ("\W" == self.checker)
        if self.characterMatch or self.notCharacterMatch:
            self.lowerChecker = "a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|"
            self.capChecker = "A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|"
            self.otherChecker = "_|0|1|2|3|4|5|6|7|8|9"
            self.alphaChecker = self.lowerChecker + self.capChecker + self.otherChecker
            self.checker = self.alphaChecker
            print(self.checker)
        self.wordSepMatch = ("\s" == self.checker)
        self.notWordSepMatch = ("\S" == self.checker)
        if self.wordSepMatch or self.notWordSepMatch:
            self.checker =" |\t|\n"
        self.alternatives = "|" in self.checker
        self.patterns = self.checker.split("|")
        if self.containsMatch == True:
            self.patterns = self.checker.split(".")[0]
        if self.startsWithMatch == True:
            self.trueWord = self.trueWord.replace('^', '')
        if self.endsWithMatch == True:
            self.trueWord = self.trueWord.replace('$', '')

    def match(self, line):
        if self.exactMatch:
            if self.trueWord in line:
                print("Matched ", word, "in >>>" , line.strip(), "<<<")            
        elif self.startsWithMatch:
            if line.startswith(self.trueWord):
                print("Matched ", word, "in >>>" , line.strip(), "<<<")            
        elif self.endsWithMatch:
            if line.endswith(self.trueWord):
                print("Matched ", word, "in >>>" , line.strip(), "<<<")            
        elif self.containsMatch:
            if any(substring in line for substring in self.patterns):
                print("Matched ", word, "in >>>" , line.strip(), "<<<")            
        elif self.notDigitMatch or self.notCharacterMatch or self.notWordSepMatch:
            if not any(substring in line for substring in self.patterns):
                print("Matched ", word, "in >>>" , line.strip(), "<<<")            
        elif self.alternatives:
            if any(substring in line for substring in self.patterns):
                print("Matched ", word, "in >>>" , line.strip(), "<<<")            
        else:
            if self.trueWord in line:
                print("Matched ", word, "in >>>" , line.strip(), "<<<")            




parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--test', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='Help with testing the code')

print("Hello there user")
word = ''

path =  sys.argv[1]

word = sys.argv[2]

regulaurMatcher = RegularMatch(word) 
regulaurMatcher.compile()


f = open(path, 'r')
line = f.readline()
while line:
  regulaurMatcher.match(line)   
  line = f.readline()
f.close()

print("")
print("====Finished Matching=======")
print("Thank you for using this code:)")
print("Have a wondefulday")
