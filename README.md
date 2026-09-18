SysPulse Core - Network Diagnostic & Telemetry Suite

Hi guys! Welcome to my open-source githup proejct. This is a python script I made to help check network health, run pings, and do nmap scans easily. It automatically saves everything into a nice JSON report so you can look at it later or show it to your boss!

Features:

    Profile 1: Quick Ping & Latency diagnostics for fast checks.

    Profile 2: Advanced Port State & Service Verification (uses nmap to find open ports like 80, 443, 22).

    Profile 3: Comprehensive Route Trace and full port sweep with OS fingerprinting!

    Auto-Logging: Saves all results into a timestamped json file automatically.

How to Install & Run:
Make sure you have python3 and nmap installed on your Linux machine (it works great on Kali Linux or Ubuntu!).

    Clone the repository:
    git clone https://github.com/yourusername/syspulse.git
    cd syspulse

    Give execution permision to the script:
    chmod +x syspulse.py

    Run it (pleas run with sudo so nmap and raw sockets work properly!):
    sudo ./syspulse.py

How to Use:
When you run the script, it will ask you for a few things:

    Enter your target IP address, domain name, or CIDR range.

    Select your audit intensity level (choose between 1, 2, or 3).

    Watch it do its magic and generate the report file!

Requirements:

    Python 3.x

    Nmap installed (sudo apt install nmap)

    Linux terminal (tested on Kali linux)

Feel free to open an issue or pull request if you want to contribute or find any bugs!
