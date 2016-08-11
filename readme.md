Physical Off Button for Raspberry Pi
====================================

Super-simple shut down support for the Raspberry Pi.

### Usage

Short BCM pin 21 to ground for three seconds (two pins nearest to USB ports).
It's best to use a momentary, normally open switch but female-female jumper
wires will do.

> *Paper clips/screwdrivers/what-have-you are not recommended!*

### Quick Install

**If and only if** you are using `systemd` (default in Raspbian Jessie and
newer), you can install this service in two steps:

1. Clone this repo:
   `git clone https://bitbucket.org/patricktokeeffe/rpi-off-button.git`
2. Run install script:

```
$ cd rpi-off-button
$ sudo ./install.sh
```

> The install script was made executable before committing but if you do
> encounter "command not found" errors when trying to run step 2, then
> try this first: `sudo chmod +x install.sh`.

### Installation

Fetch this repository from source, copy script to system directory (under new
file name) and grant installed file executable permissions.

````
pi@pi:~ $ git clone https://bitbucket.org/patricktokeeffe/rpi-off-button.git
Cloning into 'rpi-off-button'...
...
pi@pi:~ $ cd rpi-off-button
pi@pi:~/rpi-off-button $ ls
off-button.py  off-button.service  readme.md
pi@pi:~/rpi-off-button $ sudo cp off-button.py /usr/sbin/off-button
pi@pi:~/rpi-off-button $ sudo chmod +x /usr/sbin/off-button
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
pi@pi:~/rpi-off-button $ ls
off-button.py  off-button.service  readme.md
pi@pi:~/rpi-off-button sudo cp off-button.service /etc/systemd/system/
pi@pi:~/rpi-off-button sudo systemctl enable off-button.service
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
● off-button.service - Off button service
   Loaded: loaded (/etc/systemd/system/off-button.service; enabled)
   Active: active (running) since Mon 2016-03-14 14:12:31 GMT+8; 4s ago
 Main PID: 28771 (off-button.py)
   CGroup: /system.slice/off-button.service
           └─28771 /usr/bin/python /home/pi/raspbian-off-button/off-button.py

Mar 14 14:12:31 tracer systemd[1]: Started Off button service.
pi@pi:~ $ sudo service off-button stop
pi@pi:~ $ sudo service off-button start
```

> As of 2016-03-14, there is (apparently) no support for symlinking the service
> file from a source repository into the "proper directory" (/var/systemd/system/).
> You can read about why [here](https://bugzilla.redhat.com/show_bug.cgi?id=955379).
>
> **TL;DR** Copy service files because symlinks are too ambiguous.

#### Raspbian Wheezy & earlier

In Raspbian Wheezy (based on Debian 7) the recommended method of auto-starting this
script is to schedule an "`@reboot`" cron task. Since the script requires root-level
permissions for GPIO access, and since does not interact with logged-in users or the
file system, this is a reasonably robust and secure compromise. (It's worth noting
this method provides no way to stop or restart this script!)

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
@reboot python /the/full/path/to/off-button.py &
````

Of course, you should specify the *actual* path, which may be something like
`/home/pi/rpi-off-button/off-button.py`. Save and exit (^X, Y) to make changes
effective.
