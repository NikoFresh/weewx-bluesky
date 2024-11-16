# installer for Twitter
# Copyright 2014-2020 Matthew Wall
# Distributed under the terms of the GNU Public License (GPLv3)

from weecfg.extension import ExtensionInstaller


def loader():
    return BlueSkyInstaller()


class BlueSkyInstaller(ExtensionInstaller):
    def __init__(self):
        super(BlueSkyInstaller, self).__init__(
            version="0.1",
            name='bluesky',
            description='publish weather data on bluesky',
            author="Nicolò Frescura",
            author_email="nicolo.frescura@pm.me",
            restful_services='user.bluesky.BlueSky',
            config={
                'StdRESTful': {
                    'BlueSky': {
                        'username': 'USERNAME',
                        'password': 'PASSWORD'}}},
            files=[('bin/user', ['bin/user/bluesky.py'])]
        )
