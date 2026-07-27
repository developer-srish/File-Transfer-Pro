# 📁 File Transfer Pro

<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&pause=1000&color=00C4FF&center=true&vCenter=true&width=900&lines=File+Transfer+Pro;Python+Socket+File+Transfer;Fast+%7C+Simple+%7C+Secure;Made+by+Srish+Ghosh">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python)
![Sockets](https://img.shields.io/badge/Python-Sockets-success?style=for-the-badge)
![Rich](https://img.shields.io/badge/Rich-Terminal%20UI-blueviolet?style=for-the-badge)
![PyFiglet](https://img.shields.io/badge/PyFiglet-ASCII%20Art-orange?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

<p align="center">
<img src="https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif" width="650">
</p>

---

# 📖 About

**File Transfer Pro** is a beginner-friendly Python project that allows users to transfer files between two computers using **TCP sockets**.

The project consists of a **Server** and a **Client**. The server sends any selected file while the client receives it and automatically saves it on the local computer.

The application also includes a beautiful command-line interface using **Rich** and **PyFiglet**, making the terminal more interactive and user-friendly.

This project is ideal for learning:

- Python Networking
- TCP Socket Programming
- Client-Server Architecture
- File Handling
- Binary Data Transfer
- Rich Terminal UI
- PyFiglet ASCII Art
- Python Projects

---

# ✨ Features

✅ Fast File Transfer

✅ TCP Socket Communication

✅ Simple Client-Server Architecture

✅ Automatic File Saving

✅ Rich Progress Animation

✅ Beautiful Terminal Interface

✅ Colorful Console Output

✅ Lightweight

✅ Cross Platform

✅ Beginner Friendly

✅ Easy to Understand Code

---

# 📂 Project Structure

```text
File_Transfer_Pro/
│
├── server.py
├── client.py
├── requirements.txt
├── Dockerfile
├── README.md
└── LICENSE
```

---

# 📋 Requirements

- Python 3.12+
- pip
- Git
- Windows or Linux
- Internet or Local Network Connection

---

# 📥 Install Git

## Windows

Download Git

https://git-scm.com/download/win

Verify installation

```bash
git --version
```

---

## Ubuntu / Debian

```bash
sudo apt update
sudo apt install git
```

---

## Fedora

```bash
sudo dnf install git
```

---

## Arch Linux

```bash
sudo pacman -S git
```

---

## macOS

```bash
brew install git
```

or

```bash
xcode-select --install
```

---

# 📥 Clone Repository

```bash
git clone https://github.com/developer-srish/File_Transfer_Pro.git
```

```bash
cd File_Transfer_Pro
```

---

# 📦 Install Dependencies

Using requirements.txt

```bash
pip install -r requirements.txt
```

or install manually

```bash
pip install rich pyfiglet
```

---
# ▶️ Running the Server

Start the server first.

```bash
python server.py
```

The server will display:

```text
Waiting for connection...
```

Next, enter:

- The file name you want to send.
- The file extension.
- The filename that will appear on the client's computer.

Example:

```text
Enter file Name with extension
example.pdf

Enter file extension
.pdf

Enter the name of the file that will appear in the client's computer
Study_Notes
```

The server is now waiting for a client connection.

---

# ▶️ Running the Client

Open another terminal (or another computer connected to the same network).

Run:

```bash
python client.py
```

The client will ask:

```text
IP:
```

Enter the server's IPv4 address.

Example:

```text
192.168.1.25
```

If the connection is successful, the file transfer will begin automatically.

---

# 🌐 Finding Your IP Address

## Windows

Open **Command Prompt** and run:

```cmd
ipconfig
```

Look for:

```text
IPv4 Address
```

Example:

```text
192.168.1.25
```

---

## Ubuntu / Debian

```bash
hostname -I
```

or

```bash
ip addr
```

---

## Fedora

```bash
hostname -I
```

---

## Arch Linux

```bash
hostname -I
```

---

## macOS

```bash
ipconfig getifaddr en0
```

or

```bash
ifconfig
```

---

# 📁 How to Transfer Files

1. Start the server.
2. Select the file to send.
3. Enter the desired filename for the client.
4. Start the client.
5. Enter the server's IP address.
6. Wait for the transfer to complete.
7. The received file will automatically be saved.

---

# 📤 Example

## Server

```text
Waiting for connection...

Connection from ('192.168.1.15', 54321)

Enter file Name with extension
notes.pdf

Enter file extension
.pdf

Enter the name of the file that will appear in the client's computer
Study_Notes

Trying to send file...

Successfully Transfered File
```

---

## Client

```text
IP:
192.168.1.25

Trying to get the file...

Successfully Received File
```

---

# 📂 Output

After the transfer finishes, the client folder will contain:

```text
Study_Notes.pdf
```

---

# ⚙️ How It Works

1. The server starts a TCP socket.
2. It listens on **Port 5050**.
3. The client connects using the server's IP address.
4. The server sends the filename.
5. The server sends the file extension.
6. The server opens the selected file in binary mode.
7. The file is transmitted in **1024-byte chunks**.
8. The client receives each chunk.
9. The client writes the data into a new file.
10. After transmission is complete, the file is automatically saved.

---

# 🔄 File Transfer Flow

```text
              SERVER
                 │
                 │
          Select a File
                 │
                 ▼
        Read Binary Data
                 │
                 ▼
      TCP Socket (Port 5050)
                 │
                 ▼
             CLIENT
                 │
                 ▼
        Receive File Data
                 │
                 ▼
      Save File Automatically
```

---

# 📦 Supported File Types

File Transfer Pro can transfer almost any file type, including:

- 📄 TXT
- 📑 PDF
- 🖼️ PNG
- 🖼️ JPG
- 🎵 MP3
- 🎬 MP4
- 📦 ZIP
- 📄 DOCX
- 📊 XLSX
- 📽️ PPTX
- 🐍 PY
- 📁 CSV
- 📦 RAR
- 📦 7Z
- And many more...

---

# 🐳 Docker Guide

## Prerequisites

- Docker Desktop installed
- Windows 10/11
- Administrator Command Prompt
- Internet Connection

---

# 1. Enable Windows Features

Open **Command Prompt as Administrator** and run:

```cmd
dism.exe /Online /Enable-Feature /FeatureName:Microsoft-Windows-Subsystem-Linux /All /NoRestart
```

Then enable the Virtual Machine Platform:

```cmd
dism.exe /Online /Enable-Feature /FeatureName:VirtualMachinePlatform /All /NoRestart
```

Restart your computer after both commands finish.

---

# 2. Update WSL

After restarting, open **Command Prompt as Administrator** and run:

```cmd
wsl --update
```

If an update is installed, restart your computer once more.

---

# 3. Start Docker Desktop

Launch **Docker Desktop**.

Wait until it displays:

```text
Engine running
```

Verify Docker is working correctly:

```cmd
docker --version
docker info
```

---

# 4. Open the Project Folder

```cmd
cd "C:\Path\To\File_Transfer_Pro"
```

Example:

```cmd
cd "C:\Users\Hp\Desktop\File_Transfer_Pro"
```

---

# 5. Build the Docker Image

```cmd
docker build -t file-transfer-pro .
```

This creates the Docker image:

```text
file-transfer-pro
```

---

# 6. Run the Server Container

```cmd
docker run --rm -it ^
-p 5050:5050 ^
-v "%cd%:/app" ^
file-transfer-pro
```

The server will start and wait for incoming client connections.

---

# 7. Run the Client Container

Open another terminal and run:

```cmd
docker run --rm -it ^
-v "%cd%:/app" ^
file-transfer-pro python client.py
```

If the server is running on your Windows host, enter:

```text
host.docker.internal
```

when prompted for the IP address.

On Linux, enter your host machine's local IP address.

---

# 🐳 Useful Docker Commands

## Show running containers

```cmd
docker ps
```

---

## Show all containers

```cmd
docker ps -a
```

---

## Show Docker images

```cmd
docker images
```

---

## Stop a running container

```cmd
docker stop <container_id>
```

---

## Remove a container

```cmd
docker rm <container_id>
```

---

## Remove the Docker image

```cmd
docker rmi file-transfer-pro
```

---

## Rebuild the Docker image

```cmd
docker build --no-cache -t file-transfer-pro .
```

---

# 📝 Docker Notes

- `--rm` automatically removes the container after it exits.
- `-it` enables interactive terminal input.
- `-p 5050:5050` maps port **5050** from the container to your computer.
- Restart Docker Desktop if `docker info` reports that the engine is not running.
- Always run `wsl --update` if Docker reports WSL-related errors.
- If Docker Desktop fails to start, verify that both **Windows Subsystem for Linux** and **Virtual Machine Platform** are enabled.

  # 🛠️ Technologies Used

- 🐍 Python
- 🌐 Socket Programming
- 📡 TCP/IP Networking
- 📁 File Handling
- 🎨 Rich
- 🎭 PyFiglet
- 💻 Command Line Interface (CLI)

---

# 📚 What You'll Learn

By building this project, you'll learn:

- Python Socket Programming
- TCP Client-Server Communication
- Networking Fundamentals
- File Handling in Python
- Binary File Transfer
- Exception Handling
- Command Line Applications
- Rich Terminal UI
- Real-World Python Projects

---

# ⚠️ Troubleshooting

## Connection Refused

If you receive:

```text
ConnectionRefusedError
```

Make sure:

- The server is running.
- You entered the correct IP address.
- Both devices are connected to the same network.
- Port **5050** is not blocked by a firewall.

---

## Address Already in Use

If you receive:

```text
OSError: [Errno 98] Address already in use
```

The port is already occupied.

Either:

- Close the previous server.
- Change the port number in both **server.py** and **client.py**.

---

## Module Not Found

If you receive:

```text
ModuleNotFoundError
```

Install the missing packages.

```bash
pip install rich pyfiglet
```

or

```bash
pip install -r requirements.txt
```

---

## File Not Found

If you receive:

```text
FileNotFoundError
```

Make sure:

- The file exists.
- The filename is correct.
- The file is inside the project folder.

---

## Connection Timed Out

Check:

- Internet/LAN connection.
- Correct server IP.
- Firewall settings.
- Antivirus restrictions.

---

# 🔒 Limitations

Current version supports:

- One client at a time.
- One file transfer per connection.
- No encryption.
- No authentication.
- Manual IP entry.

Future versions may include:

- Multiple clients
- Encryption
- Authentication
- Drag-and-drop support
- Progress bars for file transfers
- Resume interrupted transfers

---

# 🤝 Contributing

Contributions are always welcome!

1. Fork the repository.

```bash
git fork
```

2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added a new feature"
```

4. Push the branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📜 License

This project is licensed under the **MIT License**.

You are free to:

- ✅ Use
- ✅ Modify
- ✅ Share
- ✅ Learn from the source code

---

# 👨‍💻 Author

<p align="center">

## **Srish Ghosh**

Python Developer • Open Source Enthusiast • Student

GitHub

**https://github.com/developer-srish**

</p>

---

# 🚀 Future Improvements

Planned features include:

- 📊 File transfer progress bar
- 🔒 End-to-end encryption
- 👥 Multiple client support
- 📂 Folder transfer
- ⏯️ Pause and Resume transfers
- 🖥️ Graphical User Interface (GUI)
- 🌍 Internet-based file sharing
- 📱 Mobile client
- ⚡ Faster transfer protocol
- 🔑 Password-protected transfers

---

# 💖 Support the Project

If this project helped you:

⭐ Star the repository

🍴 Fork the repository

🐛 Report bugs

💡 Suggest new features

📢 Share it with others

Every contribution and star helps the project grow!

---

<p align="center">

# ⭐ Don't Forget to Star this Repository!

If you enjoyed this project or found it useful, please consider giving it a ⭐ on GitHub.

It motivates future development and helps more people discover the project.

<img src="https://media.giphy.com/media/QBd2kLB5qDmysEXre9/giphy.gif" width="320">

## Made with ❤️ in Python by **Srish Ghosh**

### Happy Coding! 🚀

</p>
