Physical Off Button for Raspberry Pi
====================================

Super-simple shut down support for the Raspberry Pi.

### Usage

Short BCM pin 21 to ground for three seconds (two pins nearest to USB ports).
It's best to use a momentary, normally open switch but female-female jumper
wires will do.

> *Paper clips/screwdrivers/what-have-you are not recommended!*

### Installation

Fetch this repository from source, then enter the directory and grant executable
permissions to `off-button.py`.

````
pi@pi:~ $ git clone https://bitbucket.org/patricktokeeffe/raspbian-off-button.git
Cloning into 'raspbian-off-button'...
...
pi@pi:~ $ cd raspbian-off-button
pi@pi:~/raspbian-off-button $ ls
off-button.py  off-button.service  readme.md
pi@pi:~/raspbian-off-button $ sudo chmod +x off-button.py
````

#### Raspbian Jessie

As of Raspbian Jessie (based on Debian 8), services are managed by `systemd`. This
transition simplifies the creation and management of services by removing the need
to daemonize scripts or rely on the `@reboot` cron trigger. With systemd, we create
one file describing the service, then enable it and -viola- the script is now
accessible like any other service.

Since the service file has already been created (`off-button.service`), all you
must do is copy it into the proper directory (`/etc/systemd/system`), then enable
run-at-boot for it (`systemctl enable`):

```
pi@pi:~/raspbian-off-button $ ls
off-button.py  off-button.service  readme.md
pi@pi:~/raspbian-off-button sudo cp off-button.service /etc/systemd/system/
pi@pi:~/raspbian-off-button sudo systemctl enable off-button.service
...
```

That's it. Now you should be able to issue commands like for any other service:

```
pi@pi:~ $ systemctl
...
...
off-button.service                                     loaded active running   Off button service
...
...
pi@pi:~ $ sudo service off-button status
 * off-button.service - Off button service
   Loaded: loaded (/etc/systemd/system/off-button.service; enabled)
   Active: active (running) since Thu 2016-03-10 15:47:50 GMT+8; 3 days ago
 Main PID: 313 (off-button.py)
   CGroup: /system.slice/off-button.service
           └─313 /usr/bin/python /home/pi/raspbian-off-button/off-button.py

Mar 10 15:47:50 tracer systemd[1]: Started Off button service.
pi@pi:~ $ sudo service off-button stop
pi@pi:~ $ sudo service off-button start
```

> As of 2016-03-14, there is (apparently) no support for symlinking the service
> file from a source repository into the "proper directory" (/var/systemd/system/).
> You can read about why [here](https://bugzilla.redhat.com/show_bug.cgi?id=955379).
>
> **TL;DR** Copy service files because symlinks are too ambiguous.

#### Raspbian Wheezy & earlier

In Raspbian Wheezy (based on Debian 7) the recommended method of aut0-starting this
script is to schedule an "@reboot" cron task. Since the script requires root-level
permissions for GPIO access, and since does not interact with logged-in users or the
file system, this is a reasonably robust and secure compromise. (It's worth noting
the "@reboot" method provides no way to stop or restart this script!)

> Services in Raspbian Wheezy are controlled by `initd`. While it is possible to
> turn scripts into services with initd, the additional legwork required means it
> is beyond the scope of this writeup. :(

To use the cron reboot technique, open the root user cron table...

````
pi@pi:~ $ sudo crontab -e
````

...and add the following line. (Don't forget the ampersand `&`, which tells the
command to run in the background.)

````
@reboot /home/pi/raspbian-off-button/off-button.py &
````

Save and exit (^X, Y) to make changes effective.

