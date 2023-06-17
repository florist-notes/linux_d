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

Why put 0000 0001 to the left of all 4 cells and not right? Due to [Endianness](https://en.wikipedia.org/wiki/Endianness)!

Second figure is to store a list [1,2], 8 cells or 64 bits in total, 32 bits each i.e 4 byte and 4 byte. It needs a contiguos fixed width space/memory to store the list. Now, how to store strings? ASCII mapping. Each leter is mapped to a number and it is same thereafter. For pointers, we can store in a memory address , the memory address of another cell. Our computers can access these memory addresses directly, very quickly!

<b>Big O Notation:</b> In the worst case scenario. Let's take 3 different algorithms:
(1) f_1(a) => 1 + a[0]
(2) f_2(a) => sum(a)
(3) f_3(a) => pair(a)      ...a = [...N] (integer array of length N)

For N=1, (1),(2) & (3) runs almost in same time frame.For N=10000000, (1) runs instantly, (2) takes a bit time but (3) crashes and takes forever. The speed is dependent on the size of the array, so it is more meaningful to express speed in terms of size of input. If size of input grows, the time taken grows as well.
For (1) we have O(1), For (2) we have O(n) and for (3), we have O(n^2). From Asymptotic Analysis point of view, we consider O(8) == O(1) == Constant as it doesn't depends on the number of input. Even if input number changes, we'll have the same number of operations. So integer taking up 4 bytes or 8 bytes doesn't really matter for time complexity as it takes only O(1).
O(n^2+n+1) = O(n^2); O(2n^2) = O(n^2) ; O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(2^n) < O(n!)

<img src="algorithms/notes/bigo.webp" width=50%><a> </a><img src="algorithms/notes/bigo2.jpg" width=41.5%>

<b>Scenarios:</b>
1) Algorithm performing bunch of elementary operations ~ O(1)
2) Algorithm traversing an array once ~ O(n)
3) Algorithm traversing the array twice, left to right and back ~ O(2n)= O(n)
4) Algorithm to traverse an array with nested forloop (e.g pairing numbers) ~ O(n^2+2n) = O(n^2)
5) Algorithm to add two arrays with n and m numbers respectively ~ O(n+m)

<b>Logarithm:</b>
log_b(x) = y, iff b^y = x ; In computer science ,we always assume a base 2. So in logn, it has base 2 (Binary). In Mathematics we use base 10. log(1) = 0; log(4) = 2; log(16) = 4;
2^x = N, log(N) = x; So While N increase very large, x increases only by a minute amount. So x will be small and hence O(log(N)) is a much better complexity than O(N) as N increases. So O(log(N)) will be way better as input size increases. 2^20 ~ 1 Million , 2^30 ~ 1 Billion , so x only increased by 10 but N (input size) moved from 1 Million to a Billion. x here is time, but for O(N) it will be very linear.
e.g - Array of length 8 and an algorithm where in at every step it eliminated half of the array. Array [0, 1, 2, 3, 4, 5, 6, 7]. Let's say it elimiates the right side, at every step = [0, 1, 2, 3, 4, 5, 6, 7] → [0, 1, 2, 3] → [0, 1] → [0]. We had an array of length n = 8, and total amount of operations that we performed is basically log(n) ~ log(8) = 3 and here we performed 3 operations. If we increase array size by double, say [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] it will only take one extra step to get to [0, 1, 2, 3, 4, 5, 6, 7]. No of operation increases only by 1 as we double the input size. Half a Binary Tree in each iteration is O(logn).

<b>Arrays:</b> Say a = [1,2,3], and we have 64 bit integers so 8 bytes = 8 memory slots for each integer. For a , we need 3 x 8 = 24 memory slots. There are two types of arrays - Static Array and Dynamic Array. a[100] is a static array where we specify the length.

<img src="algorithms/notes/array.JPG" width=45%><a> </a><img src="algorithms/notes/linkedlist.JPG" width=48.5%>

<b>Reading/Write element of an array:</b> O(1) ST; Initialize an array: O(8N) ~ O(N) ST [for 64 bit int] for us N=3; Traverse: O(N) T, O(1) S; Copy: O(N) ST. Copying an array is expensive (slice an array etc) is O(n); Insertion: O(N) T, O(1) S. We need to shift elements, so we need to copy everything and find a new memory space of length (old memory length + 8 byte). This is nota good complexity to have considering we keep appeding values to an array all the time. So we need Dynamic Arrays! In C++ it is called a vector and in Java it is called an arraylist. Dynamic Arrays allows faster insertion at the end of the array. Dynamic arrays allocates close to 2x memory slot for a given array, so we have more space at the end. For [1,2,3] we have a dynamic array similar to [1,2,3,.,.,.] under the hood. Constant time insertion O(1). If we exhaust the extra space while inserting, only then we copy the array in memory similar to a static array. The copy will give another double amount of memory space that we need.
e.g: [1,.], We insert 2 in O(1) [1,2], then we insert 3 in O(N) (The array is copied to new space in memory with extra space for insertion and old memory space is freed), we have [1,2,3,.], we insert 4 in O(1) and have [1,2,3,4], then we insert 5 in O(N) giving us [1,2,3,4,5,.,.,.], where rest 6,7,8 is inserted in O(1).
Insert for Dynamic array: O(1) T , We have so many constant time insertions that the few linear time insertions gets cancelled out. This is known as Ammortized Analysis. If we want to insert in the middle or beginning of the array, then dynamic arrays won't really help. It will be O(n). Popping value out of an array/ removing value out of an array: pop() ~ O(1); To pop value from beginning or middle of an array ~ O(N). Because we are shifting.

<b>Linked List:</b> 3→1→4→2 . In array we have to allocate back to back memory slots, but in Linked List it overcomes that limitation. Linked List stores elements anywhere in the memory and they connect elements using pointers. Each element is called a node and it points to next node. Linked List can be anywhere in memory. First element is head of the linked list.
Get: O(i) T, where i is the index & O(1) S ; Set: O(i) T, O(1) S; Init: O(N) ST; Copy: O(N) ST; Traverse: O(N) T, O(1) S;
Insertion: 3→1→4→2 to 5→3→1→4→2 ; We create a new head node and point it to the old head node. O(1) ST, if insert at tail (some linked list has reference to tail ) if we dont have a reference to tail, we have to traverse the linked list and is O(n). Deletion:same ;
There's Doubly linked list, Circular linked lists.

<b>Hash Table</b>:
"foo" ⇒ 1
"bar" ⇒ 2
"baz" ⇒ 3

Hash Table is a key value store. Key {"foo", "bar", "baz"}. Insertion, Deleting or Searching a key-value pair are constant time operations O(1). Similar to arrays where keys are indices in arrays but in HT keys can be anything from strings to other data types. Key gets transformed into an index when passed through a hash function. So hash function converts {"foo", "bar", "baz"} into indexes against which values {1,2,3} are stored. So we have constant lookup ~ O(1).
Many hash functions!! to convert the strings {"foo", "bar", "baz"} into integer value indexes. Say we use conversion standard of ASCII character to encoded integer values and then sum up the encoded values. Say we get 301 for "foo", it is very huge number and we are only dealing with an array of 3 indices. So we 301 % n, where n = length of array. So 301 % 3 = 1 is the index for "foo". Say "bar" is 602 and "baz"is 90, so 602 % 3 is 2 and 90 % 3 is 0. So we have key value pair as , "foo" 1 ⇒ 1 , "bar" 2 ⇒ 2 and "baz" 0 ⇒ 3. What if two keys or strings map to same index? We create a linked list of potential values. The hashed keys out from a hash function collides and we need to store their value in the same index. Lets say "abr" index value is 2. So we store the value for keys "bar" and "abr" in the same index as a linked list. Here arises a problem, how do we know, which value is stored for "abr" or "bar" in the linked list. In each node of the linked list, we point it to the key. So, for same index in the Value table, we have a linked list and each node of the linked list points to the original key in memory. In the worst case, if every key after hashing, maps to the same value, it will create one huge linked list. So Insertion, Deletion and Searching is O(n). Hash Tables support constant time O(1) Insert, Search and Delete on average but on the worst case scenario, it is O(n).
Solution: Very strong hashing functions to minimise the number of collisions. They have become the standard that we assume O(1) for interviews and in industry. We treat the act of hashing keys, a constant time operation O(1). What happens if we run out of space in our underlying array of values. What if we had 300 keys ? so a 100 keys mapped to index 0, 100 keys mapped to index 1 and another 100 to index 2. We introduce the concept of resizing. We use a hash table that resizes itself (Sort of like a dynamic array would do). The overall space complexity is O(n).

<b>Stacks and Queus</b>:
Stacks are LIFO and Queues are FIFO. They support constant time & space O(1) ST for insertion and deletion of objects. Search is O(n) T, O(1) S. push(), pop() ; enqueue(), dequeue(); peek().

<b>Strings</b>: In ASCII Table ; A→65, a→97. Traversing through a string is O(n) T, O(1) S; Copy is O(n) ST, Get is O(1) ST. In C++ strings are mutable. In Python, Java string are immutable.
e.g - foobar = "this is a string", & if we do, foobar += "x"; In Python, (where strings are immutable) creates a brand new string and adds new letter to that string. It is not a contant time operation and is O(n). Similarly, adding two strings , concatenating two strings all are O(n+m).

<b>Graphs</b>: Graphs are made up of nodes and edges. A graph is said to be connected if you can reach any other node from one node within a graph. If graph has a cycle, we call it a cyclic graph. For cyclic graph, be careful with infinite loops. Sometimes when we are dealing with 2D arrays, they are mostly graph problems. Strings, and we are swapping letters in a string, e.g we have got "abc" and we wish to replace every letter of the string with the letter "x". This might lead to a graph structure, where nodes in the graphs are strings and the edges will be transformations (swap one character with "x"). While representing a graph in code, we represent it as an adjacency list. Maybe we can represent graphs in hash tables where we store every node as a key and key points to the relevant nodes. So every nodes stores a list of its neighbours or list of its adjacencies. Creating a graph, we are storing, V vertices and E edges. Space complexity of storing a graph is O (V+E). Traversing a graph has 2 main method : BFS and DFS. Time complexity for traversal is O(V+E).

<img src="algorithms/notes/graph.JPG" width=49%><a> </a><img src="algorithms/notes/tree.JPG" width=48.5%>

<b>Trees:</b> Each node in a tree can have only one parent. Different types of tree - Binary Tree, k-ary trees (atmost k child from each node), BST, Heaps - min & max heaps, Tries etc. Storing a tree will be O(n) S. Traversing an entire tree : O(n) T. Traversing from top to bottom via one path , say in a Binary Tree is O( log(n) ) T ~ Balanced Binary Tree. AVL or Red Black Tree are balanced to maintain O(logn). If the tree is skewed, then it will be O(n). A complete tree will be filled at every level except/maybe the last level, where only nodes filled from left to right is accepted. A tree is full when every node in the tree has no children node or k-children node, where k is the number in k-ary tree. For k=2 (Binary Tree), every node must have 2 children or no children. Perfect Tree: All the leaf nodes have the same depth.

Example of complete tree:

```

     o            o              o
    / \          / \            / \
   o   o       o   o         o   o
  / \  /       / \  / \      / \  / \
 o  o o     o  o o  o    o  o o  o
                             /
                            o
                            
                            
                            
```