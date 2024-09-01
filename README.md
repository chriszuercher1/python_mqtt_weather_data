# MQTT Example with Raspberry Pi

This repository contains an example project that demonstrates how to use the MQTT protocol to stream weather data. The project utilizes the `mosquitto` MQTT broker and the `paho-mqtt` Python client library to send and receive messages.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Understanding MQTT](#understanding-mqtt)

## Introduction

Message Queuing Telemetry Transport (MQTT) is a lightweight messaging protocol designed for devices that require a small code footprint or have limited network bandwidth. It is widely used in IoT (Internet of Things) devices due to its efficiency and simplicity.

This project showcases how to set up an MQTT broker using `mosquitto` and how to create a simple Python client using `paho-mqtt` to send and receive messages.

## Requirements

Before you begin, ensure you have forked the GitHub repository: https://github.com/mario-gellrich-zhaw/python_mqtt_weather_data

## Installation

Based on the GitHub repository you must create a new GitHub Codespaces environment.

### Usage

The mosquitto broker should automatically start after installation (see setup.sh).

To make sure it runs, you can open a Terminal and type:

```bash
mosquitto -d 
```
To run the MQTT example, run the mqtt_publisher.py and the app.py in separate Terminals.

```bash
# Run the publisher
python mqtt_publisher.py

# Run the subscriber (optional)
python mqtt_subscriber.py

# Run the app
python app.py
```

## Understanding MQTT

**What is MQTT?**  
MQTT stands for Message Queuing Telemetry Transport. It is a publish/subscribe messaging protocol that works on top of the TCP/IP protocol. MQTT is designed to be lightweight, making it ideal for use in constrained environments such as IoT devices.

**How MQTT Works**
Broker: The central server that receives all messages from the clients and routes them to the appropriate subscribers.
Client: Any device or application that connects to the broker to send (publish) or receive (subscribe) messages.
Topic: The routing information for the broker to send the message to the correct clients. Topics are organized hierarchically using slashes (e.g., house/sensor1).

**Why Use MQTT?** 
Efficiency: MQTT minimizes network bandwidth and device resource requirements, making it ideal for low-power devices.
Simplicity: The publish/subscribe model is easy to understand and implement.
Reliability: MQTT can ensure messages are delivered at least once, exactly once, or at most once.