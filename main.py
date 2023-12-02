import random
import string
import ctypes
from pystyle import Write, Colors, System
from colorama import Fore, Style
import datetime
import getpass
import time
import requests


red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
orange = Fore.RED + Fore.YELLOW
pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
reset = Fore.RESET
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
dark_green = Fore.GREEN + Style.BRIGHT

date = datetime.datetime.now()
date_now = date.strftime("%d/%m/%Y")
username = getpass.getuser()

def g(rolls):
	data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
	result = ""
	while rolls >= 1:
		c = random.choice(data)
		result = c + result
		rolls = rolls - 1
	return result

ctypes.windll.kernel32.SetConsoleTitleW(f'! ALEX TOOL - Made By tbs.eu_alex  - Date : {date_now} - Logged As : {username}')
Write.Print(f"""
\t       ███       ██         █████████ ██    █████████████████████ ██████ ██
\t       ███       ██         █████████ ██    ██    ██       ██   █ █    █ ██
\t     ██   ██▓    ██         ██          ████      ██       ██   █ █    █ ██
\t     ██   ██▓▒   ██         ███ ██  █   ████      ██       ██   █ █    █ ██
\t   ███████████  ▓██         ██ █  ██    ██  ██    ██       ██   █ █    █ ██
\t   ████▓██████  ▓██         ██          ██  ██    ██       ██   █ █    ████
\t ██   ▓▓      ██▓██████████▓█████████ ██      ██  ██       ██   █ █    █ ██
\t ██   ▒▓      ██▓██████████▓▓████████▓██      ██  ██       ██████ ██████ █████████
\t ▓▓   ▒▒        ▒           ▓▒▒      ▓▓▓      ▓▓  ▓▓        ▓▓▓     ▓▓▓  ▒▒▓▓▓
\t ▒▓  ░░░        ░          ▒ ▒       ▒▓▒      ▓▓  ▓▓         ▓▓    ▓▒▓     ▒▓▒▓
\t ▒▒░                       ░ ░       ▒▒       ▒▓  ▓▒        ▓▒▒    ▒▒     ▒▒▒
\t ░░                                  ░░       ▒▒  ▒         ▒▒▒     ▒     ▒
\t                                                ▒           ░░░     ░     ░
                 """, Colors.red_to_blue, interval=0.0000)
Write.Print(f"""

                                                Welcome {username} 

════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                \t(1) Account Generator\t\t(8) Amazon Generator
                \t(2) Nitro Checker\t\t(9) Netflix Generator
                \t(3) Discord Generator\t\t(10) EBay Generator
                \t(4) Minecraft Generator\t\t(11) Roblox Generator
                \t(5) Just Eat Generator\t\t(12) Spotify Generator
                \t(6) Steam Generator\t\t(13) Playstore Generator
                \t(7) Glovo Generator\t\t(14) Minecraft Accounts [PAID VERSION REQUIRED]

""", Colors.red_to_blue, interval=0.0100)
Write.Print(f"""═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════""", Colors.red_to_blue, interval=0.0100)
Write.Print(f"\ncmdprompt@alexmultitool ~> ", Colors.red_to_blue, interval=0.010); opc = input(magenta).lower()

if opc == "1":
    Write.Print(f"""
        \t(1) Gmail Account             \t\t\t(2) Libero Account
                        \t\t(3) Virgilio Account
    """, Colors.red_to_blue, interval=0.010) 
    Write.Print(f"\ncmdprompt@accountgenerator ~> ", Colors.red_to_purple, interval=0.010); opn = input(blue).lower()
    if opn == "1":
        Write.Print(f"cmdprompt@howmanytogenerate ~> ", Colors.red_to_blue, interval=0.010); op = input(magenta).lower()
        print("")
        opo = int(op)
        for x in range(opo):
              Write.Print(f"cmdprompt@results ~> Account: {g(12)}@gmail.com | Password: {g(8)}\n", Colors.red_to_blue, interval=0.0000)
        Write.Print("cmdpromp@sleeptime ~> Sleeping for 150 seconds", Colors.red_to_purple, interval=0.010)
        time.sleep(150)
    elif opn == "2":
        Write.Print(f"cmdprompt@howmanytogenerate ~> ", Colors.red_to_blue, interval=0.010); op = input(magenta).lower()
        print("")
        opo = int(op)
        for x in range(opo):
              Write.Print(f"cmdprompt@results ~> Account: {g(12)}@libero.it | Password: {g(8)}\n", Colors.red_to_blue, interval=0.0000)
        Write.Print("cmdpromp@sleeptime ~> Sleeping for 150 seconds", Colors.red_to_purple, interval=0.010)
        time.sleep(150)
    elif opn == "3":
        Write.Print(f"cmdprompt@howmanytogenerate ~> ", Colors.red_to_blue, interval=0.010); op = input(magenta).lower()
        print("")
        opo = int(op)
        for x in range(opo):
              Write.Print(f"cmdprompt@results ~> Account: {g(12)}@virgilio.it | Password: {g(8)}\n", Colors.red_to_blue, interval=0.0000)
        Write.Print("cmdpromp@sleeptime ~> Sleeping for 150 seconds", Colors.red_to_purple, interval=0.010)
        time.sleep(150)

if opc == "2":
        Write.Print(f"cmdprompt@howmanytogenerate ~> ", Colors.red_to_blue, interval=0.010); op = input(magenta).lower()
        print("")
        opc = int(op)
        for x in range(opc):
                code = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM') for _ in range(16))
                session = requests.Session()
                req = session.get(
                        f"https://discordapp.com/api/entitlements/gift-codes/{code}",
                        timeout = 1000,
                ).status_code
                if req == 200:
                        Write.Print(f"cmdprompt@results ~> Code: https://discord.gift/{code}\n", Colors.green, interval=0.000)
                else:
                        Write.Print(f"cmdprompt@results ~> Code: https://discord.gift/{code}\n", Colors.red_to_purple, interval=0.000)
        Write.Print("cmdpromp@sleeptime ~> Sleeping for 150 seconds", Colors.red_to_purple, interval=0.010)
        time.sleep(150)

if opc == "3":
        Write.Print(f"cmdprompt@howmanytogenerate ~> ", Colors.red_to_blue, interval=0.010); op = input(magenta).lower()
        print("")
        opc = int(op)
        for x in range(opc):
                code = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM') for _ in range(16))
                Write.Print(f"cmdprompt@results ~> Code: https://discord.gift/{code}\n", Colors.red_to_purple, interval=0.000)
        Write.Print("cmdpromp@sleeptime ~> Sleeping for 150 seconds", Colors.red_to_purple, interval=0.010)
        time.sleep(150)

if opc == "4":
        Write.Print(f"cmdprompt@howmanytogenerate ~> ", Colors.red_to_blue, interval=0.010); op = input(magenta).lower()
        print("")
        opc = int(op)
        for x in range(opc):
                code = "" + g(4).upper() + "-" + g(4).upper() + "-" + g(4).upper() + "-" + g(4).upper() + "-" + g(4).upper()
                Write.Print(f"cmdprompt@results ~> Code: {code}\n", Colors.red_to_purple, interval=0.000)
        Write.Print("cmdpromp@sleeptime ~> Sleeping for 150 seconds", Colors.red_to_purple, interval=0.010)
        time.sleep(150)

if opc == "5":
        Write.Print(f"cmdprompt@howmanytogenerate ~> ", Colors.red_to_blue, interval=0.010); op = input(magenta).lower()
        print("")
        opc = int(op)
        for x in range(opc):
                code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
                Write.Print(f"cmdprompt@results ~> Code: {code}\n", Colors.red_to_purple, interval=0.000)
        Write.Print("cmdpromp@sleeptime ~> Sleeping for 150 seconds", Colors.red_to_purple, interval=0.010)
        time.sleep(150)

if opc == "6":
        Write.Print(f"cmdprompt@howmanytogenerate ~> ", Colors.red_to_blue, interval=0.010); op = input(magenta).lower()
        print("")
        opc = int(op)
        for x in range(opc):
                code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
                Write.Print(f"cmdprompt@results ~> Code: {code}\n", Colors.red_to_purple, interval=0.000)
        Write.Print("cmdpromp@sleeptime ~> Sleeping for 150 seconds", Colors.red_to_purple, interval=0.010)
        time.sleep(150)

if opc == "7":
        Write.Print(f"cmdprompt@howmanytogenerate ~> ", Colors.red_to_blue, interval=0.010); op = input(magenta).lower()
        print("")
        opc = int(op)
        for x in range(opc):
                code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
                Write.Print(f"cmdprompt@results ~> Code: {code}\n", Colors.red_to_purple, interval=0.000)
        Write.Print("cmdpromp@sleeptime ~> Sleeping for 150 seconds", Colors.red_to_purple, interval=0.010)
        time.sleep(150)

#amazon
if opc == "8":
        Write.Print(f"cmdprompt@howmanytogenerate ~> ", Colors.red_to_blue, interval=0.010); op = input(magenta).lower()
        print("")
        opc = int(op)
        for x in range(opc):
                code = ''.join(random.choice('0123456789') for _ in range(16))
                Write.Print(f"cmdprompt@results ~> Code: {code}\n", Colors.red_to_purple, interval=0.000)
        Write.Print("cmdpromp@sleeptime ~> Sleeping for 150 seconds", Colors.red_to_purple, interval=0.010)
        time.sleep(150)

#netflix
if opc == "9":
        Write.Print(f"cmdprompt@howmanytogenerate ~> ", Colors.red_to_blue, interval=0.010); op = input(magenta).lower()
        print("")
        opc = int(op)
        for x in range(opc):
                code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(11))
                Write.Print(f"cmdprompt@results ~> Code: {code}\n", Colors.red_to_purple, interval=0.000)
        Write.Print("cmdpromp@sleeptime ~> Sleeping for 150 seconds", Colors.red_to_purple, interval=0.010)
        time.sleep(150)

#ebay
if opc == "10":
        Write.Print(f"cmdprompt@howmanytogenerate ~> ", Colors.red_to_blue, interval=0.010); op = input(magenta).lower()
        print("")
        opc = int(op)
        for x in range(opc):
                code = ''.join(random.choice(string.digits) for _ in range(13))
                Write.Print(f"cmdprompt@results ~> Code: {code}\n", Colors.red_to_purple, interval=0.000)
        Write.Print("cmdpromp@sleeptime ~> Sleeping for 150 seconds", Colors.red_to_purple, interval=0.010)
        time.sleep(150)
#roblox
if opc == "11":
        Write.Print(f"cmdprompt@howmanytogenerate ~> ", Colors.red_to_blue, interval=0.010); op = input(magenta).lower()
        print("")
        opc = int(op)
        for x in range(opc):
                code = g(4)+"-"+g(4)+"-"+g(4)+"-"+g(4)
                Write.Print(f"cmdprompt@results ~> Code: {code}\n", Colors.red_to_purple, interval=0.000)
        Write.Print("cmdpromp@sleeptime ~> Sleeping for 150 seconds", Colors.red_to_purple, interval=0.010)
        time.sleep(150)
#spotify
if opc == "12":
        Write.Print(f"cmdprompt@howmanytogenerate ~> ", Colors.red_to_blue, interval=0.010); op = input(magenta).lower()
        print("")
        opc = int(op)
        for x in range(opc):
                code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
                formatted_code = '-'.join([code[i:i+4] for i in range(0, 16, 4)])
                Write.Print(f"cmdprompt@results ~> Code: {formatted_code}\n", Colors.red_to_purple, interval=0.000)
        Write.Print("cmdpromp@sleeptime ~> Sleeping for 150 seconds", Colors.red_to_purple, interval=0.010)
        time.sleep(150)
#playstore
if opc == "13":
        Write.Print(f"cmdprompt@howmanytogenerate ~> ", Colors.red_to_blue, interval=0.010); op = input(magenta).lower()
        print("")
        opc = int(op)
        for x in range(opc):
                code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(11))
                Write.Print(f"cmdprompt@results ~> Code: https://discord.gift/{code}\n", Colors.red_to_purple, interval=0.000)
        Write.Print("cmdpromp@sleeptime ~> Sleeping for 150 seconds", Colors.red_to_purple, interval=0.010)
        time.sleep(150)
#mc acc
if opc == "14":
        Write.Print(f"cmdprompt@error ~> This is a free version of ! ALEX MULTI-T00L.\nTo download the full src version contact in DM the owner (tbs.eu_alex)", Colors.red_to_blue, interval=0.010); op = input(magenta).lower()