import os
from colorama import *
from requests import get,session,request
import random

#checking os untuk clear
def check_clear():
    check = os.name
    if check == 'nt':
        os.system('cls')
    elif check == 'posix':
        os.system('clear')
    else:
        print('apakah os anda bermasalah???')

check_clear()
def mulai():
    print(Fore.LIGHTBLUE_EX,
    """
    
 _______  _______           _______  _______  ______   _______          
/ ___   )(  ____ \|\     /|(  ___  )(  ____ )(  __  \ (  ____ \|\     /|
\/   )  || (    \/| )   ( || (   ) || (    )|| (  \  )| (    \/| )   ( |
    /   )| (__    | | _ | || (___) || (____)|| |   ) || (__    | |   | |
   /   / |  __)   | |( )| ||  ___  ||     __)| |   | ||  __)   ( (   ) )
  /   /  | (      | || || || (   ) || (\ (   | |   ) || (       \ \_/ / 
 /   (_/\| (____/\| () () || )   ( || ) \ \__| (__/  )| (____/\  \   /  
(_______/(_______/(_______)|/     \||/   \__/(______/ (_______/   \_/   
                                                                        

                                                                            
    """,Style.RESET_ALL)
                                               
    print(Fore.GREEN,"""
            ---------------------------------------
                proxy scan
                versi : 1.0
            =====================================
                contact me : wa.me/+6282314509535
            ---------------------------------------
    """,Style.RESET_ALL,'\n')

    input_user = str(input('masukan nama file : '))

    def save_deadproxy(proxy):
        file = open("proxy_mati.txt","a")
        file.write(f"{proxy}  ")
        file.write("\n")
        file.close()

    def save_live_proxy(proxy):
        with open("proxy_idup.txt","a") as file:
            return file.write(f"{proxy}\n") 

    def proxy():
        with open(input_user,'r') as file:
            line = file.readlines()
            proxy = random.randint(0,len(line)-1)
            test_proxy = line[proxy]
            proxies={'http': f'http://{test_proxy}'}
            try:
                sess = session()
                response = sess.get('http://icanhazip.com',headers={'User-Agent': 'Bla'}, proxies=proxies,timeout=5)
                jsonize = response.text
                if response.status_code == 200:
                    print(Fore.GREEN,f"PROXY YANG ON ==> {test_proxy}",Style.RESET_ALL)
                    save_live_proxy(test_proxy)
                else:
                    print(Fore.GREEN,f"PROXY YANG ON ==> {test_proxy}",Style.RESET_ALL)
                    save_live_proxy(test_proxy)
            except:
                print(Fore.RED,f"PROXY YANG MATI -> {test_proxy}",Style.RESET_ALL)
                save_deadproxy(proxies)

    def main():
        with open(input_user,'r') as file:
            line = file.readlines()
            for x in range(0,len(line)):
                proxy()

    if __name__ == "__main__":
        main()
        
if __name__ == "__main__":
    password = str(input("masukan password : "))
    if password == "ZewarDev1337":
        check_clear()
        mulai()
    else:
        print('password salah kontol')