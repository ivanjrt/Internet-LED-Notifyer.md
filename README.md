# Internet-LED-Sensor.md
MicroCenter:
* https://www.microcenter.com/product/486575/raspberry-pi-zero-w-microcontroller-development-board 15.99
* https://www.microcenter.com/product/603754/inland-pi-kit-deluxe-parts-pack 19.99
* https://www.microcenter.com/product/454325/adafruit-industries-half-size-breadboard 4.99

setup Init: https://www.youtube.com/watch?v=tF85BpXs5nA&t=1s
Ref https://www.youtube.com/watch?v=iL_oZGHLHvU



# Once loaded the OS. SFTP and SSH access should be Enabled.
- this takes about 10 minutes for the first time, then from there it takes about 5.
```bash
sudo apt update
sudo apt install python3-gpiozero
sudo apt-get install python3-pip -y
sudo apt install python-gpiozero-doc -y
sudo apt install screenfetch btop -y
```

* Install screenfetch and add it at startup.
```
sudo apt install screenfetch -y
```

* To have it run at startup
```nano  ~/.bashrc```
add this line at the end of the file:
```
screenfetch
```
