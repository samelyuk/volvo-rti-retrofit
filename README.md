# volvo-rti-retrofit
Volvo S60 RTI retrofit with Android Auto, Carplay, Handsfree etc.

Welcome to the OpenAutoPro project tailored for the Volvo S60 D5! This project enhances your driving experience by integrating a Raspberry Pi and Arduino into your vehicle, replacing the CD reader from the RTI system. Utilizing the stock RTI display and controls ensures seamless integration.

## Table of Contents
1. [Connection Overview](#connection-overview)
   - [Necessary Components](#necessary-components)
   - [Cable Management](#cable-management)
   - [SWM Button Configuration - LIN bus](#swm-button-configuration---lin-bus)
   - [RTI Control Module Setup](#rti-control-module-setup)
   - [AUX Integration](#aux-integration)
2. [Programming Details](#programming-details)
   - [Arduino 1: Handling button inputs via LIN bus](#arduino-1-handling-button-inputs-via-lin-bus-controlling-the-rti-display)
   - [Arduino 2: Emulating a CD changer for AUX functionality](#arduino-2-emulating-a-cd-changer-for-aux-functionality)
   - [Raspberry Pi: OpenAutoPro installation, setup, Arduino connectivity, and configuring the splash screen](#raspberry-pi-openautopro-installation-setup-arduino-connectivity-and-configuring-the-splash-screen)

## Connection Overview

### Necessary Components
- Raspberry Pi 4, 2 GB RAM: SD Card 64GB
- USB Sound Card Vention (https://www.alza.sk/vention-usb-external-sound-card-0-15m-gray-metal-type-omtp-ctia-d6093937.htm)
- Bluetooth Orico BTA-409 (https://www.alza.sk/orico-bta-409-biely-d6447277.htm)
- Arduino Nano (Original ATmega328) - Clone doesn’t read SWM buttons
- Arduino Nano (China clone) - For AUX
- MCP2025 Chip
- Step-Down Converter 12V-5V, 5A
- Ground Loop Isolator - From Aliexpress (https://shorturl.at/lSVW0)
- Various cables, connectors, etc.

### Cable Management
Efficient cable management is essential for organizing the components of the OpenAutoPro project within the Volvo S60 D5. Let's discuss how we've optimized cable routing for a tidy and functional setup.
- Utilizing Original Cables
- Power Source Selection

### SWM Button Configuration - LIN bus
To integrate the SWM (Steering Wheel Mounted) buttons along with the RTI (Road and Traffic Information) buttons into the OpenAutoPro system, we'll leverage the LIN bus communication protocol.
- Hardware Setup
- Software Implementation
- Key Codes for Volvo S60 2008

### RTI Control Module Setup
I have removed almost everything from the RTI Control Module box. I only left two connectors: an 8-pin DIN socket and a 10-pin connector from the display. I have placed all the computing components in this box: Raspberry Pi with all its components, a step-down converter, and two Arduino microcontrollers on a PCB.

### AUX Integration
While the Volvo S60 from 2008 typically comes equipped with an AUX input, my model had its radio upgraded to the HU-850, an older version lacking this feature. Following Karl Hagström's guide (https://gizmosnack.blogspot.com/2015/11/aux-in-volvo-hu-xxxx-radio.html), I created a CD changer emulator using an Arduino Nano clone.

## Programming Details

### Arduino 1: Handling button inputs via LIN bus, controlling the RTI display
- Details about Arduino 1

### Arduino 2: Emulating a CD changer for AUX functionality
- Details about Arduino 2

### Raspberry Pi: OpenAutoPro installation, setup, Arduino connectivity, and configuring the splash screen
- Details about Raspberry Pi
