import socket
import time
import builtins
from pyfiglet import Figlet
from rich.console import Console
from rich.progress import Progress
console = Console()
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


def print(text, style="white", delay=0.05):
    for char in text:
        console.print(char, style=style, end="")
        time.sleep(delay)
    console.print()
s=socket.socket()
s.bind(('',5050))
s.listen(1)
print('[-]Waiting for connection',style='bright_green')
conn,addr=s.accept()
print(f'[-] Connection from {conn} and {addr}')
f_n=input('[-] Enter file Name with extension(It should be in this folder only) ')
f_e=input('[-] Enter file extension')
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


