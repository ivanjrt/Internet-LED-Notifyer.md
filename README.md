# Goal of this: To create a device that will sense online Activitity from the Internet and Locally.

# Internet-LED-Sensor.md
requirements:
- Tea 🍵
- raspberry pi zero w, with its power adapter and cable
- 2x Resistors, 220 OHM
- 1x Green LED
- 1X Red LED
- Soldering Wire
- Soldering Iron
- Power Drill
- 3D Printer, or print online the model that goes accordingly: [https://www.thingiverse.com/thing:2407893](url) <br/>

# Flashing the Drive:
Download the RPI Manager: https://www.raspberrypi.com/software/ <br/>
* Settings (Change Accordingly): <br/>
![image](https://github.com/ivanjrt/Internet-LED-Sensor.md/assets/44326428/5e5be6d5-4b3b-43ad-a12d-f4fa7821d2e5) <br/>
![image](https://github.com/ivanjrt/Internet-LED-Sensor.md/assets/44326428/ec797201-99e4-40d4-bbde-f4d2c4dc570b) <br/>
![image](https://github.com/ivanjrt/Internet-LED-Sensor.md/assets/44326428/6bb9f723-d86e-4cc1-a1f3-f77ddd04236e) <br/>
![image](https://github.com/ivanjrt/Internet-LED-Sensor.md/assets/44326428/0f972ad8-c3f4-4fad-a941-69bfc623adab) <br/>
Save <br/>
![image](https://github.com/ivanjrt/Internet-LED-Sensor.md/assets/44326428/3ddbe8e5-2fad-4ffd-9c38-39f3254e2e2c) <br/>
Yes <br/>
![image](https://github.com/ivanjrt/Internet-LED-Sensor.md/assets/44326428/605324cd-14f3-4b2d-9356-ff803ec15a4a) <br/>
then Flash the Drive, this can take sometime, Then first boot will also take the longest. _Tea Refill._


# Once loaded the OS. SFTP, SSH and Python3 access should be Enabled, go in your router and you will see its IP address.
- Install the below,  this takes about 10 minutes for the first time, then from there it takes about 5.
```bash
sudo apt update
sudo apt install python3-gpiozero
sudo apt-get install python3-pip -y
sudo apt install python-gpiozero-doc -y
```

# Soldering
you want to 

