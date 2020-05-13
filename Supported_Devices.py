from netmiko import ConnectHandler
from netmiko.ssh_exception import AuthenticationException

USERNAME = ''
PASSWORD = ''

device = {
       'device_type': 'fortigate'
}
for devices in device:
       ip_address_of_device = devices
       ios_device = {
              'device_type':'fortigate',
              'ip': ip_address_of_device,
              'username': USERNAME,
              'password': PASSWORD
       }

       try:
              net_connect = ConnectHandler(**device)
       except (AuthenticationException):
              print ('Authentication failure: ' + ip_address_of_device)
              continue
       except Exception as unknown_error:
              print ('Something went wrong:' + str(unknown_error))
              continue



