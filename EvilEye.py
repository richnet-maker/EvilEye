import socket
import os
from _datetime import datetime
import requests
from phonenumbers import carrier, timezone, parse, is_valid_number



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
    print("""\033[40m
┌─────────────────────────────┐
│   P O R T  S C A N N E R    │
├─────────────────────────────┤
│  ▸ scanning…                │
│  ▸ checking open ports      │
└─────────────────────────────┘

\033[0m""")
    try:
        url = input("[+] Input URL/IP Address: ")
        host = socket.gethostbyname(url)
        print(f"[+] scanning open ports on  {url} IP: {host} ......\n[+] Scanning Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
        for port in range(20,1000):
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            conn = sock.connect_ex((host,port))
            sock.settimeout(0.2)
            if conn == 0:
                print("\n")
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
    print("            \033[1;33mipinfo by RchNet\033[0m\n")


    target_ip = input("[+] Input Your Target IP: ")
    reqst = requests.get(f"https://ipinfo.io/{target_ip}/json")
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


    






while True:
    try:
        clear_inter()
        print("\033[33m",logo+"\033[0m")
        print("\033[36m"+"[1] Scan Network Ports\n[2] IP Address Info\n[3] Phone-Number Info"+"\033[0m")
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

        else:
            print("[+] INVALID INPUT!!")

 

    except KeyboardInterrupt:
        print("Programme Terminated")
        exit()
    except EOFError:
        print("programme Terminated")



