import subprocess

def CreateWifiConfig(SSID, password):
  config_lines = [
    'ctrl_interface=DIR=var/run/wpa_supplicant Group=netdev',
    'update_config=1',
    'country=IN',
    '\n',
    'network={',
    '\tssid="{}"'.format(SSID),
    '\tpsk="{}"'.format(password),
    '\tkey_mgmt=WPA-PSK',
    '}'
  ]

  config = '\n'.join(config_lines)
  print(config)

  with open("/etc/wpa_supplicant/wpa_supplicant.conf", "w") as wifi:
    wifi.write(config)

  print("Wifi config added")



#CreateWifiConfig("Elonmusk","Flamenco")
CreateWifiConfig("INBLRFTWIFIB2","Flamenco#abcd)")

subprocess.call(["sudo","systemctl", "daemon-reload"])
subprocess.call(["sudo", "systemctl", "restart", "dhcpcd"])
subprocess.call(["sudo", "dhclient", "wlan0"])

print("changed Network")
