# Linux-LFI-Harvester
Linux System Information Harvesting through Local File Inclusion (LFI) Vulnerability 🐱

```shell
└──╼ $python3 LFIH.py -u http://bagel.htb:8000/?page=../../../../ -h

                      __      _
                    o'')}____//
                    `_/      )
                    (_(_/-(_/
    ██      ███████ ██ ██   ██ 
    ██      ██      ██ ██   ██ 
    ██      █████   ██ ███████ 
    ██      ██      ██ ██   ██ 
    ███████ ██      ██ ██   ██                        
                    
                    Yazidou                                                                   

usage: LFIH.py [-h] -u U [-t T] [-proc] [-net] [-cmdlines] [-etc] [-var] [-all] [-p P] [-x64]

[*] Simple script for information retrieving through Local File Inclusion.

optional arguments:
  -h, --help  show this help message and exit
  -u U        Target URL
  -t T        Threads
  -proc       Retrieving on /proc
  -net        Network status (Routes, TCP, UDP, ARP) from /proc/net
  -cmdlines   Retrieving of 1-MAX_PID cmdlines on /proc/{PIDs}/cmdlines (default MAX_PID for x32, use -x64 to increase)
  -etc        Retrieving on /etc
  -var        Retrieving on /var
  -all        Retrieving all of the above
  -p P        Pathern to skip for cmdlines (i.e. NotFounds strings)
  -x64        Targeting an x64 machine (x32 by default)

```
