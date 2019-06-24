## Manual installation

To install this program manually:

1.  Either [download](https://github.com/patricktokeeffe/rpi-off-button/releases) or
    clone the source code to your Pi:
    ```
    git clone https://github.com/patricktokeeffe/rpi-off-button.git
    cd rpi-off-button
    ```

2.  Then copy the program script into system directory:
    ```
    sudo cp off-button.py /usr/sbin/off-button
    ```

3.  Enable file execution:
    ```
    sudo chmod +x /usr/sbin/off-button
    ```

4.  And, finally, start the program at boot using a method below.


### *systemd*

To use *systemd* with a manual installation, copy the provided service file and
enable the service with standard commands:
```
sudo cp off-button.service /etc/systemd/system/
sudo systemctl enable off-button.service
sudo systemctl restart off-button.service
```

### *cron*

For distros without *systemd*, schedule the script at reboot using *cron*:
```
sudo crontab -e
```
```
 ...
+@reboot /usr/sbin/off-button &
```

