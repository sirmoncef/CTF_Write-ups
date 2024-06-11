# manipulate-spreadsheet-2
We are given a link to a google docs spreadsheet.
upon inspecting it we notice some weird text in cell A1
>496e206469676974616c206669656c64732077686572652064617461206c6965732c0a5365637265742070616765732062656e6561746820636c65617220736b6965732e0a43656c6c7320656e7477696e652c206d7973746572696573206665656c2c0a4c6179657273206f66207365637265747320746865792072657665616c2e

It looks like hex characters, decoding it yields
> In digital fields where data lies,
> Secret pages beneath clear skies.
> Cells entwine, mysteries feel,
> Layers of secrets they reveal.

This suggest that there's something hidden in the sheet.
All other cells are empty, but upon further inspection there's a hidden sheet called "Sheet 2" but we can't access it just yet, to access it we need to make a copy of the sheet from the "File" dialogue. Now that we have our own copy we can see the content of "Sheet 2", it has two columns, a "byte" and an "index", also just like the first sheet there's hex data in the cell A1 that decodes to:
> Lurking shadows, secrets play,
> Stealthy whispers on display.
> BITS aligned, LEAST in SIGht,
> Gleams of secrets, veiled in light.

It's a hint to least significant bits.
So here's the plan:
1- Sort the byte column according to the indices of the index column
2- Get the least significant bit of each byte
3- Decode the resulting binary 
4- Profit

I here opted to download the sheet as a CSV file to make my life easier, but I could have done most steps in google sheets.

Here's a python script to get the flag
```py
# Quick and dirty script to get the flag from the least significant bits from the binary in the CSV  
# Not the best but it does it's job  
  
import csv  
file=open('sheet2.csv','r')  
reader=csv.reader(file,delimiter=',')  
  
# Sort rows skipping the first row because it doesn't contain bytes  
sorted_rows=sorted(list(reader)[1:],key=lambda index: int(index[2]))  

flag=''  
temp_byte=''  
for row in sorted_rows: 
	# Get the LSB 
	temp_byte+=row[1][7]  
	# Decode each byte to ASCII
	if len(temp_byte)==8:  
		flag+=chr(int(temp_byte,2))  
		temp_byte=''  
  
print(flag)
```
