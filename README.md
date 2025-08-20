# REGOČ | EUWRO-Slovenia
## TABLE OF CONTENT

| Section  | Explanation |
| --  | -- | 
| [PROBLEM](#problem)  | Adressing the task of the competition. |
| [ENGINEERING MATERIALS](#engineering-materials)  | The list of everything we used. |
| [MOBILITY MANAGMENT](#mobility-managment)  | [Driving](#driving),  [steering](#steering)| 
| [POWER AND SENSE MANAGMENT](#power-and-sense-managment)  |  [Power supply](#power-supply),[sensorics](#sensorics)  |
| [PICUTRES](#pictures)  |  [Team pictures](#team-pictures), [vehicle pictures](#vehicle-pictures)  |
| [ASSEMBLY INSTRUCIONS ](#assembly-instructions)  |  [Hardware](#hardware), [software](#software)  | 



# PROBLEM
The goal of the Future Engineers WRO category is to design a fully autonomous vehicle that completes two different challenges in 3 minutes. The direction of the vehicles movement, interior walls position and their size in both challenges is randomized before the start of the round, so the vehicle should recognize whether to turn left or right by itself. 
This is our playfield:
<br><br>
    
<img width="1316" height="764" alt="image" src="https://github.com/user-attachments/assets/6487d5d0-3245-413a-9d87-16ab59b773b3" />

<br><br>
### OPEN CHALLENGE
In the open challenge, once the robot starts, its goal is to complete 3 laps around the map while avoiding the walls and finish in the same zone it started in.


### OBSTACLE CHALLENGE 
In the obstacle challenge, once the robot starts, its goal is again to complete 3 laps but now other than avoiding walls it has to avoid red and green pillars which are in the way. Depending on the color 
it passes the pillars either from the left or the right. Once the 3 laps are complete and robot is back in its starting area it should parallely park in the previously set
parking spot. The parking spot is 1.5x the lenght of the vehicle. The vehicle may also start from the parking spot. 

# ENGINEERING MATERIALS
- Servo SG90
<img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/297e06de-a4c1-44d1-a43a-930222bc18a4" />

- Yellow TT Gear Motor
- <img width="120" height="120" alt="image" src="https://github.com/user-attachments/assets/0f006b9b-f0c9-4bdb-be62-2b6088ba5296" />

- HC - SRO4 ultrazvučni senzor (x6)
- <img width="120" height="120" alt="image" src="https://github.com/user-attachments/assets/12170dc7-47c8-42e2-a1d5-d2da560281ac" />

- Raspberry Pi Camera v2
- <img width="120" height="120" alt="image" src="https://github.com/user-attachments/assets/9018aa25-35b8-4681-9f61-39e590815c28" />

- DHT22
  <img width="120" height="120" alt="image" src="https://github.com/user-attachments/assets/e7c28bec-eb27-4171-b5b0-017d9478bc55" />

- Arduino Uno
- <img width="225" height="225" alt="image" src="https://github.com/user-attachments/assets/07404523-dd7a-4f33-982c-68c886350989" />

- Raspbbery Pi 4
- <img width="225" height="225" alt="image" src="https://github.com/user-attachments/assets/33665a85-cf07-4388-9a5e-13e3dc11a9d0" />


# MOBILITY MANAGMENT
Considering we 3D designed everything ourselves, we decided to split the vehicle in three parts: the front ( steering ), the back  ( drive ) and the middle ( connection beetween two ).They are connected so that the top part of the drive and the bottom part of the middle part allign and then we screw through both of them.  We did that so that if there is failure for example the steering, we do not haveto print it all again, but just the steering part. That is also why we tried to design everything so that we can tighten it by screws. 

The round pillars that rise from the pplatforms are holders for OUR OWN PCB. 

## DRIVING
For the driving power, the motor, we decided to go with TT Yellow Gear Motor because it was strong enough, reliable, affordabble and available to us. We stabillised it to the platform by designing a holder for it. 
With two helix gears, whose ratio is 1:2 (so that we gain torque since the speed is not as necessary), we created a transmission. We used [helix gears](https://www.google.com/search?q=helix+gears&ie=UTF-8) so that
they do not skip and have tighter grip. To the second, bigger gear, we created a plus shaped hole since we needed the shaft to rotate with the gear. The two shafts are also plus shaped and connected by a plus shaped connector. 
At the ends of those shafts is a rectangular shaft so that we avoid the shaft spining and not rotating the wheel. 

Here it is all together:

<img width="984" height="723" alt="image" src="https://github.com/user-attachments/assets/dc01d511-1438-4414-9b53-da198ae68498" /> 

## STEERING
For the steering, we went with a always reliable, stable, small, affordable and available SG90 servo motor. We decided on the Ackermann's steering system since it seemed more stable than pivot point turning or others. 
This is an example of the Ackermann's steering system.

<img width="1379" height="507" alt="image" src="https://github.com/user-attachments/assets/dc9a3a80-8cbf-4347-83f5-d468f4b4e1aa" />

You design a servo addon that rotates the middle shaft. The two side arms are pivotted at one point and on the other connected to the middle shaft. On the arms go wheels. Then just cover it up so that the force doesn't bring it all up. 

Considering that upfront we don't have driving power, the wheels must be able to rotate freely. So the shaft that they go on is a bit lose, so the wheels have the abilty to rotate and then just tighten it up with a designed screw. The wheels will spin when the 
drive wheels start to spin.

<img width="757" height="528" alt="image" src="https://github.com/user-attachments/assets/63f58725-53cf-4815-b6b5-5b74bd32e480" />
  
  
<br><br><br>
Here it is all together:

<img width="994" height="624" alt="image" src="https://github.com/user-attachments/assets/060c660a-1203-42e8-9e4f-b50d84e08cf1" />




# POWER AND SENSE MANAGMENT
## POWER SUPPLY
As for the competition at the national championship in Samobor, we will use a portable charger to power our autonomous robot. The charger we use is small so it will not take up too much space on the robot. This charger also has an on/off button, which can be used to turn the robot on and off. This charger outputs 5V and 3A, which is ideal for powering our autonomous robot. Portable chargers also use a BMS (battery management system) which ensures that the battery is safe and reliable. With the BMS, we can see things like battery charge, battery capacity, and we can get feedback about any problems with the battery. Our charger has a light indicator for battery charge. BMS is also used to balance cells (if some are discharged or overcharged), prevents overvoltage, underdischarge, overcurrent, and overheating.
## SENSORICS

# PICTURES
## TEAM PICTURES
## VEHICLE PICTURES
<br><br><br>
# ASSEMBLY INSTRUCTIONS
## HARDWARE

### 1. PLATFORM
Place the front / back platform next to the middle one so that the holes for the screwes corespond and then screw it. 
<br>

### 2. DRIVE
1. Install the motor inside his holder.
    - Put the motor in the holder and screw it.
    - Don't screw the holder to the platform!
2. Insert the small gear in the holder and the motor shaft on the other end.
3. Install the motor to the platform.
4. Big gear preparation
    - Take the two shafts and insert them in the gear until they are connected.
    - Put the cards on the shaft ( 2 on each side) corespondingly to the card holder holders.
5. Lower the big gear with card holders in their place.
6. Screw the cards to their holders.
7. Place the wheels at the end of the shaft.
<br><br>

### 3. STEERING
1. Place the servo in its place and screw it.
2. Place the left and the right arms in their position
3. Place the connector so that it captures both the left and the right arm.
4. Cover them up with coresponding covers.
5. Place the servo addon so that it connects from the middle of the connector to the servo.



## SOFTWARE
#### 1. Arduino Uno
1. Arduino IDE
    - Download and install the official Arduino IDE from [https://www.arduino.cc/en/software]
    - This software allows you to write code(called sketches), compile them, and upload them to your Arduino board

    **Setup**
    - Connect the Arduino Uno to your computer using a USB cable
    - Open the Arduino IDE and select your board:
        - Go to Tools - Board - Arduino AVR Boards - Arduino Uno

    **Uploading the program**
    - Open the sketch you want to run, for this robot specifically you want the one that says "THIS RUNS ON THE ARDUINO UNO"
    - Click the Upload button and the IDE will compile the code and upload it to the Arduino
    
    **Auto-running the program**
    - Once the code is uploaded the sketch is stored in the Arduino memory
    - Whenever the board is powered, the program will automatically start running, therefore you dont need any additional setup
    The Arduino Uno is successfully setup!

#### 2. Raspberry Pi 4
1. Raspberry Pi OS
    - Download and install the official Raspberry Pi Imager from[https://www.raspberrypi.com/software/]
    - This software will allow you to download and write various operating systems to a microSD card
    - In this case you want to choose Raspbian on the Operating System tab, and then choose your desired SD Card. When the OS is written on the SD Card you will want to insert it into the SD Card compartment on the Raspberry Pi 4

    **Setup**
    - You can either connect the Raspberry Pi to a monitor using its micro HDMI output or do everything with VNC(without contact). Since using a monitor and a micro HDMI cable is more intuitive you can use that option.
    - Now you will want to transfer the codes that say "THIS RUNS ON THE RASPBERRY PI" onto the Raspberry Pi 4.

    **Auto-running the program on start**
    - Open command prompt and run `sudo nano /etc/rc.local`
    
    Explanation:
    - sudo - run with administrator rights(needed because /etc/rc.local is a system file)
    - nano - text editor used to open the file
    - /etc/rc.local - a script that runs automatically at the end of every boot process on Linux

    - Now you will want to add the line
     `sudo bash -c 'sudo python3 /home/pi/<<directory>>/<<filename.py>>' &` before the line `exit 0` and save and close
     

    Explanation:
    - sudo - run as root(administrator)
    - bash -c ' ... ' - tells bash to run the command inside the quotes
    sudo python3 /home/pi/.../filename.py - runs the Python program as root using python3
    - & - runs the command in the background, so the system can continue booting without waiting for Python script to finish

    Reboot the Raspberry Pi and it will be ready to use!
