# Inaccessible
We have a binary `chall`.  
Running it prints out:
> No flag for you >:(

Opening the binary in `gdb` and running `info function` to see the list of functions reveals a function `win`.  
It's fair to assume that we need to call that function. 
To call `win` we will break somewhere at main
```b main```  
and we will call win with:  
`call (char*) win()`

now we get the flag
> bcactf{W0w_Y0u_m4d3_iT_b810c453a9ac9}
