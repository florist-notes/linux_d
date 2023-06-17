# System Design and Architecture

<p align="justify">
DATA STRUCTURES

Data Structures: Manipulating Data = Structuring Data , Every Engineer moves data around on a day to day basis. Data Structures are ways to organize and manage data. e.g 1→2→4→5. or

```

      2
    ↙   ↘
  4      7
↙ ↘    ↙  ↘
3  2   1   9
```



Complexity Analysis: Time Complexity and Space Complexity = Space Time Complexity. Different Data Structures have different space time ramifications.

Memory: 1 memory slot can hold 8 bits = 1 byte. So to store a variable 1, we store 0000 0001 in memory or for 3 , 0000 0011. We have 2^8 = 256 potential data values in 1 byte to store in each memory slot.
So how do we store a number bigger than 256 ? We increase the number of bits, say 32 or 64. We store in back to back free contiguos memory slots. int is 32 bits and long is 64 bits, so, int takes = 32/8 = 4 bytes = 4 back to back memory cell to store as each cell store 1 byte. To store int a=1; in memory, we do it as:

</p>

<img src="algorithms/notes/memory.JPG" width=47%><a> </a><img src="algorithms/notes/memory2.JPG" width=51.5%>