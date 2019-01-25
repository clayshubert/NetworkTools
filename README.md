# Instructions/Tool List
Some of the tools included require edits and/or applications.

Find tools below to find the specific needs for each.

# mac_change_linux
Description: This tool will change the MAC address that is assigned to any port you choose. This can be very useful to remain anonymous and prevent unauthorized access to a machine. This tool is designed for linux OS therefore, it may not work on another OS such as Windows or OSX

Instructions:
  1. Open terminal and change to the directory this tool is located in most likey located in $cd Desktop
  2. Type $vim mac_change_linux.py
  3. Open a new terminal and type $ifconfig
  4. In the original terminal replace port_name and your_mac_address by pressing the i key. The values can be replaced with the values that are found in ifconfig
  5. Press esc and type :wq to save and exit the file
  6. In the same terminal type $python mac_change_linux.py and it will run.
