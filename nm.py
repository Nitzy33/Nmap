import nmap

scanner = nmap.PortScanner()

print ("welcome")

ip_addr = input("please enter the ip ")

print ("the ip address is", ip_addr)

resp = input ("""\n Please enter the type of scan you want to run
		  1. SYN ACK SCAN
		  2. UDP SCAN
		  3. Comprehensive Scan\n""")
	
	
print ("you have selected the version", resp)

if resp == '1':
    
    print ("nmap version is", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print (scanner.scaninfo())
    print ("IP Status: ", scanner[ip_addr].state())
    print (scanner[ip_addr].all_protocols())
    print ("open ports: ", scanner [ip_addr]['tcp'].keys())

elif resp == '2':
    
    print ("nmap version is", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print (scanner.scaninfo())
    print ("IP Status: ", scanner[ip_addr].state())
    print (scanner[ip_addr].all_protocols())
    print ("open ports: ", scanner [ip_addr]['udp'].keys())


elif resp == '3':
    print ("nmap version is", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print (scanner.scaninfo())
    print ("IP Status: ", scanner[ip_addr].state())
    print (scanner[ip_addr].all_protocols())
    print ("open ports: ", scanner [ip_addr]['tcp'].keys())
    
elif resp >= '4':

    print ("Out of Range")    
		  
