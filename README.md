# cirrus-logic-audio-raspbian-scripts
Test Configuration
* rpi2 
* 32GB class 10 card
* cirrus logic audio card (new square version)
* wheezy
* Kernel patched with tar method. -- will post link later 

# Record_from_Headset.sh
Script that comes with cirrus logic audio board for rpi2 (square form factor). This is required to send the magic values to the wolfson chip to setup the device for recording from the headset connector

# timer_record.py 
Simple example to show how to setup a series of time recordings with signed 32bit, 44100khz dual channel recording.. But the jack only has a single channel for recording. Each recording is 5 seconds. The filenames are timestamped for ease of sorting. 

#pyaudiotest.py
Example showing how to use pyaudio with the cirrus card.  These are provided as I the data is spread out. 
