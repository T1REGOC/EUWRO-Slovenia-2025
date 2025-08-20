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
The goal of the Future Engineers WRO category is to design a fully autonomous vehicle that completes two different challenges in 3 minutes. The direction of the vehicles movement and the interior walls position and size
is randomized before the start of the round, so thevehicle should recognise wether to turn left or right by himself. 

OPEN CHALLENGE
In the open challenge, once the robot starts, its goal is to complete 3 laps around the map while avoiding the walls. 

OBSTACLE CHALLENGE 
In the obstacle challenge, once the robot starts, its goal is to complete 3 laps through red and green pillars while also avoiding walls. Depending on the color 
it passes the pillars either from the left or the right. Once the 3 laps are complete and robot is back in its starting area it should parallely park in the previosly set
parking spot. The parking spot is 1.5x the lenght of the vehicle. The vehicle may also start from the parking spot. 

# ENGINEERING MATERIALS

# MOBILITY MANAGMENT
## DRIVING
## STEERING


# POWER AND SENSE MANAGMENT
## POWER SUPPLY
## SENSORICS

# PICTURES
## TEAM PICTURES
## VEHICLE PICTURES

# ASSEMBLY INSTRUCTIONS
## HARDWARE
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
