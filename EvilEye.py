import socket
import os
from _datetime import datetime
import requests
from phonenumbers import carrier, timezone, parse, is_valid_number
from bs4 import BeautifulSoup
from urllib.parse import urlsplit, urljoin,urlparse



logo = """
           .-=========-.
      .-'  ()     ()   '-.
    .'       EVIL EYE       '.
   /  ()       ()     ()      \
  |     .-----------------.     |
  |    |   ░E ░V ░I ░L    |    |
  |    |      ░E ░Y ░E    |    |
   \     '-----------------'    /
    '.   ()       ()        .'
      '-.             () .-'
          '-._______.-'
                     
                 Dev: RichNet(N3TIX)
        Warning: This tool is for EDUCATIONAL intent        
"""


def clear_inter():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def break_validation():
    conti = input("[+] Do you want to continue (y/n): ")
    if conti == "y":
        pass
    elif conti == "n":
        print("\033[31m"+"[+] Programme quited !!\033[0m")
        exit()


def ports_scan():
    print("""\033[5;32m
┌─────────────────────────────┐
│   P O R T  S C A N N E R    │
├─────────────────────────────┤
│  ▸ scanning…                │
│  ▸ checking open ports      │
└─────────────────────────────┘
\033[0m
NETWORK port scanning tool
     Dev: RichNet(N3TIX)
Warning: This tool is for EDUCATIONAL intent\033[0m
""")
    try:
        url = input("[+] Input URL/IP Address: ")
        host = socket.gethostbyname(url)
        print(f"[+] scanning open ports on  {url} IP: {host} ......\n[+] Scanning Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
        #sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        for port in range(20,1000):
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            conn = sock.connect_ex((host,port))
            sock.settimeout(0.2)
            if conn == 0:
                print(f"PORT TCP\\{port} :  Open")
    except socket.gaierror:
        print("check your internet connection and try again")
    except KeyboardInterrupt:
        print("Programme Terminated !!!")


def ipinfo():
    # ipinfo_banner.py

    print("""\033[1;34m
 ** *******        ** ****     ** ********   *******  
/**/**////**      /**/**/**   /**/**/////   **/////** 
/**/**   /**      /**/**//**  /**/**       **     //**
/**/*******  *****/**/** //** /**/******* /**      /**
/**/**////  ///// /**/**  //**/**/**////  /**      /**
/**/**            /**/**   //****/**      //**     ** 
/**/**            /**/**    //***/**       //*******  
// //             // //      /// //         ///////   
""")
    print("            \033[1;33mDev: RchNet\033[0m\n")

    try:
        target_ip = input("[+] Input Your Target IP: ")
        url_ip = socket.gethostbyname(target_ip)
        reqst = requests.get(f"https://ipinfo.io/{url_ip}/json")
        resp = reqst.status_code
        if resp == 200:
            data = reqst.json()
            print(f"\n\033[32mIP : {data.get("ip")}")
            print(f"Host : {data.get("hostname")}")
            print(f"City : {data.get("city")}")
            print(f"Region : {data.get("region")}")
            print(f"country : {data.get("country")}")
            print(f"IP GPS : {data.get("loc")}")
            print(f"Organization : {data.get("org")}")
            print(f"Postal Address : {data.get("postal")}")
            print(f"Timezone : {data.get("timezone")}\033[0m\n")
        else:
            print("Can't fatch Data.... TRY AGAIN letter!!")
    except socket.gaierror:
        print("server NOT found!!")



def emailfarm():
    pass


def phonenumber():
    print("""
 ▄▀▀▄▀▀▀▄  ▄▀▀▄ ▄▄   ▄▀▀▀▀▄   ▄▀▀▄ ▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄  ▄▀▀▄ ▄▀▀▄  ▄▀▀▄ ▄▀▄ 
█   █   █ █  █   ▄▀ █      █ █  █ █ █ ▐  ▄▀   ▐ █  █ █ █ █   █    █ █  █ ▀  █ 
▐  █▀▀▀▀  ▐  █▄▄▄█  █      █ ▐  █  ▀█   █▄▄▄▄▄  ▐  █  ▀█ ▐  █    █  ▐  █    █ 
   █         █   █  ▀▄    ▄▀   █   █    █    ▌    █   █    █    █     █    █  
 ▄▀         ▄▀  ▄▀    ▀▀▀▀   ▄▀   █    ▄▀▄▄▄▄   ▄▀   █      ▀▄▄▄▄▀  ▄▀   ▄▀   
█          █   █             █    ▐    █    ▐   █    ▐              █    █    
▐          ▐   ▐             ▐         ▐        ▐                   ▐    ▐     
                                                                      Dev: RchNet        
                                                                                                                                                                 
""")
    number = input("[+] INPUT TARGET PHONENUMBER: ")
    parser = parse(number,"RO")
    valid = is_valid_number(parser)
    carrier_n = carrier.name_for_number(parser, "en")
    time_zone = timezone.time_zones_for_number(parser)
    print(f"{parser}")
    print(f"""Timezone : {time_zone}
Carrier : {carrier_n}
Valid : {valid}
""")


def urlscrapper():
    try:
        try:
            logo = """\033[1;32m
                  U  U  R__  L_       S__  P__   A_   E__  R__ 
                | | | || _\.| |      / __)| _\. / \_.| __)| _\.
              | |_| ||   /.| |__    \__ \.|  _/./___\.| _| .|   /.
               \___/.|_|_\.|____|   |___/.|_|  .|   |.|___|.|_|_\.\033[0m
                                               |   |.  dev: RichNet        
                                                               
"""
            print(logo)
            url = input("[+] Input url IN (http or https form): ")
            keyword = input("[+] Target keyword in URL (optional): ")
            req = requests.get(url)
            soup = BeautifulSoup(req.content, "html.parser")
            result = soup.find_all("a")
            for links in result:
                urls = links.get("href")
                full_url = urljoin(url,urls)
                if keyword in full_url:
                    with open("URL.txt","a") as x:
                        x.write(f"[+] {full_url}\n")
                    print("\033[1;36m"+full_url+"\033[0m")
        except requests.exceptions.MissingSchema:
            print("[+] INVALID INPUT FORMATE!!")
    except requests.exceptions.ConnectionError:
        print("[+] Can't connect to server; CHECK INTERNET CONNECTION!!")


def sub_domain(a,b):
    try:
        parse = urlparse(url)
        domain = parse.netloc
        with open(wordlist,"r") as f:
            words = f.read()
            word = words.split()
            for wd in word:
                join_sub = parse.netloc.replace("www",wd)
                full_url = parse.scheme+"://"+join_sub
                try:
                    request = requests.get(full_url,timeout=2)
                    status = request.status_code
                    if status == 200:
                        with open("result.txt","a") as x:
                            x.write(full_url+"\n")
                        print("\033[1;36m"+full_url+"\033[0m")
                    else:
                        pass
                except requests.exceptions.ConnectionError:
                    pass
                except requests.exceptions.ReadTimeout:
                    pass
    except KeyboardInterrupt:
        print("[+] Programme interupted!!")
    except requests.exceptions.InvalidSchema:
        print("[+]INVALID INPUT!!")

sub_logo = """\033[5;36m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~               ____            _  __          _    __        ~
~ ___   _   _  | __ )          | |/ /  _ __   (_)  / _|   ___ ~
~/ __| | | | | |  _ \   _____  | ' /  | '_ \  | | | |_   / _ \~
~\__ \ | |_| | | |_) | |_____| | . \  | | | | | | |  _| |  __/~
~|___/  \__,_| |____/          |_|\_\ |_| |_| |_| |_|    \___|~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0mD
             \033[3;35mSub-Domain Brute FORCING tool
                 Dev: RichNet(N3TIX)
        Warning: This tool is for EDUCATIONAL intent\033[0m
"""





while True:
    try:
        clear_inter()
        print("\033[33m",logo+"\033[0m")
        print("\033[36m"+"[1] Scan Network Ports\n[2] IP Address Info\n[3] Phone-Number Info\n[4] url discovere\n[5] Sub-Domain Discovery\n[6] EXIT"+"\033[0m")
        prmt = input("[+] Select from the options above: ")
        if prmt == "1":
            clear_inter()
            ports_scan()
            break_validation()

        elif prmt == "2":
            clear_inter()
            ipinfo()
            break_validation()

        elif prmt == "3":
            clear_inter()
            phonenumber()
            break_validation()

        elif prmt == "4":
            clear_inter()
            urlscrapper() 
            break_validation()

        elif prmt == "5":
            clear_inter()
            print(sub_logo)
            if __name__=="__main__":
                url = input("[+] Input/Paste your URL: ")
                wordlist = "wordlist.txt"
                sub_domain(url,wordlist)
                break_validation()


        elif prmt == "6":
            exit()
 

    except KeyboardInterrupt:
        print("Programme Terminated")
        exit()
    except EOFError:
        print("programme Terminated")
