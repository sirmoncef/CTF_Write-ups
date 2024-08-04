# TFCCTF

## GREETINGS | webex

### Description: 
Welcome to our ctf! Hope you enjoy it! Have fun

Static resources:
 [here](http://challs.tfcctf.com:32055).


### Solve :

they give us a form to enter a name , after trying some xss also htmlinjection it didnt work after that 

i find that the app was using node js sso i try some ssti payload NUNJUCKS,Handlebars ...
i found that when we use #{7*7}  it render 49 sso its clearly PugJs

so we craft this payload and get our flag location cat and congrats! 
``#{global.process.mainModule.constructor._load;sh=localLoad("child_process").execSync('ls')}()}``


![alt text](<Screenshot from 2024-08-04 21-57-16.png>)


**TFCCTF{a6afc419a8d18207ca9435a38cb64f42fef108ad2b24c55321be197b767f0409}**
