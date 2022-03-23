import subprocess
import time
import colorama
from colorama import Fore

print ("")
print ("")

subprocess.call("figlet " + "PROVENOM" + " | lolcat", shell=True)

time.sleep(3) 

subprocess.call("clear", shell=True)
print(Fore.GREEN + "Coded By:- Abdul Fasith")

subprocess.call("figlet " + "PRO HACKERS" + " | lolcat", shell=True)

print(Fore.BLUE + "-*-*-*-*-*-*-*-*-*- PRO HACKERS -*-*-*-*-*-*-*-*-*-")
print("")
print(Fore.RED + " ☆ Github==> https://github.com/Prohackers535")

subprocess.call(Fore.BLUE + "apt install python3 figlet -y" , shell=True)
print("")

subprocess.call("pip3 install colorama" , shell=True)
print("")

subprocess.call("pip3 install lolcat" , shell=True)
print("")

print(Fore.YELLOW + "Install Metasploit and Apkmod Before Run This Tool")
print("")

meta = input(Fore.GREEN + "Do You Want To Install Metasploit Type (y) To Yes:--->> ")
print("")

if meta == "y":
    subprocess.call("apt install wget curl -y" , shell=True)
    subprocess.call("cd $HOME;wget https://raw.githubusercontent.com/efxtv/Metasploit-in-termux/main/metasploit-6-termux.sh" , shell=True)
    subprocess.call("bash metasploit-6-termux.sh" , shell=True)
    subprocess.call("rm -rf /data/data/com.termux/files/usr/bin/msfvenom" , shell=True)
    subprocess.call("cd;cd metasploit-framework;ln -s $HOME/metasploit-framework/msfvenom /data/data/com.termux/files/usr/bin/" , shell=True)
    print("")
    
apkmod = input(Fore.BLUE + "Do You Want To Install Apkmod Type (y) To Yes:--->> ")
print("")

if apkmod == "y":
    subprocess.call("cd $HOME" , shell=True)
    subprocess.call("wget https://raw.githubusercontent.com/Hax4us/Apkmod/master/setup.sh" , shell=True)
    subprocess.call("bash setup.sh" , shell=True)
    print("")
    

print(Fore.YELLOW + "-*-*-*-*-*-*-*-*-*- PRO HACKERS -*-*-*-*-*-*-*-*-*-")
print(Fore.RED + "Coded By:- Abdul Fasith") 

print(Fore.GREEN + "☆ Github==> https://github.com/Prohackers535")
print("")








 
