import netmiko
from getpass import getpass
import click

def connect(device_ip, username, cmd):
    device = {
        'device_type': 'cisco_ios',
        'host': device_ip,
        'username': username,
        'password': getpass(f'\n\nPassword for {username}:')
    }

    conn = netmiko.ConnectHandler(**device)
    output = f'\n\n*********************************************************************************************\n\n'
    output += f'Command: {cmd}\n\n'
    output += conn.send_command(cmd)
    output += '\n\n*********************************************************************************************\n\n'
    conn.disconnect()
    return output

def review_args(h, u, c):
    print('\n\n************************************* Missing Arguments *************************************\n\n')
    print('Missing 1 or more arguments.Please review below:\n')
    print(f'Host: {h}')
    print(f'Username: {u}')
    print(f'Command: {c}')
    print('\n\n*********************************************************************************************\n\n')

@click.command()
@click.option('--host', default=False, help="The IP or Hostname of device you are trying to connect to.")
@click.option('--user', default=False, help="The username to use to authenticate to the host.")
@click.option('--cmd', default=False, help="The command you are trying to run against the device. Wrap command in quotes.")
def main(host, user, cmd):
    if host and user and cmd:
        print(connect(host, user, cmd))
    else:
        review_args(host, user, cmd)

if __name__ == '__main__':
    main()
