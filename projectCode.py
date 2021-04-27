def prams():
 word = input("Enter the word you would like to found ")



print("Hello there user")
word=''
i = 0
i = float(input("Would you like to use this program today"))
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
  i = input("would you like to contineu ")

print("Thank you for using this code:)")
print("Have a wondefulday")









