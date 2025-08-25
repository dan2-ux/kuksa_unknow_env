# This repository will be a guide to run kuksa server on unknow Linux distro. 

Workflow
The pi 5 with running unknow Linux distro will act as a main server and command provider. Another pi 5 will continuesly read the server and turn on and off the neo pixel when data is changed. 

## How to run it?
First, on the pi 5 for neo-pixel, you need to run the "compine.py" which will turn on neo-pixel when received sysnals. 
<pre>python3 compine.py</pre>
On the main pi 5, you need run multiple python files.
<pre>python3 kuksa_server</pre>
Inorder to, turn the led on, consider running the "setLight.py" file.
<pre>python3 setLight.py</pre>
To turn it off run the "downLight" file.
<pre>python3 downLight</pre>
