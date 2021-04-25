path = 'c:\\Users\\eoinb\\Desktop\\graphy thory\\graph-theory\\test.txt'
f = open('test.txt', 'w')
f.write('cocacola\n')
f.write('fanta and culb orange\n')
f.write('z-up\n')
f.close()
f = open('test.txt', 'r')
line = f.readline() 
while line:
        
        if "culb" in line:
                print("query found")
        line = line.rstrip()  # strip trailing spaces and newline
        # process the line
        print(line)
        line = f.readline()
f.close()
f = open('test.txt', 'r')
line = f.readline() 

if "culb" in line:
    print("query found")
f.close()
