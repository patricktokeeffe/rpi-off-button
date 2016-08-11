#!/bin/bash

echo "Installing service executable..."
cp ./off-button.py /usr/sbin/off-button
chmod +x /usr/sbin/off-button

echo "Installing service configuration..."
cp ./off-button.service /etc/systemd/system/
echo "Registering service with systemd..."
systemctl enable off-button.service

echo "Starting Off button service..."
systemctl start off-button.service

echo "Successfully installed Off button service."
echo 'To view service status, run "systemctl status off-button"'
