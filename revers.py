file = open("/home/m/mcdevitt/cis597/revers.txt",'r')
mylist =[]

for line in file:
    if line.find('IN') != -1:
        num  = line.index('IN')
        print(line[:num])
    if line.find('PTR') != -1:
        n = line.index('PTR')
        print(line[n+4:].strip())