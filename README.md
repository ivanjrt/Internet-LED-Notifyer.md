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


# Once loaded the OS. SFTP, SSH and Python3 access should be Enabled, go in your router and you will see its IP address.  <br/>
- Install the below,  this takes about 10 minutes for the first time, then from there it takes about 5. <br/>
```bash
sudo apt update
sudo apt install python3-gpiozero
sudo apt-get install python3-pip -y
sudo apt install python-gpiozero-doc -y
```

# Soldering
From what I used two GPIO `17` & `27`, plust two Grounds. (See below): <br/>
![image](https://github.com/ivanjrt/Internet-LED-Sensor.md/assets/44326428/7be1066a-0efe-44da-abf9-d2c86cd07c0a) <br/>
This is a Diaggram on how this needs to be sordered: <br/>
![image](https://github.com/ivanjrt/Internet-LED-Sensor.md/assets/44326428/b12d7cb5-e7d1-4883-9fb1-56256db360a4) <br/>
https://gpiozero.readthedocs.io/en/latest/recipes.html#led-with-variable-brightness  <br/>

# Triggering point.
Make sure you have `pip` Installed otherwise:   <br/>
```bash
sudo apt-get install python3-pip
```
In this same repo, I'm sharing the python file, where you need to make changes to your Internal and External host to ping acccoringly.  <br/>
`nano main.py` , `CTRL + X`  ,  to save the file  <br/>
Add the context, then run the file with this.  <br/>
```python3 main.py```  <br/>

# Et Voila! Final Produt.
![image](https://github.com/ivanjrt/Internet-LED-Sensor.md/assets/44326428/363f0e74-7d56-4a4f-ae96-8383e0d529eb)  <br/>




