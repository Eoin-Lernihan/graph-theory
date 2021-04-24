path = 'c:\\Users\\eoinb\\Desktop\\graphy thory\\graph-theory\\test.txt'
f = open('test.txt', 'w')
f.write('cola\n')
f.write('fanta\n')
f.write('z-up\n')
f.close()
f = open('test.txt', 'r')
line = f.readline() 
while line:
        line = line.rstrip()  # strip trailing spaces and newline
        # process the line
        print(line)
        line = f.readline()
f.close()