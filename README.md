# DSA
A personal repo to keep track of my learning of DSA in Python

> in order to learn dsa , we need to have some understanding of BIg O notation and time complexities.
### The Language and metric we use to describe efficieny of an algorithm 

### Time complexity is a way of showing how runtime of a function increases as the size of the input increases.

> example : find a number in a an array : [1,2,3,4,5,6]
- find the number '1' in the array is best case scenario, which is Big 'Ω' 
- find the number '4' in the array is the average case scenario, which is Big 'Θ'
- find the number '6' is the worst case scenario which is Big O .

[BIG O Graph](bigO.png)

- O(1): ANy given input the runtime will reamin constant 
- O(n): Linear time complexity ; as input grows so do operations 
- O(n^2): operations increase exponentially as the no. of inputs increase
- O(logn): When the input size is reduced by half, maybe when iterating, handling recursion.

>## Rules for measuring codes using Big O :
- if your algorithm is in the form, "do this when you are all done, then do that" then you **add** the run times.
- if your algorithm is in the form, "do this for each time you do that" then you **multiply** the run times.

1. any assignment statements or if statements that get executed once regardless of the size of input, have time complexity as **O(1)**
2. a simple loop for 0 to n has **O(n)**
3. a nested loop of the same type has **O(n^2)** 
4. a loop whose controlling parameter is divided in steps at each step has **O(logn)**
5. when dealing with multiple statements, just add them up