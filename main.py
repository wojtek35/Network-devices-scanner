from scapy.all import *
import time
import os
import sys
from colorama import Fore
from colorama import Style
import report
import sniff
from configparser import ConfigParser
from win10toast import ToastNotifier


# pip3 install PyTelegramBotAPI==2.2.3


toast = ToastNotifier()
config = ConfigParser()
file = 'config\config.ini'
config.read(file)

    
def app():
    filename = 'config\ip_list.txt' # Load the file with lists of ip adresses
    results = {}
    os.system('cls')
    with open(filename) as file_object:
        for line in file_object:
            results[line.rstrip()]=''  # Create a dictionary of ip adresses we want to scan {'192.168.x.x': '', ...}

    scan_ips(results)


def scan_ips(results):
    new_results = {}
    old_results = {}
    older_results = {}

    counter = 0
    change = 2
    while True:
        time.sleep(int(config['Scanning interval (in seconds)']['time']))
        new_results = check_ip(results) # returns ip addresses which have been found
        os.system('cls')
        # if results have changed
        if new_results != old_results: 

            print('new_results != old_results')
            print_to_terminal(counter, new_results)     # Displays status to terminal
            print(f"Change: {change}")
            older_results.update(old_results)
            old_results.update(new_results)
            if change == 0:
                change = 1
            elif change == 1:
                change = 0
                counter = 0
            continue
        # if the results havent changed
        elif new_results == old_results:

            print('new_results == old_results')
            print_to_terminal(counter, new_results)     # Displays status to terminal
            print(f"Change: {change}")

            if counter > int(config['Counter']['count']):  # if the counter has reached a specified amout, send a device status change notification and reset counter
                counter = 0
                send_report(new_results, older_results)      # send email, telegram and windows notification
                change = 0
            if change == 1:
                counter += 1
            elif change == 2:
                change = 0

def check_ip(results): 
    for ip, status in results.items():
        result = sniff.sniff_ips(ip)
        if result != '':
            results[ip] = 'ONLINE'
        else:
            results[ip] = 'OFFLINE'
    return(results)

def send_report(new_results,old_results):
    old_set = set(old_results.items())
    new_set = set(new_results.items())

    data = new_set - old_set
    message =''
    for val in data:
        information = f"{val[0]} changed its status to {val[1]}"
        message += f"{information}\n"
    print(message)
    toast.show_toast("Status update", message, duration=5)
    report.send_email(message)
    report.send_telegram(message)


def print_to_terminal(counter, new_results):
    print(f"Counter: {counter}")
    for ip, status in new_results.items():
        if status == 'ONLINE':
            print(f"{ip} is {Fore.GREEN}{status}{Style.RESET_ALL}")
        elif status == 'OFFLINE':
            print(f"{ip} is {Fore.RED}{status} {Style.RESET_ALL}")


app()



 


