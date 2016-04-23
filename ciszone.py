file = open("/home/m/mcdevitt/cis597/pointer.txt",'r')
mylist =[]

for line in file:
    if line.find('IN') != -1:
        num  = line.index('IN')
        print(line[:num])
    if line.format('CNAME') != -1:
        n = line.index('CNAME')
        print(line[n+5:].strip())




