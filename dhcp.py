file = open("/Users/robertmcdevitt/Desktop/cis597/dhcp.txt",'r')
mylist =[]
char ='"'
for line in file:
    if line.find('host-name') != -1:
        mylist.append(line[line.find('host-name')+11:len(line)-3])
    if line.find('ethernet') != -1:
        mylist.append(line[line.find('ethernet')+8:])
    if line.find('fixed-address') != -1:
        mylist.append(line[line.find('fixed-address')+14:])

file.close()
print(mylist)