# AmdGPUH265Handler
A simple Python automation for AMD GPU-accelerated video encoding using H265 via ffmpeg

Description of functionalities:
* As for now .py script is capable of handling whatever ffmpeg (build: ffmpeg-20200831-4a11a6f-win64-static) can do - which is a lot. For 
more info go to <https://ffmpeg.org/documentation.html>

* Native support for AMD GPUs arise from the use of AMD AMF H.265 (HEVC) Encoder - hevc_amf  .

* Compared to software-driven encoding of H264 -> H265 this speeds-up overall process time from 5 up to 12 times.

* For the moment CLI is the only way to run and interact with the script.

-------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------

Script requires Python 3.8 . To run it simply execute it with IDLE.

First what can be seen is the installation of additional py modules used in the script. After that name of OS is diplayed

Upon execution of script, usr has to:

0. In the directory where source video is stored, create a "_h265" folder
1. Input path for the directory in which source video is stored
2. Name of the video to be encoded WITH FILE EXTENSION - e.g. Video.mp4 or Movie.mkv
3. Value for destination video stream bitrate. In the line above there is a value of source media video bitrate.
4. Value for destination audio stream bitrate. Current number of audio channels will remain after encoding.
5. Check and confirm by typing "yes" that all values, path and filename are correct.
6. Wait for the process to end. At the right-most end of last line there's a current speed displayed - that means how may times faster 
(or slower) encoding will take related to normal play (x1.0) time. There's also a current time-stamp displayed.
7. Your encoded video will be in ..\<source video folder\_h265\<original filename>.<original container extension>

Thats it! Enjoy smaller-but-almost-the-same-quality video :)
Kamil Krysiak <kamkry18@gmail.com>