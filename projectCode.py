print("Hello there user")
word = ''

path = input("Enter the directory you would like to use ")

word = input("Enter the regular expertion you would like to found ")
checker = word
endsWithMatch = checker.endswith('$')
startsWithMatch = checker.startswith('^')
digitMatch = ("/d" == checker)
if digitMatch:
  checker = "0|1|2|3|4|5|6|7|8|9"
alternatives = "|" in checker
trueWords = checker.split("|")
exactMatch = startsWithMatch and endsWithMatch
print(exactMatch)
trueWord = word
if '.' in word:
  print("query found")
if startsWithMatch == True:
  trueWord = trueWord.replace('^', '')
if endsWithMatch == True:
  trueWord = trueWord.replace('$', '')
f = open(path, 'r')
line = f.readline()
while line:
  if exactMatch:
    if trueWord == line:
      print("exactMatch found")
      line = line.rstrip()
  elif startsWithMatch:
    if line.startswith(trueWord):
      print("query found")
      line = line.rstrip()
  elif endsWithMatch:
    if line.endswith(trueWord):
      print(line)
      line = line.rstrip()
  elif alternatives:
    if any(substring in line for substring in trueWords):
      print("alternatives query found")
      line = line.rstrip()
  else:
    if trueWord in line:
      print("query found")
      line = line.rstrip()
      print(line)
  line = f.readline()
f.close()

print("Thank you for using this code:)")
print("Have a wondefulday")
