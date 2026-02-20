# Task 2 – Self Study

## Data Structure: Heap

A heap is a complete binary tree that satisfies the heap property.

In a Max Heap:
- The value of each parent node is greater than or equal to its children.

---

## Heap ADT

Operations supported:

- insert(value)
- extract_max()
- build_heap()

Time Complexity:
- insert(): O(log n)
- extract_max(): O(log n)
- build_heap(): O(n)

---

## Algorithm: Heap Sort

Heap Sort works as follows:

Step 1: Insert all elements into a Max Heap  
Step 2: Extract the maximum element repeatedly  
Step 3: Reverse the result to get ascending order  

---

## Example

Input:
[4, 10, 3, 5, 1]

Process:
- Build max heap
- Extract 10
- Extract 5
- Extract 4
- Extract 3
- Extract 1

Output:
[1, 3, 4, 5, 10]

---

## Time Complexity Analysis

- Best Case: O(n log n)
- Worst Case: O(n log n)
- Space Complexity: O(1)

---

## Applications

- Priority Queue
- Task Scheduling
- Graph Algorithms