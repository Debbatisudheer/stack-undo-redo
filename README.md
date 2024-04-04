Stacks:
=======

    Time Complexity:
    ----------------
        Push (Insertion): O(1)
        Pop (Deletion): O(1)
        Peek (Access top element): O(1)
    Space Complexity:
    -----------------
    O(n)

    What is a Stack?
    ================

Think of a stack as a pile of books. You can only add or remove books from the top of the pile. This is known as Last In, First Out (LIFO) behavior.
Time Complexity:
Push (Insertion):
----------------

    When you add a new item to the stack, you're placing it on top of the existing items. Since you're always adding it to the top, it doesn't matter how big the stack is already; it takes the same amount of time. So, adding an item (pushing) is always quick, regardless of the size of the stack.
    Time Complexity: O(1) - This means adding an item to the stack takes constant time, no matter how big the stack is.

Pop (Deletion):
---------------

    When you remove an item from the stack, you always remove the topmost item. Again, it doesn't matter how big the stack is; you're always just removing the top item. So, removing an item (popping) is also quick, regardless of the size of the stack.
    Time Complexity: O(1) - This means removing an item from the stack also takes constant time, no matter how big the stack is.

Peek (Access top element):
--------------------------

    To see the item at the top of the stack without removing it, you just look at the top. It doesn't involve any rearrangement of the items in the stack.
    Time Complexity: O(1) - Accessing the top item is always quick because you're just looking at the topmost item without changing anything.

Space Complexity:
-----------------

    The space complexity of a stack refers to how much memory it uses.
    Each item you add to the stack consumes some memory space.
    If you have 'n' items in the stack, it will take up 'n' units of memory space.
    Space Complexity: O(n) - This means the amount of memory the stack uses increases linearly with the number of items in the stack.

So, in summary:

    Push, Pop, and Peek operations in a stack are all very efficient, taking constant time (O(1)).
    The amount of memory a stack uses grows linearly with the number of items it contains, making its space complexity O(n).


Time Complexity:
----------------
Push (Insertion):

    When you add a new item (plate) to the stack, you just put it on top. It doesn't matter how many items are already there; you always add to the top.
    Time Complexity: Adding an item is always fast, no matter how big the stack is.

Pop (Deletion):
----------------

    When you remove an item (plate) from the stack, you always take the one from the top.
    Time Complexity: Removing an item is also always fast, no matter how big the stack is.

Peek (Access top element):
-------------------------

    To see the top item (plate) without removing it, you just look at the top.
    Time Complexity: Looking at the top item is always fast, no matter how big the stack is.

Space Complexity:
------------------

    Space complexity refers to how much memory the stack uses.
    Each item you add to the stack takes up some memory.
    If you have 'n' items in the stack, it will take up 'n' units of memory.
    Space Complexity: The more items you have, the more memory the stack uses, growing in a straight line.

So, to put it simply:

    Adding, removing, and looking at items in a stack are all very quick, no matter how many items are in the stack.
    The memory used by the stack grows steadily as you add more items, but it grows at a predictable rate.

    Typically, stacks are not used directly for iteration or recursion. Instead, they are used as a supporting data structure for implementing algorithms that involve iteration or recursion.

    Iteration: Iteration is often implemented using loops, such as for or while loops. Stacks can be used in certain cases to implement specific types of iteration, like in depth-first search (DFS) algorithms, where you use a stack to keep track of nodes to visit.

    Recursion: Recursion involves a function calling itself. Stacks come into play here implicitly, due to the call stack maintained by the programming language. Each function call is pushed onto the call stack, and when a function returns, it is popped off the stack. This behavior resembles a stack data structure.

So, while stacks are not directly used for iteration or recursion in the sense of writing loops or recursive functions, they are often involved in the underlying mechanics of these processes.
