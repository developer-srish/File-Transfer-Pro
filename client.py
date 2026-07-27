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
IP=input('IP: ')
s.connect((IP,5050))
print('[?] Trying to get the file',style='bright_yellow')
fn=s.recv(1024).decode()
file_n=s.recv(1024).decode()

with open(fn+file_n,'wb') as f:
    while True:
        data=s.recv(1024)
        if not data:
            break
        f.write(data)
        
print('[-] Successfully Received File',style='bright_green')