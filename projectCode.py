def prams():
 
 word = input("Enter the word you would like to found ")
 checker = word

 endsWithMatch = checker.endswith('$') 
 startsWithMatch =   checker.startswith('^')
 exactMatch = startsWithMatch and endsWithMatch

 if '.' in word :
    print("query found")
 if exactMatch == True :
    print (checker.endswith('$'))
    print (checker.startswith('^'))
    trueWord = word.replace("$", "")
 elif startsWithMatch == True :
    print (checker.startswith('^'))
 elif startsWithMatch == True :
    print (checker.endswith('$'))


 


print("Hello there user")
word=''
i = 0
i = float(input("Would you like to use this program today(yes is a number greater than 1)"))
while i > 1:
  
  path = input("Enter the directory you would like to use ")
  prams()
  
  f = open(path, 'w')
  f.write('cocacola\n')
  f.write('fanta and culb orange\n')
  f.write('z-up\n')
  f.close()
  f = open(path, 'r')
  line = f.readline() 
  while line:   
        if word in line:
                print("query found")
        line = line.rstrip() 
        # strip trailing spaces and newline
        # process the line
        print(line)
      
        line = f.readline()
  f.close()
  i = float(input("would you like to contineu "))

print("Thank you for using this code:)")
print("Have a wondefulday")









