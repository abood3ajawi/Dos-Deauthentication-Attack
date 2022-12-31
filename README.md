# Dos-Deauthentication-Attack
<h2>Deauthentication Frame : </h2>
<p>Deauthentication Frame is a type of packet defined in the IEEE 802.11  , used to terminate a WiFi connection it can send from access point to staion or from staion to access point , to tell a connection is close.<p/>
<h2> IEEE 802.11 Frame Format  : </h2>
<img src="https://user-images.githubusercontent.com/60039619/210155937-4320975d-f88e-43a2-bb0c-e23e09dc546d.png"/>
<p > you can generate frame using scapy and set address 1 to broadcast which mean all devices connected and address 2,3 to access point MAC_address   </p>
<h2> Capture frame on wireshark : </h2>

<h2>Hint : </h2>
<ul>
<li>use multi threading to do parallel DOS attack to all access points</li>
<li>easy to get information about nearly access point using : sudo wlist interdacename scan</li>
<li>use regex to get what you need</li>
<li>your interface should be in monitor mode </li>
<li>may while you are doing dos attack your network manager change interface to maneged mode , disable NetworkManager : sudo service NetworkManager stop</li>
  
</ul>

