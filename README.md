# cirrus-logic-audio-raspbian-scripts
Test Configuration
* rpi2 
* 32GB class 10 card
* cirrus logic audio card (new square version)
* wheezy
* Kernel patched with tar method. The method is detailed here.  http://www.element14.com/community/thread/42202/l/cirrus-logic-audio-card-working-on-the-raspberry-pi-2?displayFullThread=true
* * specifically: http://www.element14.com/community/message/145591/l/re-cirrus-logic-audio-card-working-on-the-raspberry-pi-2#145591
* <i> Untested option</i>: https://github.com/CirrusLogic/rpi-linux/wiki/Building-the-code

# Record_from_Headset.sh
Script that comes with cirrus logic audio board for rpi2 (square form factor). This is required to send the magic values to the wolfson chip to setup the device for recording from the headset connector

# timer_record.py 
Simple example to show how to setup a series of time recordings with signed 32bit, 44100khz dual channel recording.. But the jack only has a single channel for recording. Each recording is 5 seconds. The filenames are timestamped for ease of sorting. 
Check output by seeing 5 wave files created

#pyaudiotest.py
Example showing how to use pyaudio with the cirrus card.  These are provided as I the data is spread out. 
Check output by plot poping up. You have to close the plot. I have not put multiprocessing in to take care of that

#alsaaudio.py
Very similar to other tests, but used alsaaudio driver. Success is tested by looking at console for typical samled python numpy array ' [ 0. 0. 0. ..., 19. 19. 40.] the values are random


#Notes on cirrus card. 
I have not checked it for response characteristics, but I will be doing so with some test equipment. As it was purchased for the superwide bandwidth and high sample rate. I have only tested it that it records and plays back from/into the headset. I will be updating that here. 
