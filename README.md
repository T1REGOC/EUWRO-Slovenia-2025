# REGOČ | EUWRO-Slovenia
## TABLE OF CONTENT

| Section  | Explanation |
| --  | -- | 
| [PROBLEM](#problem)  | Adressing the task of the competition. |
| [ENGINEERING MATERIALS](#engineering-materials)  | The list of everything we used. |
| [MOBILITY MANAGMENT](#mobility-managment)  | [Driving](#driving),  [steering](#steering)| 
| [POWER AND SENSE MANAGMENT](#power-and-sense-managment)  |  [Power supply](#power-supply), [sensorics](#sensorics)  |
| [PICUTRES](#pictures)  |  [Team pictures](#team-pictures), [vehicle pictures](#vehicle-pictures)  |
| [ASSEMBLY INSTRUCIONS ](#assembly-instructions)  |  [Hardware](#hardware), [software](#software)  | 
| ---| --- |
| [3D FILES](https://github.com/T1REGOC/EUWRO-Slovenia-2025/tree/main/3d%20Models)| Files of our robot. |
| [SRC](https://github.com/T1REGOC/EUWRO-Slovenia-2025/tree/main/src) |Code. |
| [SCHEMES](https://github.com/T1REGOC/EUWRO-Slovenia-2025/tree/main/schemes)| Schemes of...  |
| [VIDEOS](https://github.com/T1REGOC/EUWRO-Slovenia-2025/tree/main/videos)| Videos of our robot. |




# PROBLEM
The goal of the Future Engineers WRO category is to design a fully autonomous vehicle that completes two different challenges in 3 minutes. The direction of the vehicles movement, interior walls position and their size in both challenges is randomized before the start of the round, so the vehicle should recognize whether to turn left or right by itself. 
This is our playfield:
<br><br>
    
<img width="1316" height="764" alt="image" src="https://github.com/user-attachments/assets/6487d5d0-3245-413a-9d87-16ab59b773b3" />

<br><br>
### OPEN CHALLENGE
In the open challenge, once the robot starts, its goal is to complete 3 laps around the map while avoiding the walls and finish in the same zone it started in.
For the Open Challenge we use ultrasonic sensors to make sure the vehicle is centered at all times, that is why we have ultrasonic sensors on both sides, and while the vehicle is centering it also looks for a pattern using the camera.
We needed to take a look at the map again:

<img width="551" height="558" alt="image" src="https://github.com/user-attachments/assets/5d573bdf-6fd6-4d35-8240-af510e401224" />

By thinking a little bit you can see that if your direction is clockwise you will pass the lines always going orange first and then blue, but if you are going counter-clockwise you will always go blue first and then orange. We did not recognize this at first, but after a few months of working on the robot it was almost like a key, because our most unpredictable sensor from the last robot(the color sensor APDS-9960) did not give accurate results so we would want to remove it in this one. That is when we got the idea that the passing of the lines(orange-blue or blue-orange) is a pattern and we could use tensorflow for that because what is a machine learning model best at? You're right, looking for patterns. Using tensorflow we would make a model that had these possible outputs(orange-blue, blue-orange or none), it is pretty straight-forward to how we would adapt looking at the output, if the camera saw orange-blue it steers right, blue-orange it steers left, then we count the times that we passed the lines and when it hit 12(3 laps) we stop.

### OBSTACLE CHALLENGE 
In the obstacle challenge, once the robot starts, its goal is again to complete 3 laps but now other than avoiding walls it has to avoid red and green pillars which are in the way. Depending on the color 
it passes the pillars either from the left or the right. Once the 3 laps are complete and robot is back in its starting area it should parallely park in the previously set
parking spot. The parking spot is 1.5x the lenght of the vehicle. The vehicle may also start from the parking spot. 
So how did we do it? We first thought about using just RGB and opencv, but we researched about the color formats and we did not want to use RGB after that because we found the superior one: HSV(Hue, Saturation, Value). So you might ask why we use this instead of RGB, its simple:
1. It seperates color(hue) from brightness(value) and saturation.
2. It is more robust to lighting changes than RGB.
3. It makes it easier to define color ranges for masking
4. RGB mixes color and brightness, so the same color can look very different under different lighting.
HSV allowed us to filter by hue, making color detection more reliable. But we dont want to solely depend on just opencv, we want to make it both more reliable and more educational therefore we added tensorflow. This time we made a model with tensorflow that looked for green or red pillars, so then in the code we made it so even though opencv saw the pillar it has no power because tensorflow was our priority. So the only way that a pillar would be detected and accepted is for our tensorflow model to find it.
Now we fixed the problem with the pillars, we gotta get the parking right, for parking we use ultrasonic sensors and also decided to use 2 instead of 1 ultrasonic sensors on the sides(you will see why in a bit), so depending on what is our steering side the parking will always be opposite(if you steer right the parking is on the left) and we would use that to our advantage, so for the parking after the last steering we would "line up" the vehicle for parking by looking at the differences of distance that the ultrasonic sensors give on the same side, so for example if the vehicle is at a 30 degree angle from the wall back sensor would give 3cm and the front one would be 8cm, what we would do in this scenario is steer the vehicle depending on which number is bigger and which side it was, and we would do this until the difference would be under 2cm.
#### PARKING
Now that we are lined up to the wall we dont want to steer until we actually need to park in, so now we look for the parking also using ultrasonic sensors but now looking solely on the back side sensor, why? Because the parking walls are 20cm wide and passing by our sensor would see this(25,25,27,28,28,2,2,28) so if you dont understand those would be the example readings from the sensor and we knew when we hit the parking spot when we would hit a "drastic change" often going in a number that is under 10cm, but we cant steer yet because we hit the first part of the parking and we want to parralel park so we need to hit the second part of the parking, we just go straight and look for another drastic change again, when we see it that means that the back side sensor(almost where the back wheels are) is at the second part of the parking, so now we reverse and steer until our back sensor hits under 5cm and then go forward and steer to line up.
   
# ENGINEERING MATERIALS
- Servo SG90 ( Why we chose it: reliable, small, previusly available to us )
<img width="120" height="100" alt="image" src="https://github.com/user-attachments/assets/297e06de-a4c1-44d1-a43a-930222bc18a4" />

- Yellow TT Gear Motor ( Why we chose it: enough torque, previously available to us, reliable ) 
<img width="120" height="120" alt="image" src="https://github.com/user-attachments/assets/0f006b9b-f0c9-4bdb-be62-2b6088ba5296" />

- HC - SRO4 Ultrasonic sensor (x6)
<img width="120" height="120" alt="image" src="https://github.com/user-attachments/assets/12170dc7-47c8-42e2-a1d5-d2da560281ac" />

- Raspberry Pi Camera v2
<img width="120" height="120" alt="image" src="https://github.com/user-attachments/assets/9018aa25-35b8-4681-9f61-39e590815c28" />

- DHT11
<img width="120" height="120" alt="image" src="https://github.com/user-attachments/assets/e7c28bec-eb27-4171-b5b0-017d9478bc55" />

- Arduino Uno
<img width="225" height="225" alt="image" src="https://github.com/user-attachments/assets/07404523-dd7a-4f33-982c-68c886350989" />

- Raspbbery Pi 4
<img width="225" height="200" alt="image" src="https://github.com/user-attachments/assets/1a91165c-ba4a-4d1d-a9f9-3d6a9ce4c3ae" />



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

Electrical scheme

<img width="900" height="900" alt="Untitled" src="https://github.com/user-attachments/assets/69ee1bd4-e610-4a38-9e00-23bfae7f1f4f" />

## POWER SUPPLY
As for the competition at the national championship in Samobor, we will use a portable charger to power our autonomous robot. The charger we use is small so it will not take up too much space on the robot. This charger also has an on/off button, which can be used to turn the robot on and off. This charger outputs 5V and 3A, which is ideal for powering our autonomous robot. Portable chargers also use a BMS (battery management system) which ensures that the battery is safe and reliable. With the BMS, we can see things like battery charge, battery capacity, and we can get feedback about any problems with the battery. Our charger has a light indicator for battery charge. BMS is also used to balance cells (if some are discharged or overcharged), prevents overvoltage, underdischarge, overcurrent, and overheating.

---
## SENSORICS

- Selection
<img width="468" height="196" alt="image" src="https://github.com/user-attachments/assets/6ffb2ff1-3bfd-4062-a7c1-46323790c880" />



  
The selection of sensors for our project was carried out systematically. For each potential component, we carefully considered not only its advantages but also every possible limitation or drawback it could introduce. This iterative process—selecting, evaluating, and refining—ensured that the final sensor set was both practical and effective for our goals.

- Ultrasonic sensors
  
One of the key design decisions was to integrate two ultrasonic sensors, positioned on both sides of the robot instead of relying on a single unit. This configuration allows the robot to align itself precisely with walls, which can then be leveraged for autonomous steering without depending solely on the camera system. By doing so, we enhanced both the reliability and independence of the navigation process.

- Digital Temperature and Humidity sensor
  
Additionally, we incorporated a DHT11 sensor to measure ambient temperature and humidity. These values directly influence the speed of sound in air, and by accounting for them, we can improve the accuracy of distance measurements from the ultrasonic sensors. This consideration highlights the importance we placed on precision and robustness in the sensor design. Therefore instead of the fixed speed of sound at 343m/s we made it a variable, and this is the formula we used:

`Speed_of_sound(m/s) = 331.4 + 0.6 * temperature(°C) + 0.0124 * Humidity(%)`

---
# PICTURES
## TEAM PICTURES
<img width="800" height="1200" alt="image" src="https://github.com/user-attachments/assets/9df28bd2-ff29-4a23-af98-29138cdcc5b7" />

Left: David , Middle: Gabriel, Right: Vedran






## VEHICLE PICTURES
Back

<img width="600" height="500" alt="image" src="https://github.com/user-attachments/assets/3df465c7-5cff-4527-9bc0-783ff32a6756" />

Bottom

<img width="600" height="900" alt="image" src="https://github.com/user-attachments/assets/c7ef07c7-b1bf-47fe-8ef7-7cdf9aff0da4" />


Left

<img width="600" height="500" alt="image" src="https://github.com/user-attachments/assets/a8083a93-98ad-4f63-b5cf-c79db2270438" />


Right

<img width="600" height="500" alt="image" src="https://github.com/user-attachments/assets/e3d95251-96f0-4648-914e-dbaabc4be084" />


Top

<img width="600" height="900" alt="image" src="https://github.com/user-attachments/assets/657b4ef5-ecfd-4628-8562-ccc09c78c346" />



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
