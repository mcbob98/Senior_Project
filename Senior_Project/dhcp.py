file = open("/home/m/mcdevitt/cis597/dhcp.txt",'r')
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
l = int(len(mylist) / 3)
k= 0
table = [[0 for r in range(3)]for c in range(5)]
for row in range(3):
    for col in range(3):
        table[row][col] = mylist[k].rstrip()
        k = k + 1
print(table)