# Simple script to automate transcoding videos to H265 using ffmpeg pack
# As for current version, it is dedicated to AMD GPU's
# Created by Kamil Krysiak <kamkry18@gmail.com>
#

import os                                                       # library for capturing OS type/verison
import subprocess                                               # library for handling Powershell <-> Python communication
import time                                                     # library for handling time (to be able to wait :) )
import pathlib                                                  # library for opening paths using '\

#subprocess.run(["powershell.exe", "pip install ffmpeg-python"]) # install ffmpeg-python API;
subprocess.run(["powershell.exe", "pip install string-color"])  # install coloring feature for Python3
subprocess.run(["powershell.exe", "pip install pymediainfo"])   # install video metadata read module for Python3

# Dedicated to PowerShell in Windows
print()
print()

from stringcolor import *
# color-ify things a bit
print('Welcome to simple Python script for easy, seamless transition into H265-coded videos!')
system_name = os.name
print('Your OS is: ' + cs(system_name, "Blue"))
time.sleep(1)

print('Will use FFMPEG codec pack for encoding')
print('Type-in path with videos to be transcoded: ', end = '')
path_input = input()                                            # Path to directory containing video file

print('Type-in name of file to be transcoded: ', end = '')
file = input()                                                  # Path to particular video file
from pymediainfo import MediaInfo
media_info = MediaInfo.parse(str(path_input) + "/" + str(file))

for track in media_info.tracks:
    if track.bit_rate is not None:
        print("{}: {}".format(track.track_type, track.bit_rate))                            # Preapring info about current video bitrate
        break

print('Current video bitrate: ' + cs(str(track.bit_rate / 1000000), "Blue") + ' Mbps')
print("Type-in target VIDEO bitrate value (in Mbps): ", end = '')
target_bitrate_video = input()                                  # Declaration of targeted video bitrate

    # ADD IMPLEMENTATION FOR RETRIVING CURRENT AUDIO BITRATE AND NO. OF CHANNELS

print("Type-in target AUDIO bitrate value (in kbps): ", end = '')
target_bitrate_audio = input()                                  # Declaration of targeted audio bitrate

print('Please confirm all settings: ', end = '')
print('Source file: ' + cs(str(path_input), "DeepPink3") + cs("/", "DeepPink3") + cs(str(file), "DeepPink3"))
time.sleep(2)

print('Target video bitrate: ' + cs(str(target_bitrate_video), "DeepPink3") + cs(" Mbps", "DeepPink3"))
print('Target audio bitrate: ' + cs(str(target_bitrate_audio), "DeepPink3") + cs(" kbps", "DeepPink3"))
print("Is that correct? " + cs("Type 'yes': ", "Red"), end = '')
confirmation = input()

if str(confirmation) == "yes":
    from pathlib import Path
    command = Path("ffmpeg -hwaccel auto -i " + str(path_input) + "/" + str(file) + " -c:v hevc_amf -preset medium -b:v " + str(target_bitrate_video) + "M -c:a ac3 -b:a " + str(target_bitrate_audio) + "k " + str(path_input) + "/" + r"_h265/" + str(file))
    #file_to_execute = open(command)
    print(str(command))
    subprocess.run(["powershell.exe", str(command)])

else:

    print('Terminating')

exit
