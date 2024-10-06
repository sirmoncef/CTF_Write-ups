# IRONCTF 24

## ceralShop | webex

### Description: 

asked my friend to set up a website for my shop. He says it's completely secure, and no one can get access to the source. Can you prove him wrong?

# Author: 4rUN


### Solve :

LFI & php deserialization vuln :

FIRSTLY we get a base64 , inside it we got a hint about lfi so we try :

```https://cerealshop.1nf1n1ty.team/?file=/etc/passwd``` it works ! 

next after some tries we got the source ate index.php

[text](index.php)

we can observe a type juggling attack here 

so i create i php script to get the right coockie and get the flag 

[text](solve.php)




**ironCTF{D353r1411Z4710N_4T_1T5_B35T}**




