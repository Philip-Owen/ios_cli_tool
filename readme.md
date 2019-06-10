# IOS CLI Tool

A simple CLI program that will run a given command on a Cisco IOS device.

- Written with Python 3.7.
- `pip install requirements.txt`
- Parameters
    - `--host` - The IP or Hostname of device you are trying to connect to.
    - `--user` - The username to use to authenticate to the host.
    - `--cmd`  - The command you are trying to run against the device. Wrap
               command in quotes.

#### Example

```
> python net-tool.py --host 10.0.0.1 --user admin --cmd 'sho ver | i uptime'


Password for admin:


*********************************************************************************************

Command: sho ver | i uptime

IOS-SW-1 uptime is 20 weeks, 22 hours, 33 minutes

*********************************************************************************************
```