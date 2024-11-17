WIP


bluesky - weewx extension that sends data to BlueSky
Copyright 2014-2020 Matthew Wall
Distributed under the terms of the GNU Public License (GPLv3)

===============================================================================
Pre-requisites

You'll need Python >= 3.9 and OpenSSL >= 3.0
Install the atproto python bindings

sudo pip3 install atproto


===============================================================================
Installation instructions

1) download

wget -O weewx-bluesky.zip https://github.com/NikoFresh/weewx-bluesky/archive/master.zip

2) run the installer:

wee_extension --install weewx-bluesky.zip

3) modify weewx.conf:

[StdRESTful]
    [[BlueSky]]
        username = USERNAME
        password = PASSWORD

4) restart weewx

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start

