Physical Off Button for Raspberry Pi
====================================

Super-simple shutdown for Raspberry Pi: close circuit between pin BCM 21 and
ground for 3+ seconds to initiate a clean shutdown.

### Requirements

* git (for preferred install method)
* Python 2 or 3
    * *RPi.GPIO*, <https://pypi.org/project/RPi.GPIO/> (*assumed to already be
      installed, which is true for Raspbian Jessie and newer*)

### Getting Started

> *For older/alternate distros that do not use *systemd* (e.g. Raspbian Wheezy
> and earlier), perform a [manual install](manual-install.md) instead.*

To install as automatic *systemd* service, clone this repo then run `install.sh`:
```
git clone https://github.com/patricktokeeffe/rpi-off-button.git`
cd rpi-off-button
sudo ./install.sh
```

### Usage

* To initiate a clean shutdown, short BCM pin 21 to ground for three seconds (i.e.
  connect the two pins nearest to USB ports), then wait up to ten more seconds for
  the shutdown routine to finish. 
    * > A momentary, normally open switch is the best choice, but female-female
      > jumper wires will do. (*Paper clips/screwdrivers/etc are not recommended!*)
* If the circuit re-opens before three seconds, shutdown will not occur.
* After shutting down, the Pi will blink its green power light once per second
  about 5 times to signal its ready to power off.


