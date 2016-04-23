import psycopg2
#connection string to our database
try:
    conn =  psycopg2.connect(database='dnsdb', user='mcdevitt', password='IgetP@id$$15', host='129.130.10.32', port='5432', sslmode='require')
except:
    print("connetion error")

cur = conn.cursor()

file = open("hosts.txt", 'r')
i = 0
for line in file:
    row = line.split(" ") # Get each line
    name = row[i]
    address = row[i+1]
    cur.execute("insert into host(hostname) values ('name')");
    cur.execute("insert into mac(mac_address) values('address')");
    #cur.execute("insert into ip()")
    print(row[i] + " " + row[i + 1] + " " + row[i + 2])
    i = 0