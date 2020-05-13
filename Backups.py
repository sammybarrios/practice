import time
import datetime
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetmikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import getpass
from time import strftime

date_time = strftime('%d-%m-%Y')

#USERNAME = raw_input('Enter you SSH username: ')
USERNAME = 'admin'
#PASSWORD = getpass()
PASSWORD = ''

#with open ('command_file') as file:
#       command_list = file.read().splitlines()

with open ('ip_list.txt') as file:
       ip_device_list = file.read().splitlines()

for devices in ip_device_list:
       print ('Connecting to device ' + devices)
       ip_address_of_device = devices
       ios_device = {
              'device_type':'fortinet',
              'ip': ip_address_of_device,
              'username': USERNAME,
              'password': PASSWORD
       }

       try:
              net_connect = ConnectHandler(**ios_device)
       except (AuthenticationException):
              print ('Authentication failure: ' + ip_address_of_device)
              continue
       except (NetmikoTimeoutException):
              print ('Timeout to device: ' + ip_address_of_device)
              continue
       except (SSHException):
              print ('SSH Issue, SSH may be disable in device' + ip_address_of_device)
              continue
       except Exception as unknown_error:
              print ('Something went wrong:' + str(unknown_error))
              continue


       output = net_connect.send_command('get system status | grep -f Hostname')
       output = str(output)
       output = output.replace('Hostname: ','')
       output = output.replace('\n', '')
       hostname = output.replace(' <---','')
       config = net_connect.send_command('show')
       file = open(hostname+'_' + ''+date_time+'.txt', "w")
       file.write(config)
       print('Backup was successful for '+hostname+'!')
       net_connect.disconnect()


