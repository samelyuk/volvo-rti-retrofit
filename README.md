# Volvo RTI Retrofit
Volvo P2 RTI retrofit with Android Auto, Carplay, Handsfree etc.

# Version r1.1

Welcome to the OpenAutoPro project tailored for the Volvo P2! This project enhances your driving experience by integrating a Raspberry Pi and Arduino into your vehicle, replacing the Control Module from the RTI system. Utilizing the stock RTI display and controls ensures seamless integration.

RTI Retrofit - Android Auto
![RTI Retrofit - Android Auto](https://github.com/samelyuk/volvo-rti-retrofit/blob/main/doc/INT2.jpg)

# Special Thanks

I would like to extend my sincere thanks to the following contributors who have greatly contributed to the development and success of this project:
- **Karl Hagström**: His comprehensive guide on adding AUX functionality to the Volvo HU-XXXX radio has been invaluable. Check out the guide [here](https://gizmosnack.blogspot.com/2015/11/aux-in-volvo-hu-xxxx-radio.html).
- **klalle**: For updated AUX script and contributions. Check out their GitHub gist [here](https://gist.github.com/klalle/1ae1bfec5e2506918a3f89492180565e).
- **laurynas**: For developing the Volvo LINbus reader program, which played a crucial role in integrating SWM buttons into the OpenAutoPro system. Find the program [here](https://github.com/laurynas/volvo_linbus).
- **Luuk**: Their resource on enabling Android Auto on Volvo RTI systems has been immensely helpful. More details can be found [here](https://luuk.cc/p/vD2f/Android_Auto_on_Volvo_RTI).
- **BlueWaveStudio Team** For developing OpenAutoPro. More details can be found [here](https://bluewavestudio.io/).

Your contributions have significantly enriched this project, and I deeply appreciate your efforts. Thank you!

## What is now working:
- OpenAuto Pro with Bluetooth and internal audio player, hands-free calling, 15 band equalizer, etc.
- Android Auto Wireless
- Original display via serial video
- Opening and closing the display using buttons Enter+Back.
- Change the display brightness using buttons Next+Yes/No.
- The buttons on the steering wheel, including RTI buttons.
- Rear camera

## Future works:
- Add OBD info
- Add a small battery to maintain power during engine startup
- A better case for all the components

[![Buy me a coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-%23FFDD00.svg?&style=flat&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/samelyuk)

# Table of Contents
1. [Connection Overview](#connection-overview)
   - [Necessary Components](#necessary-components)
   - [Cable Management](#cable-management)
   - [SWM Button Configuration - LIN bus](#swm-button-configuration---lin-bus)
   - [RTI Control Module Setup](#rti-control-module-setup)
   - [AUX Integration](#aux-integration)
   - [RTI Extender Cable Scheme](#rti-extender-cable-scheme)
   - [RTI Control Module Scheme](#rti-control-module-scheme)
2. [Programming Details](#programming-details)
   - [Arduino 1: Handling button inputs via LIN bus](#arduino-1-handling-button-inputs-via-lin-bus-controlling-the-rti-display)
   - [Arduino 2: Emulating a CD changer for AUX functionality](#arduino-2-emulating-a-cd-changer-for-aux-functionality)
   - [Raspberry Pi: OpenAutoPro installation, setup, Arduino connectivity, and configuring the splash screen](#raspberry-pi-openautopro-installation-setup-arduino-connectivity-and-configuring-the-splash-screen)

## Connection Overview

### Necessary Components
- Raspberry Pi 4, 2 GB RAM: SD Card 64GB
- USB Sound Card [Vention](https://www.alza.sk/vention-usb-external-sound-card-0-15m-gray-metal-type-omtp-ctia-d6093937.htm)
- Bluetooth [C-TECH BTD-02](https://www.alza.sk/c-tech-btd-02-d7866536.htm)
- Arduino Nano (Original ATmega328) - Clone doesn’t read SWM buttons
- Arduino Nano (China clone) - For AUX
- MCP2004 Chip [TME](https://www.tme.eu/sk/details/mcp2004a-e_p/integrovane-obvody-interface-ostatne/microchip-technology/)
- Step-Down Converter 12V-5V, 5A
- Ground Loop Isolator - From [Aliexpress](https://shorturl.at/lSVW0)
- Various cables, connectors, etc.
- Rear Camera for P2 [Aliexpress](https://www.aliexpress.com/item/1005006792687999.html?spm=a2g0o.order_list.order_list_main.5.a2201802Ed3mHx)
- Analog video Converter [Aliexpress](https://www.aliexpress.com/item/1005005445050331.html?spm=a2g0o.order_list.order_list_main.11.a2201802Ed3mHx)
  
RTI Retrofit - OpenAutoPro
![RTI Retrofit - OpenAutoPro](https://github.com/samelyuk/volvo-rti-retrofit/blob/main/doc/INT1.jpg)

### Cable Management
Efficient cable management is essential for organizing the components of the OpenAutoPro project within the Volvo S60 D5. Let's discuss how we've optimized cable routing for a tidy and functional setup.
Utilizing Original Cables
- To maintain a clean and integrated installation, I've repurposed existing cables from the front of the car to the trunk.
- Two cables run from the RTI display and radio to the RTI control module. While one cable remains connected between the radio and the control module, we'll utilize the other 10-pin cable from the RTI display to the control module as an extension cord.
Power Source Selection
- To ensure seamless power management, we've tapped into the backside of the 12V socket in the front. We will use 2 pins for Power and ground in RTI cable.
- The 12V socket offers the advantage of cutting off power entirely when the ignition is switched off, reducing the risk of power drain.
- In future iterations, I plan to incorporate a small battery to maintain power during engine startup, further enhancing system reliability.

![RTI Controll module](https://github.com/samelyuk/volvo-rti-retrofit/blob/main/doc/RTI-box1.jpg)
![RTI Controll module Disassembley](https://github.com/samelyuk/volvo-rti-retrofit/blob/main/doc/RTI-box2.jpg)
![RTI Controll module Disassembled](https://github.com/samelyuk/volvo-rti-retrofit/blob/main/doc/RTI-box3.jpg)

### Display Cable Connection:
Incorporating the RTI (Road and Traffic Information) display into the OpenAutoPro system requires a meticulous approach to cable connection. Let's break down the cable setup for seamless integration.
Cable Components:
- Video Cable: This cable carries the video signal from the source to the RTI display, facilitating visual output.
- Ground Cable: Ensures proper grounding for stable operation and electrical safety.
- Display Serial Cable: Facilitates communication between the display and the system, enabling control and data exchange.

![RTI Display Pinout](https://github.com/samelyuk/volvo-rti-retrofit/blob/main/doc/rti-disp.png)

### SWM Button Configuration - LIN bus
The SWM buttons from the steering wheel, along with the RTI buttons, will be read through the LIN bus. We will utilize the original Arduino Nano with MCP2025 and the "laurynas" Volvo LINbus reader program (https://github.com/laurynas/volvo_linbus). Simply pressing the required button is sufficient to view the LIN bus key code from our buttons, without the need to turn on the ignition. The key code for the Volvo S60 2008 appears as follows: Enter button: “ C1 3F 20 A0 ”

The cables from the SWM/SAS are located up to the steering wheel, under the cover. See blue arrow.
![SWM Location](https://github.com/samelyuk/volvo-rti-retrofit/blob/main/doc/SWM%20Location.png)
![SWM Pinout](https://github.com/samelyuk/volvo-rti-retrofit/blob/main/doc/SWM%20Pins.png)

### RTI Control Module Setup
I have removed almost everything from the RTI Control Module box. I only left two connectors: an 8-pin DIN socket and a 10-pin connector from the display. I have placed all the computing components in this box: Raspberry Pi with all its components, a step-down converter, and two Arduino microcontrollers on a PCB.

RTI New Setup (Will be updated)
![RTI New Setup (Will be updated)](https://github.com/samelyuk/volvo-rti-retrofit/blob/main/doc/RTI-now.jpg)

RTI Old Setup
![RTI Old Setup](https://github.com/samelyuk/volvo-rti-retrofit/blob/main/doc/RTI-old.jpg)

### AUX Integration
While the Volvo S60 from 2008 typically comes equipped with an AUX input, my model had its radio upgraded to the HU-850, an older version lacking this feature. Following Karl Hagström's guide (https://gizmosnack.blogspot.com/2015/11/aux-in-volvo-hu-xxxx-radio.html), I created a CD changer emulator using an Arduino Nano clone.

![Radio Pinout](https://github.com/samelyuk/volvo-rti-retrofit/blob/main/doc/Radio%20Pins.png)

### Rear Camera
I found a rear camera specifically for the Volvo P2, and its installation is straightforward. First, connect the camera power to a step-down converter from the 12V side. Next, connect the camera's video output to an analog video converter, which then connects to the Raspberry Pi via USB.

To activate the camera when shifting into reverse, we will use a script integrated into OpenAuto Pro. In the rear camera settings, set Pin 17. Then, take two wires from the reverse light and connect them to a relay. Additionally, take two wires from the Raspberry Pi GPIO: 3V3 power and GPIO 17, and connect them to the relay.
![RPI Gpio](https://www.raspberrypi.com/documentation/computers/images/GPIO-Pinout-Diagram-2.png)

When the reverse light is activated, the relay opens power to GPIO 17 on the Raspberry Pi, prompting OpenAuto Pro to start the camera.

### RTI Extender Cable Scheme
![RTI Control Module](https://github.com/samelyuk/volvo-rti-retrofit/blob/main/doc/RTI%20Cable%20Extender%20Scheme.png)

### RTI Control Module Scheme
![RTI Control Module](https://github.com/samelyuk/volvo-rti-retrofit/blob/main/doc/RTI%20Control%20Module%20Scheme.jpg)

## Programming Details (SOON)

![Image Description](https://github.com/samelyuk/volvo-rti-retrofit/blob/main/doc/S60.jpg)

### Raspberry Pi: OpenAutoPro installation, setup, Arduino connectivity, and configuring the splash screen

This guide outlines the steps to configure your Raspberry Pi, including exchanging the Raspberry Pi configuration file, setting up autostart for a button reader, setting the Volvo splash screen, and configuring the equalizer.

#### 1. Exchanging the Raspberry Pi Config File

To make necessary system adjustments, you need to edit the Raspberry Pi boot configuration file.

1. Open the Raspberry Pi configuration file using the following command:

    ```bash
    sudo nano /boot/config.txt
    ```

2. Modify or add any required settings based on your project’s specifications.

3. Save and exit the editor by pressing `Ctrl + X`, then `Y`, and `Enter`.

#### 2. Setting Up Autostart for Button Reader

To ensure that the `run.sh` script (which reads button inputs) runs automatically on startup, follow these steps:

1. Move the `run.sh` script to the `/home/pi` directory:

    ```bash
    sudo mv /home/pi/run.sh /home/pi
    ```

2. **Move the `key.py` file to the `/home/pi/Documents/` directory:**

    ```bash
    sudo mv /home/pi/key.py /home/pi/Documents/
    ```

3. Edit the autostart file to add the script:

    ```bash
    sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
    ```

4. Append the following line to the end of the file:

    ```bash
    @/home/pi/run.sh
    ```

5. Save and exit the editor by pressing `Ctrl + X`, then `Y`, and `Enter`.

6. Make the `run.sh` script executable:

    ```bash
    sudo chmod +x /home/pi/run.sh
    ```

7. Install the required Python package `pynput`:

    ```bash
    sudo pip3 install pynput
    ```

#### 3. Setting the Volvo Splash Screen

To set up the Volvo splash screen on your Raspberry Pi:

1. Move the splash screen files to the OpenAuto Pro directory:

    ```bash
    sudo mv /home/pi/splash1.h264 /usr/share/openautopro
    sudo mv /home/pi/splash2.h264 /usr/share/openautopro
    ```

#### 4. Exchanging the Equalizer Configuration

To set up the equalizer configuration:

1. Move the `openauto_equalizer.ini` equalizer settings to: '/home/pi/.openautopro/config/'
   
---

With these steps completed, your Raspberry Pi should be properly configured for your project, with the required scripts and configurations in place.

