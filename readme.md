Off button support for Raspberry Pi
===================================

Super-simple shut down support for the Raspberry Pi. 

#### Usage

Short BCM pin 21 to ground for three seconds using a female-female jumper wire.
(The two closest pins to the USB ports.)

#### Installation

````
pi@pi:~ $ git clone https://bitbucket.org/patricktokeeffe/raspbian-off-button.git
Cloning into 'raspbian-off-button'...
...
pi@pi:~ $ ls
raspbian-off-button
pi@pi:~ $ sudo crontab -e
````

Add this line, then save and exit (^X, Y).

````
@reboot /home/pi/raspbian-off-button/offbutton.py &
````

