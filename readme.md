# bluesky

WeeWX extension that sends data to BlueSky

## Pre-requisites

Install the atproto python bindings

```bash
sudo pip3 install atproto
```

## Installation instructions

1. download

```bash
wget -O weewx-bluesky.zip https://github.com/NikoFresh/weewx-bluesky/archive/master.zip
```

2. run the installer:

```bash
weectl extension install weewx-bluesky.zip
```

3. modify weewx.conf:

```conf
[StdRESTful]
    [[BlueSky]]
        username = USERNAME
        password = PASSWORD
```

4. restart weewx

```bash
sudo systemctl stop weewx
sudo systemctl start weewx
```

## Configuration

This is how a full configuration looks like:

```conf
[StdRESTful]
    [[BlueSky]]
        username = USERNAME  # Required
        password = PASSWORD  # Required
        station = hal        # Name of the weather station
        format = {station:%.8s}: Ws: {windSpeed:%.1f}, Wd: {windDir:%03.0f}, Wg: {windGust:%.1f}, oT: {outTemp:%.1f}, oH: {outHumidity:%.2f}, P: {barometer:%.3f}, R: {rain:%.3f}  # Default message format
        format_None = -  # How a missing value has to be displayed
        format_utc = False  # When True display date and time in UTC format instead of local
        unit_system = METRICWX  # US, METRIC, METRICWX
        website = False  # Set to True to enable website embed
        website_url = https://example.com  # Defaults to station_url from weewx.conf
```

## License

```
Copyright 2024 Nicolò Frescura
Distributed under the terms of the GNU Public License (GPLv3)
```
