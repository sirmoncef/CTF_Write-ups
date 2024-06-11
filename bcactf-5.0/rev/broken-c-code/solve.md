# Broken-C-Code:
We are given a binary `flagprinter`, upon executing it outputs what seems to be a broken flag. Firing up BinaryNinja reveals this code for `main`

```C
int32_t main(int32_t argc, char** argv, char** envp)

{
  puts("Here's your flag!\n");
  void var_a8;
  __builtin_memcpy(&var_a8, 0x400800, 0x98);
  for (int32_t i = 0; i <= 0x97; i = (i + 2))
  {
    putchar(((int32_t)((int8_t)((int32_t)(truncf(sqrt(((double)(*(uint32_t*)(&var_a8 + (((int64_t)i) << 2)) - 3))), "Here's your flag!\n"))))));
  }
  return 0;
}

```
It seems that the loop index is incrimented twice, which explains why we have the broken flag, it's skipping characters.  
I opeted to try and change the binary(Which may be a wierd solution but why not):  
Let's look at `main`'s disassembly in BinaryNinja:  

```ASM
00400646  55                 push    rbp {__saved_rbp}
00400647  4889e5             mov     rbp, rsp {__saved_rbp}
0040064a  4881eca0000000     sub     rsp, 0xa0
00400651  bfc0074000         mov     edi, 0x4007c0  {"Here's your flag!\n"}
00400656  e8b5feffff         call    puts
0040065b  488d8560ffffff     lea     rax, [rbp-0xa0 {var_a8}]
00400662  be00084000         mov     esi, 0x400800
00400667  ba13000000         mov     edx, 0x13
0040066c  4889c7             mov     rdi, rax {var_a8}
0040066f  4889d1             mov     rcx, rdx  {0x13}
00400672  f348a5             rep movsq qword [rdi], [rsi] {var_140} {var_a8}  {0x0}
00400675  c745fc00000000     mov     dword [rbp-0x4 {i}], 0x0
0040067c  eb34               jmp     0x4006b2

0040067e  8b45fc             mov     eax, dword [rbp-0x4 {i}]
00400681  8d5001             lea     edx, [rax+0x1]
00400684  8955fc             mov     dword [rbp-0x4 {var_c}], edx
00400687  4898               cdqe    
00400689  8b848560ffffff     mov     eax, dword [rbp+rax*4-0xa0 {var_a8}]
00400690  83e803             sub     eax, 0x3
00400693  660fefc0           pxor    xmm0, xmm0
00400697  f20f2ac0           cvtsi2sd xmm0, eax
0040069b  e8a0feffff         call    sqrt
004006a0  f20f2cc0           cvttsd2si eax, xmm0
004006a4  0fbec0             movsx   eax, al
004006a7  89c7               mov     edi, eax
004006a9  e852feffff         call    putchar
004006ae  8345fc01           add     dword [rbp-0x4 {i} {var_c}], 0x1

004006b2  8b45fc             mov     eax, dword [rbp-0x4 {i}]
004006b5  3d97000000         cmp     eax, 0x97
004006ba  76c2               jbe     0x40067e

004006bc  b800000000         mov     eax, 0x0
004006c1  c9                 leave    {__saved_rbp}
004006c2  c3                 retn     {__return_addr}
```

The instruction:  
`004006ae  8345fc01           add     dword [rbp-0x4 {i} {var_c}], 0x1`
Seems to be incrementing `i` by one. Logically changing that 1 to 0 would fix the program.  
We can edit the line with BinaryNinja by right clicking the line going to `Patch`, and choosing `Edit Current Line`.  
Now we can change the 0x1 to 0x0. Afte that we save the file.  
Executing the new patched binary will give us our flag:  
`bcactf{c_c0dE_fIXeD_7H4NK5_762478276}`
