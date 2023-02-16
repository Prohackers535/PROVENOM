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
print("")
subprocess.call(Fore.BLUE + "apt-get install python3 -y" , shell=True)
subprocess.call("apt-get install figlet -y" , shell=True)
print("")

subprocess.call("pip3 install colorama" , shell=True)
print("")

subprocess.call("pip3 install lolcat" , shell=True)
print("")

print(Fore.YELLOW + "Install Metasploit and Apkmod Before Run This Tool")
print("")

meta = input(Fore.GREEN + "Do You Want To Install Metasploit Type (y) To Yes:--->> ")
print("")

if meta == "y" or "Y":
    subprocess.call("apt install wget curl -y" , shell=True)
    subprocess.call("cd $HOME;mkdir -p $PREFIX/etc/apt/sources.list.d" , shell=True)
    subprocess.call("cd;wget https://raw.githubusercontent.com/ivam3/termux-packages/gh-pages/ivam3-termux-packages.list -O $PREFIX/etc/apt/sources.list.d/ivam3-termux-packages.list" , shell=True)
    subprocess.call("apt update && apt upgrade -y" , shell=True)
    subprocess.call("cd;apt install metasploit-framework -y" , shell=True)
    print("")
    
apkmod = input(Fore.BLUE + "Do You Want To Install Apkmod Type (y) To Yes:--->> ")
print("")

if apkmod == "y" or "Y":
    subprocess.call("cd $HOME" , shell=True)
    subprocess.call("wget https://raw.githubusercontent.com/Hax4us/Apkmod/master/setup.sh" , shell=True)
    subprocess.call("bash setup.sh" , shell=True)
    print("")
    

print(Fore.YELLOW + "-*-*-*-*-*-*-*-*-*- PRO HACKERS -*-*-*-*-*-*-*-*-*-")
print(Fore.RED + "Coded By:- Abdul Fasith") 

print(Fore.GREEN + "☆ Github==> https://github.com/Prohackers535")
print("")








 
