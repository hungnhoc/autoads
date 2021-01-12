import requests
import os,sys
from time import sleep
from colorama import Fore, Back, Style
from colorama import init, AnsiToWin32
init(wrap=False)
from bs4 import BeautifulSoup
os.system("clear")
print (Fore.YELLOW+ "\t\t____  ____    _____  ____  ____ _    ")
print ("\t\t/   _\/  __\  /__ __\/  _ \/  _ \/ \   ")
print (Fore.BLUE+"\t\t|  /  | | //    / \  | / \|| / \|| |  ") 
print ("\t\t|  \__| |_\\    | |  | \_/|| \_/|| |_/\ ")
print (Fore.RED+"\t\t\____/\____/    \_/  \____/\____/\____/")
print (Fore.WHITE+"\t\t Mình Code Lại Nha Không Phải Do Mình Viết Ạ ")
print (Fore.GREEN)
cookie=input("Nhập Cookie:")
while(True):
    url ='https://ads-social.online/kiemtien'
    id1={'g-recaptcha-response':'03AGdBq26QdTOKBJup0oHFkIQwqYKolTMFQTYiA_bBi80wQ5FXtDpeXjJWWcIBXDLSipPCZs8kgjyGaiPdePFYEAy6jBmJl6f4CtEgVRErFuA5m3IDCykZogX9dzRaEQVqWcVJdWQsnCApHhE1oG5aJP0dzzMXtGpYj88BAZGMcVCrGQYmUXO7xid73fIx7EpkvHcSyxHHB22nhiGVpMngPh25T-PwoNRkYbMVXlkIhBkimahG1uivwHe0p6GBcGuQXdPxoN8TPcMeNU-l3iouRJ7GM--qZNRyKZPOHLxKBCbBJhTi_K2eFIoJVGYV33EehiKcalfTNPlFUfm_GmZA6sygwMH0A2CqQWnuZUyQjhKKp5CTvfzCP0zBkZW6NPNYyzlgu6InGZfGzW4-j8OkXqzTzFQKJ2C6HVHJzIQCV6kjypxoTXebNjPQIN_HekWZbqdvnkN41MxbHGPXPO3giCxAD8WsQMpwI2nvMBpFkZkxXO50iBSnzPvkBeMZiNVCIzk4ekPUgwvWd6edIP3ea5FaRaH7X3Y10Q'}
    header={'Cookie':cookie}
    web=requests.post(url,headers=header,data=id1)
    sop = BeautifulSoup(web.text,'html.parser')
    a = sop.find_all("button", id = True)
    for i in a:
        link = i["id"]
        id={'token':link}
        web1=requests.post('https://ads-social.online/nhantien.php',headers=header,data=id)
        status=web1.json()['message']
        print (Fore.GREEN+"|================================|")
        print (Fore.GREEN+"|",Fore.RED+status,Fore.GREEN+"|")
        print (Fore.GREEN+"|================================|")
        sleep(1)