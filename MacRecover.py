import sys
import subprocess
print("""
 __  __            ____                                ____       
|  \/  | __ _  ___|  _ \ ___  ___ _____   _____ _ __  |  _ \ _   _
| |\/| |/ _` |/ __| |_) / _ \/ __/ _ \ \ / / _ \ '__| | |_) | | | |
| |  | | (_| | (__|  _ <  __/ (_| (_) \ V /  __/ |    |  __/| |_| |
|_|  |_|\__,_|\___|_| \_\___|\___\___/ \_/ \___|_|    |_|    \__, |
                                                              |___/ 
""")
print("This is a tool to help you recover your Mac.")
print("This project was made by github.com/RyanisyydsTT")
print("""
[MacOS installer downloader]
1. Big Sur (11.7.0)
2. Monterey (12.7.6)
3. Ventura (13.6.9)
4. Sonoma (14.6.1)
[We will upload more version to here after first release!]
Please select the version you want to download
""")
selection = input(">>> ")
if selection == 1:
    os = "MacOS Big Sur"
    print(f"Let me confirm, You are downloading {os}, and the file will be stored in the same directory as the python file, if confirmed, Please input Y/N")
    confirmed = input(">>> ")
    if confirmed == "Y" or "y":
        subprocess.run(['curl', ['-O'], 'https://swcdn.apple.com/content/downloads/14/38/042-45246-A_NLFOFLCJFZ/jk992zbv98sdzz3rgc7mrccjl3l22ruk1c/InstallAssistant.pkg'])
    else:
        print("Not confirmed, quitting")
        sys.exit()
elif selection == 2:
    os = "MacOS Monterey"
    print(f"Let me confirm, You are downloading {os}, and the file will be stored in the same directory as the python file, if confirmed, Please input Y/N")
    confirmed = input(">>> ")
    if confirmed == "Y" or "y":
        subprocess.run(['curl', ['-O'], 'https://swcdn.apple.com/content/downloads/34/21/062-40406-A_GZQ27OUQER/ggclib72ow1omcvfexvp84bc9x5ei5tyqu/InstallAssistant.pkg'])
    else:
        print("Not confirmed, quitting")
        sys.exit()
elif selection == 3:
    os = "MacOS Ventura"
    print(f"Let me confirm, You are downloading {os}, and the file will be stored in the same directory as the python file, if confirmed, Please input Y/N")
    confirmed = input(">>> ")
    if confirmed == "Y" or "y":
        subprocess.run(['curl', ['-O'], 'https://swcdn.apple.com/content/downloads/34/21/062-40406-A_GZQ27OUQER/ggclib72ow1omcvfexvp84bc9x5ei5tyqu/InstallAssistant.pkg'])
    else:
        print("Not confirmed, quitting")
        sys.exit()
elif selection == 4:
    os = "MacOS Sonoma"
    print(f"Let me confirm, You are downloading {os}, and the file will be stored in the same directory as the python file, if confirmed, Please input Y/N")
    confirmed = input(">>> ")
    if confirmed == "Y" or "y":
        subprocess.run(['curl', ['-O'], 'https://swcdn.apple.com/content/downloads/34/21/062-40406-A_GZQ27OUQER/ggclib72ow1omcvfexvp84bc9x5ei5tyqu/InstallAssistant.pkg'])
    else:
        print("Not confirmed, quitting")
        sys.exit()
else:
    print("Wrong input, please try again")
    sys.exit()

