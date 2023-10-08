iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.142.2',
    'username': 'admin',
    'password': '123456',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.142.12',
    'username': 'admin2',
    'password': '123456',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.142.22',
    'username': 'admin3',
    'password': '123456',
}


all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (3):
       config_commands = ['hostname  RTR' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print(output) 
