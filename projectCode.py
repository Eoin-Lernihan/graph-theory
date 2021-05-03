import sys
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--test', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='Help with testing the code')

print("Hello there user")
word = ''

path =  sys.argv[1]

word = sys.argv[2]
checker = word

containsMatch = "." in checker
endsWithMatch = checker.endswith('$')
startsWithMatch = checker.startswith('^')
exactMatch = startsWithMatch and endsWithMatch

digitMatch = ("/d" == checker)
notDigitMatch = ("/D" == checker)
if digitMatch or notDigitMatch:
  checker = "0|1|2|3|4|5|6|7|8|9"
characterMatch = ("/w" == checker)
notCharacterMatch = ("/W" == checker)
if characterMatch or notCharacterMatch:
  lowerChecker = "a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|"
  capChecker = "A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|"
  otherChecker = "_|0|1|2|3|4|5|6|7|8|9"
  alphaChecker = lowerChecker + capChecker + otherChecker
  checker = alphaChecker
  print(checker)
wordSepMatch = ("/s" == checker)
notWordSepMatch = ("/S" == checker)
if wordSepMatch or notWordSepMatch:
  checker =" |\t|\n"
alternatives = "|" in checker
trueWords = checker.split("|")

trueWord = word
crotchetEndsWithMatch = checker.endswith(']')
crotchetStartsWithMatch = checker.startswith('[')
crotchetsMatch = crotchetStartsWithMatch and crotchetEndsWithMatch

if containsMatch == True:
  trueWords = checker.split(".")[0]
if startsWithMatch == True:
  trueWord = trueWord.replace('^', '')
if endsWithMatch == True:
  trueWord = trueWord.replace('$', '')
if crotchetStartsWithMatch == True:
  trueWord = trueWord.replace('[', '')
if crotchetEndsWithMatch == True:
  trueWord = trueWord.replace(']', '')

f = open(path, 'r')
line = f.readline()
while line:
  if containsMatch:
    if any(substring in line for substring in trueWords):
      print(line)
  elif exactMatch:
    if trueWord in line:
      print(line)
  elif startsWithMatch:
    if line.startswith(trueWord):
      print(line)
  elif endsWithMatch:
    if line.endswith(trueWord):
      print(line)
  elif notDigitMatch or notCharacterMatch or notWordSepMatch:
    if not any(substring in line for substring in trueWords):
      print(line)
  elif alternatives:
    if any(substring in line for substring in trueWords):
      print(line)
  else:
    if trueWord in line:
      print(line)
     
  line = f.readline()
f.close()

print("Thank you for using this code:)")
print("Have a wondefulday")
