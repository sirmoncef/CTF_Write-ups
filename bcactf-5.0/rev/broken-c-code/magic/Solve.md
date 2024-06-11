# BCACTF 5.0

## magic - 75 | reverse

### Description: 
I found this piece of paper on the floor. I was going to throw it away, but it somehow screamed at me while I was holding it?!



Static resources:
 [here](https://arcs-s3-repo.nyc3.cdn.digitaloceanspaces.com/magic/magic.pdf).


### Solve :

this is a forensics reverse challenge first of all we try simple stegano tool and we find in exif a tag : ![alt text](<../ScreenShots/Screenshot from 2024-06-10 13-18-58.png>)

Producer : 283548893274

after that we used binwalk to extract the files in the pdf file and we find a js Obfuscated file 

![alt text](<../ScreenShots/Screenshot from 2024-06-10 13-22-56.png>)

![alt text](<../ScreenShots/Screenshot from 2024-06-10 13-23-28.png>)

after deobsificate i wrote a script to get the flag using the Producer : 283548893274

[text](magic.py)



**bcactf{InTerACtIv3_PdFs_W0W_cbd14436e6aea8}**
