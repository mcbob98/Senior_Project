file = open("/home/m/mcdevitt/cis597/129.10.zone.txt",'r')
mylist =[]
test = " "
for line in file:
   if line.find('ORIGIN') != -1:
      zone = (line[7:10] + ".zone,")
   if line.find('TTL') != -1:
      zone = zone + ("TTL," + line[5:11].strip()+",")
   if line.find('serial') != -1:
       zone = zone + ("serial," + line[:11].strip())
       mylist.append(zone.strip())
   if line.find('PTR') != -1:
       num = line.index("IN")
       num2 = line.index("PTR")
       
       mylist.append(line[:num].strip() +",".strip() + line[num+2:num2+3].strip()+"," + line[num2+3:].strip() + "\n")

file.close()

zone = open("10.zone.txt", 'w+')

for i in mylist:
    zone.write(str(i))