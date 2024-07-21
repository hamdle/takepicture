Requirements
------------
PHP
Python, Pip

Install
-------
$ pip install pygame
$ pip install opencv-python

Run
---
$ php run.php

$ php run.php /home/eric/repos/takepicture

$ php run.php /home/eric/repos/takepicture 3

Arg 1: Directory that holds takepicture python script.
Arg 2: Number of minutes between running python script.

RaspberryPi
-----------
Setup -- run script on boot. Reboot every 60 minutes to reset camera due to
Lenovo camera saturation bug.

1.
$ vim /etc/rc.local

Note: rc.local runs every time raspberrypi boots

2.
Current:
$ sh /home/eric/scripts/run.sh & sleep 60m; reboot

Should work, needs tested:
$ php /home/eric/repos/takepicture/run.php /home/eric/repos/takepicture & sleep & sleep 60m; reboot

Note: place before exit 0

TODO
----
- fix post data issue
- replace key with login token authentication
- make url configurable in .env file
- make id configurable in .env file
- write output to tmp file
- launch terminal and tail output file on startup
