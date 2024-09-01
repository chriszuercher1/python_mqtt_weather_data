#!/bin/bash
set -e

echo "Updating package list..."
sudo apt-get update

echo "Installing Mosquitto and clients..."
sudo apt-get install -y mosquitto mosquitto-clients

echo "Starting Mosquitto in the background..."
sudo mosquitto -d

echo "Setup complete!"
