import time
import subprocess
import os
from gpiozero import LED
from datetime import datetime, timedelta

green = LED(27)
red   = LED(17)

def ping_host(host):
    try:
        output = subprocess.run(["ping", "-c", "1", "-W", "1", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.returncode == 0
    except Exception as e:
        return False

def write_to_file(message):
    with open("zerocitadelmon.txt", "a") as file:
        file.write(message + "\n")

def refresh_log_file_if_needed():
    log_file = "zerocitadelmon.txt"
    if os.path.exists(log_file):
        file_creation_time = datetime.fromtimestamp(os.path.getctime(log_file))
        if datetime.now() - file_creation_time > timedelta(days=5):
            os.remove(log_file)
            open(log_file, 'w').close()
    else:
        open(log_file, 'w').close() 


def check_servers():
    external_server = "www.google.com" # Change this Accordingly
    internal_server = "192.168.1.1" # Change this Accordingly
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
                message = "Internet and Router is UP " + dt_string
                write_to_file(message)
                #print(message)
            elif not ddnsExternal and internalGW:
                green.off()
                red.off()
                red.blink()
                green.blink()
                message = "Internet is DOWN though the Router is UP " + dt_string
                write_to_file(message)
                #print(message)
            elif not internalGW:
                green.off()
                red.off()
                green.off()
                red.on()
                message = "Your Router is OUT check ASAP " + dt_string
                write_to_file(message)
                #print(message)
            elif not ddnsExternal and not internalGW:
                green.off()
                red.off()
                green.off()
                red.blink()
                message = "Your Router and Internet OUT check ASAP " + dt_string
                write_to_file(message)
                #print(message)

            time.sleep(45)

    except KeyboardInterrupt:
        print("Script stopped by user")

if __name__ == "__main__":
    check_servers()
