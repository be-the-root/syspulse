```markdown
# DarkHell Recon

A Python-based automated terminal framework for network reconnaissance, web enumeration, and security auditing.

## Description

DarkHell is designed to streamline security auditing by organizing common command-line enumeration tools—such as Nmap, SQLMap, Gobuster, Nikto, and SSLScan—into a structured interactive menu and command-line automation framework. Built for security lab environments and authorized penetration testing workflows, it wraps complex syntax into modular execution commands to automate multi-stage scanning, port discovery, and application fingerprinting.

### Screenshots

![DarkHell Terminal Scan](image_agent_tag_7325621398111242582)

## Getting Started

### Dependencies

* Linux distribution (tested on Kali Linux, Debian, or Ubuntu)
* Python 3.8 or higher
* Installed CLI security utilities: `nmap`, `sqlmap`, `gobuster`, `nikto`, `sslscan`

### Installing

* Clone the repository to your local machine:
  ```bash
  git clone [https://github.com/be-the-root/darkhell.git](https://github.com/be-the-root/darkhell.git)

```

* Navigate into the project directory:
```bash
cd syspulse

```


* Grant execution permissions to the script:
```bash
chmod +x syspulse.py

```



### Executing program

* Launch the script with root privileges (required for raw sockets and privileged Nmap scans):
```bash
sudo python3 syspulse.py

```


* Enter your target IP address, domain name, or CIDR range when prompted.
* Select your audit module or intensity level from the interactive menu.
* Monitor the progress in real time as report outputs are generated.

## Help

Ensure `nmap` and required tools are installed on your PATH if the script throws execution errors:

```bash
sudo apt update && sudo apt install nmap sqlmap gobuster nikto sslscan -y

```



## License

This project is made by me
