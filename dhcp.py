file = open("/home/m/mcdevitt/cis597/dhcp.txt",'r')
mylist =[]


for line in file:
    if line.find('host-name') != -1:
        mylist.append(line[line.find('host-name')+11:-3].strip())
    if line.find('ethernet') != -1:
        mylist.append(line[line.find('ethernet')+8:-2].strip())
    if line.find('fixed-address') != -1:
        mylist.append(line[line.find('fixed-address')+14:-2].strip())

file.close()

host = open("hosts.txt", 'w+')
k  = 0
l = int(len(mylist) / 3)
print(mylist)
for i in range(l): # host.write(mylist[k] + " ")
    host.write("insert into host(hostname) values('{0}');\n".format(mylist[k])
               +"insert into mac(mac_adrress) values('{0}');\n".format(mylist[k+1])
               + "insert into ip(ip_address) values('{0}');\n".format(mylist[k+2]))
    k = k + 3
    host.write("\n")


host.close()