import subprocess

subprocess.call("ifconfig //port_name// down", shell=True)
subprocess.call("ifconfig //port_name// hw ether //your_mac_address//", shell=True)
subprocess.call("ifconfig //port_name// up", shell=True)

