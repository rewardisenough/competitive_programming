# Tower of Hanoi

# Goal
The goal of this game is to move all n disks from tower 1 to tower 3. You can only move one disk at a time and can't place larger disk on a smaller disk.

# Walkthrough

First, let's think of the solution when n=1. Solution is just A -> C.

Next, let's think of the solution when n=2. We know that largest disk has to be at C. 
Then, solution is A -> B, A -> C, B -> C. 

Before we move on to n=3, let's think about how we want our code to look like.

```
# for n=1.
print("A -> C")

# for n = 2.
print("A -> B")
print("A -> C")
print("B -> C")
```

Notice, for n=2, "A -> C" was in the middle. The same solution for n=2 can work for n=2 if we omit the first and third line of code.
Indeed, this looks similar to a concept called **recursion**.

Recursion occurs when you call the same function inside of the function. 
Thus, let's first make a function called 'hanoi'. Our parameter should include n(number of disk), start, middle, end). start,middle,end doesn't mean much here since their position changes through out the recursion.
```
def hanoi(n,start,middle,end):
  
```
Recursion also involves something called a "base case". Base case is needed to stop the recursion eventually.
In this context, our base case should obviously be when there is no disk left to move. n=0.
```
def hanoi(n,start,middle,end):
  # base case
  if(n==0):
    return 
```
We know that largest disk can only move to disk 3 regardless of n.
```
def hanoi(n,start,middle,end):
  # base case
  if(n==0):
    return
    
   print(f"{start} -> {end}") # these are called f-strings in python. 
```
Code for above only works when n=1. What if n=2?
```
def hanoi(n,start,middle,end):
  #base case
  if(n==0):
    return
   
   hanoi(n-1,start,end,middle) # A -> B
   
   print(f"{start} -> {end}") # A -> C
   
   hanoi(n-1, middle,start,end) # B -> C
```
First, you may ask why n-1? Because we already know how hanoi function works when n=1. Then, when we're trying to solve when n=2, we can use hanoi(n=1).
Hanoi(n=1) just moves 'start' to 'end'. 

Next, you may also notice that the position of the function parameter have changed. 
First function is now hanoi(n-1,start,end,middle) and second function is hanoi(n-1,middle,start,end).

```
The position of the parameter can be derived from when we first solved the problem without any code. 
We said " Then, solution is A -> B, A -> C, B -> C. ". 
```
Based on that observation, if we start with hanoi(2,"A","B","C"), it makes sense that first function is hanoi(n-1,start,end,middle) and second function is hanoi(n-1,middle,start,end).

We just saw that we can solve problem of n=2 just by using hanoi function with n=1. Then, we can also solve n=3 just by using hanoi function with n=2. 
Consequently, hanoi function with n=2 then uses hanoi function with n=1. Similar pattern occurs for any number of 'n'.

One important thing to notice is that when you call hanoi(3,"A","B","C"), inside of that function, hanoi(2,"A","C","B") and hanoi(2,"B","A","C") is called. 
That's what makes biggest disk moving from A -> C possible. It's interesting how the same code for solving n=2 can 'adapt' to solving n=3.


# Closing note
The purpose of writing this was to show my thought process of understanding the solution to this problem. When I initially saw the solution to this problem, I didn't understand it at all. So I decided to think about the solution from scratch. Through out that thinking process, I was able to understand the little details which was crucial to understanding the solution. 
