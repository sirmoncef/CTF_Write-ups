# WANICTF

## Surveillance_of_sus |NORMAL | Forensics

### Description: 
悪意ある人物が操作しているのか、あるPCが不審な動きをしています。

そのPCから何かのキャッシュファイルを取り出すことに成功したらしいので、調べてみてください！

A PC is showing suspicious activity, possibly controlled by a malicious individual.

It seems a cache file from this PC has been retrieved. Please investigate it!



 [here](https://score.wanictf.org/storage/x11rcthpe10na4qv2q4zkldxa204lmk6/for-Surveillance-of-sus.zip).


### Writer : Mikka


### Solve :

after i tried basic stegano tools i didint find anything 
after i use 
`xxd Cache_chal.bin| head`
we find 
```
00000000: 5244 5038 626d 7000 0600 0000 f617 b0bf  RDP8bmp.........
00000010: 6e5f cea9 4000 4000 0000 00ff 0000 00ff  n_..@.@.........
00000020: 0000 00ff 0000 00ff 0000 00ff 0000 00ff  ................
00000030: 0000 00ff 0000 00ff 0000 00ff 0000 00ff  ................
00000040: 0000 00ff 0000 00ff 0000 00ff 0000 00ff  ................
00000050: 0000 00ff 0000 00ff 0000 00ff 0000 00ff  ................
00000060: 0000 00ff 0000 00ff 0000 00ff 0000 00ff  ................
00000070: 0000 00ff 0000 00ff 0000 00ff 0000 00ff  ................
00000080: 0000 00ff 0000 00ff 0000 00ff 0000 00ff  ................
00000090: 0000 00ff 0000 00ff 0000 00ff 0000 00ff  ................
```

so after ssome searchind i find  areppo on github about  cached file of BMP

[here](https://github.com/ANSSI-FR/bmc-tools)

so we used it 

`./bmc-tools.py -s ../Downloads/for-Surveillance-of-sus/Cache_chal.bin -d ../Downloads`

and we get many bmp filess we can find the flag in characters in this files 






**FLAG{RDP_is_useful_yipeee}**