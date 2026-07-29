import socket
import time
from pyfiglet import Figlet
from rich.console import Console
from rich.progress import Progress
import smtplib
from email.message import EmailMessage
import random as r
import json
from dotenv import load_dotenv
import os

load_dotenv()

se = os.getenv("EMAIL")
app = os.getenv("APP_PASSWORD")
console = Console()
def print(text, style="white", delay=0.05):
    for char in text:
        console.print(char, style=style, end="")
        time.sleep(delay)
    console.print()
with open('user.json', 'r') as f:
    dat=json.load(f)
if dat['Count'] == 0:
    print(f'Welcome {dat["Name"]} to File Tarnsfer pro',style='magenta')
    n=input('Enter your Name : ')
    ema=input('Enter Email id')
    
    
    su='Email Verification'
    co= r.randint(100000, 999999)
    msg=EmailMessage()
    msg.set_content(
    f"""Welcome to File Transfer Pro!

Your verification OTP is: {co}

Do not share this OTP with anyone.
"""
)
    msg['Subject'] =su
    msg['From'] =se
    msg['To'] =ema
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(se, app)
        server.send_message(msg)
    oo=input('Enter otp')
    if int(oo) == co :
        dat["Count"]=1
        dat["Name"] = n
        dat["Email"]=ema
        print(f'Welcome {dat["Name"]}',style='magenta')
        with open("user.json", "w") as f:
            json.dump(dat, f, indent=4)
    else:
        print("Wrong OTP!", style="red")
        exit()
else:
    print(f'Welcome {dat["Name"]} to File Tarnsfer pro',style='magenta')
    

fig = Figlet(font="starwars")
banner = fig.renderText("File Transfer Pro")

colors = [
    "red",
    "yellow",
    "green",
    "cyan",
    "blue",
    "magenta",
    "bright_red",
    "bright_green",
    "bright_blue",
]

for i, line in enumerate(banner.splitlines()):
    console.print(f"[bold {colors[i % len(colors)]}]{line}[/]")
with Progress() as progress:
    task = progress.add_task("[cyan]Loading...", total=100)

    while not progress.finished:
        time.sleep(0.05)
        progress.update(task, advance=1)

time.sleep(3)



s=socket.socket()
s.bind(('',5050))
s.listen(1)
print('[-]Waiting for connection',style='bright_green')
conn,addr=s.accept()
print(f'[-] Connection from {conn} and {addr}')
f_n=input('[-] Enter file Name with extension(It should be in this folder only) ')
f_e=input('[-] Enter file extension :')
fn=input('[-] Enter the name of the file that will appear in the client"s computer ')
conn.send(fn.encode())
conn.send(f_e.encode())
print('[?] Trying to send file',style='bright_yellow')
try:
    with open(f_n ,'rb') as f:
        # Getting the file data in bytes
        while True:
            data=f.read(1024)
            if not data:
                break
            conn.sendall(data)
    print('Successfully Transfered File',style='bright_green')
except Exception as e:
    print('[!] Error',style='bright_red')
    print(e)


