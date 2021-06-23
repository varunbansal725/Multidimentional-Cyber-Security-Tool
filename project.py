import os
import requests
import getpass
import socket
import platform
os.system("tput setaf 4")
print("\t\tWelcome to the TUI that makes your life simpler")
os.system("tput setaf 5")
print("\t\t\tBe the root user to use this TUI")
os.system("tput setaf 7")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
print("What operation do you want to perform?", end="")
while True:
    print("""Menu for Operations-
        1. Get HTTP Header                              25. Retrieve a text from a picture using Steganography
        2. UDP scan                                     26. Perform ARPspoof attack
        3. John the Ripper tool                         27. iOT device scan          
        4. SQLmap                                       28. Perform website footprinting
        5. DNS Lookup                                   29. Check for SQL vulnerabilities in a website   
        6. Reverse IP Lookup                            30. Check for Load Balancing Information of a website
        7. Get "Robots.txt" file of a website           31. Discover e-mail accounts of a company
        8. IP Locator                                   32. Discover a website for Directories & Files
        9. Host Finder                                  33. Mirror a website
        10. Use Recon-ng tool                           34. Embed a text in a picture using Steganography
        11. GeoIP Finder                                35. LLMNR/NBT-NR poisoning
        12. Subnet Finder                               36. E-mail account footprinting
        13. Whois information                           37. Create a customized Dictionary
        14. ARP scan                                    38. Exit
        15. ICMP ECHO Ping scan                         
        16. TCP SYN Ping scan
        17. TCP Connect scan
        18. Stealth scan
        19. XMAS scan
        20. FIN scan
        21. Service Version Discovery
        22. OS Discovery
        23. Display ARP cache table
        24. Scan a website for basic information
    Enter the S.No. corresponding to the operation to be performed: """, end="")
    operation_number=input()
    if int(operation_number)==1:
        victim1 = input("Enter the website address: ")
        os.system("curl -i {}".format(victim1))
    elif int(operation_number)==2:
        print("Enter the target IP address: ", end="")
        target_ip=input()
        os.system("apt-get install nmap")
        os.system("nmap -sn -PU {}".format(target_ip))
    elif int(operation_number)==4:
        sqlmap_victim=input("Enter the website address: ")
        os.system("apt-get install sqlmap")
        os.system("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev")
        sql = 'https://'+sqlmap_victim+'/index.php?id=1'
        os.system("sqlmap --url {}".format(sql))
    elif int(operation_number)==5:
        victim = input("Enter the website address: ")
        os.system("apt-get install dnsutils")
        os.system("nslookup {}".format(victim))
    elif int(operation_number)==6:
        victim = input("Enter the IP address: ")
        os.system("apt-get install dnsutils")
        os.system("nslookup {}".format(victim))
    elif int(operation_number)==7:
        victim = input("Enter the website address: ")
        robots = 'https://'+victim+'/robots.txt'
        info = requests.get(robots)
        print('\033[94m',info.text)
    elif int(operation_number)==8:
        victim = input("Enter the ip address: ")
        os.system("curl ipinfo.io/{}".format(victim))
    elif int(operation_number)==9:
        victim = input("Enter the domain name/ip address for the host: ")
        os.system("apt-get install dnsutils")
        os.system("host {}".format(victim))
    elif int(operation_number)==10:
        print("Enter the name of the workspace you wish to create: ", end="")
        workspace=input()
        os.system("git clone https://github.com/lanmaster53/recon-ng.git")
        os.system("recon-ng -w {}".format(workspace))
    elif int(operation_number)==11:
        geoip_victim = input("Enter the website address: ")
        os.system("geoiplookup {}".format(geoip_victim))
    elif int(operation_number)==12:
        sub_victim = input("Enter the website's server address: ")
        os.system("apt install ipcalc")
        os.system("ipcalc {}".format(sub_victim))
    elif int(operation_number)==13:
        victim = input("Enter the website address: ")
        os.system("apt-get install whois")
        os.system("whois {}".format(victim))
    elif int(operation_number)==14:
        print("Enter the target IP address: ", end="")
        target_ip=input()
        os.system("apt-get install nmap")
        os.system("nmap -sn -PR {}".format(target_ip))
    elif int(operation_number)==15:
        print("Enter the target IP address: ", end="")
        target_ip=input()
        os.system("apt-get install nmap")
        os.system("nmap -sn -PE {}".format(target_ip))
    elif int(operation_number)==16:
        print("Enter the target IP address: ", end="")
        target_ip=input()
        os.system("apt-get install nmap")
        os.system("nmap -sn -PS {}".format(target_ip))
    elif int(operation_number)==17:
        target_ip=input("Enter the target IP address: ")
        os.system("apt-get install nmap")
        os.system("nmap -sT -v {}".format(target_ip))
    elif int(operation_number)==18:
        target_ip=input("Enter the target IP address: ")
        os.system("apt-get install nmap")
        os.system("nmap -sS -v {}".format(target_ip))
    elif int(operation_number)==19:
        target_ip=input("Enter the target IP address: ")
        os.system("apt-get install nmap")
        os.system("nmap -sX -v {}".format(target_ip))
    elif int(operation_number)==20:
        target_ip=input("Enter the target IP address: ")
        os.system("apt-get install nmap")
        os.system("nmap -sF -v {}".format(target_ip))
    elif int(operation_number)==21:
        print("Enter the target IP address: ")
        target_ip=input()
        os.system("apt-get install nmap")
        os.system("nmap -sV {}".format(target_ip))
    elif int(operation_number)==22:
        target_ip=input("Enter the target IP address: ")
        os.system("apt-get install nmap")
        os.system("nmap -O {}".format(target_ip))
    elif int(operation_number)==23:
        arp_victim = input("Enter the IP address whose ARP cache has to be retrieved: ")
        os.system("apt-get install arp-scan")
        os.system("arp -a {}".format(arp_victim))
    elif int(operation_number)==24:
        nikto_victim = input("Enter the website URL: ")
        os.system("apt-get install nikto -y")
        os.system("nikto -host {} -ssl".format(nikto_victim))
    elif int(operation_number)==25:
        stego_input= input("Enter the image file name from which you want to retrieve the secret text from: ")
        os.system("cryptosteganography retrieve -i {}".format(stego_input))
    elif int(operation_number)==26:
        card_name = input("Enter the network card name: ")
        print("The target should be on the same network of the attacker\n")
        arpspoof_target = input("Enter the target IP address: ")
        arpspoof_attacker=input("Enter the IP address of the machine with which the target has to be spoofed: ")
        os.system("arpspoof -i {} -t {} {}".format(card_name, arpspoof_target, arpspoof_attacker))
    elif int(operation_number)==27:
        os.system("apt-get install nmap")
        iot_target = input("Enter the IP address of the target iOT device: ")
        os.system("nmap -n -Pn -sS -pT:0-65535 -v -A -oX {}".format(iot_target))
    elif int(operation_number)==28:
        target_whatweb = input("Enter the URL of the website: ")
        os.system("whatweb {}".format(target_whatweb))
    elif int(operation_number)==29:
        target_dsss = input("Enter the target URL for scanning: ")
        os.system("git clone https://github.com/stamparm/DSSS.git")
        os.system("cd DSSS")
        os.system("python dsss.py -u {}".format(target_dsss))
    elif int(operation_number)==30:
        target_lbd = input("Enter the URL for the target: ")
        os.system("lbd {}".format(target_lbd))
    elif int(operation_number)==31:
        target_infoga1 == input("Enter the URL of the target company's website: ")
        os.system("git clone https://github.com/m4ll0k/Infoga.git Infoga")
        os.system("cd Infoga")
        os.system("pip install -r requirements.txt")
        os.system("python3 infoga.py --domain {} --source google --verbose 3".format(target_infoga1))
    elif int(operation_number)==32:
        target_scan = input("Enter the target website URL: ")
        os.system("apt-get install gobuster")
        os.system("apt-get install seclists")
        os.system("gobuster -dir --url {} -w /usr/share/dirb/wordlists/common.txt".format(target_scan))
    elif int(operation_number)==33:
        mirror_target = input("Enter the website to be mirrored: ")
        os.system("apt-get install httrack")
        os.system("httrack {}".format(mirror_target))
    elif int(operation_number)==34:
        print("Your image should be in the same folder as of this tool")
        secret_text = input("Enter the text to be embedded: ")
        image_name = input("Enter the name of the image file: ")
        os.system("pip3 install cryptosteganography")
        os.system("cryptosteganography save -i {} -m '{}' -o {}".format(image_name, secret_text, image_name)) 
    elif int(operation_number)==35:
        responder_target = input("Enter the IP address of the host: ")
        os.system("responder -i {} -w On -r On -f On".format(responder_target))
    elif int(operation_number)==36:
        infoga_target = input("Enter the full email account: ")
        os.system("git clone https://github.com/m4ll0k/Infoga.git infoga")
        os.system("cd infoga")
        os.system("pip install -r requirements.txt")
        os.system("python3 infoga.py --info {} --source google -v 3".format(infoga_target))
    elif int(operation_number)==37:
        dictionary_input = input("Enter the characters/numbers to create the dictionary: ")
        min_input = input("Enter the minimum length of a word in the dictionary: ")
        max_input = input("Enter the maximum length of a word in the dictionary: ")
        output_file = input("Enter the name of the output file: ")
        os.system("crunch {} {} {} -o {}".format(min_input, max_input, dictionary_input, output_file))
    elif int(operation_number)==38:
        exit()
    else: print("Invalid Input")
    input("Enter to continue....")
    os.system("clear")
