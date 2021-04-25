path = input("Enter the direct  ")
word = input("Enter the word you would like to found ")
f = open('test.txt', 'w')
f.write('cocacola\n')
f.write('fanta and culb orange\n')
f.write('z-up\n')
f.close()
f = open('test.txt', 'r')
line = f.readline() 
while line:
        
        if word in line:
                print("query found")
        line = line.rstrip()  # strip trailing spaces and newline
        # process the line
        print(line)
        line = f.readline()
f.close()