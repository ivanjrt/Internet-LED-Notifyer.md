# sudo systemctl stop  zerocitadelmon.service
'''
Manifest Functionality:
    Solid Green = Internet and DNSServer is UP
    Green + Red Blinking = Internet is DOWN though the DNSServer is UP
    Solid Red = Internet is UP though the DNSServer is DOWN
    Blinking Red = DNSServer and Internet are OUT check ASAP
'''

import time
import subprocess
import os
from gpiozero import LED
from datetime import datetime, timedelta
import csv


green = LED(27)
red   = LED(17)
time.sleep(10) # This to wait for the WiFi to fully Turn On and get an IP


def ping_host(host):
    try:
        output = subprocess.run(["ping", "-c", "1", "-W", "1", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.returncode == 0
    except Exception as e:
        return False

def write_to_csv(message, filename="zerocitadelmon.csv"):
    with open(filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(message)

def refresh_log_file_if_needed():
    log_file = "zerocitadelmon.csv"
    if os.path.exists(log_file):
        file_creation_time = datetime.fromtimestamp(os.path.getctime(log_file))
        if datetime.now() - file_creation_time > timedelta(days=5):
            os.remove(log_file)
            open(log_file, 'w').close()  # Create a new empty file
    else:
        open(log_file, 'w').close()  # Create a new empty file if it doesn't exist


def check_servers():
    #external_server = "10.10.10.12"
    external_server = "73.136.125.159" #"ddns.robotsandbox.net"
    internal_server = "pi.hole"
    ddnsExternal    = None
    internalGW      = None

    try:
        while True:
            refresh_log_file_if_needed()

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            external_ping = ping_host(external_server)
            internal_ping = ping_host(internal_server)

            #Checking for responses
            if external_ping:
                ddnsExternal = True
            else:
                ddnsExternal = False

            if internal_ping:
                internalGW = True
            else:
                internalGW = False

            # Decision Making
            if ddnsExternal and internalGW:
                green.off()
                red.off()
                green.on()
                message = ("Internet and DNSServer is UP " , dt_string)
                write_to_csv(message)
                #print(message)
            elif not ddnsExternal and internalGW:
                green.off()
                red.off()
                red.blink()
                green.blink()
                message = ("Internet is DOWN though the DNSServer is UP " , dt_string)
                write_to_csv(message)
                #print(message)
            elif not internalGW and ddnsExternal:
                green.off()
                red.off()
                green.off()
                red.on()
                message = ("Internet is UP though the DNSServer is DOWN " , dt_string)
                write_to_csv(message)
                #print(message)
            elif not ddnsExternal and not internalGW:
                green.off()
                red.off()
                green.off()
                red.blink()
                message = ("DNSServer and Internet are OUT check ASAP " , dt_string)
                write_to_csv(message)
                #print(message)

            time.sleep(45)

    except KeyboardInterrupt:
        print("Script stopped by user")

if __name__ == "__main__":
    check_servers()
