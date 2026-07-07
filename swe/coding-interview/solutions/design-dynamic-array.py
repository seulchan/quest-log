"""
Problem:
https://neetcode.io/problems/dynamicArray/

Pattern:
- Arrays

Complexity:
- get / set: O(1)
- pushback: O(1) amortized (O(N) only when a resize triggers)
- popback: O(1)
- resize: O(N) to allocate and copy elements to the new array
- Space Complexity: O(N) where N is the current capacity of the array.

Insight:
A dynamic array achieves O(1) random access while supporting dynamic resizing. The core mechanic relies on fixed-size allocations; when the element count (`length`) reaches the allocated limits (`capacity`), a `resize()` occurs. By doubling the capacity during a resize rather than increasing it incrementally, the costly O(N) copy operations are minimized, allowing the `pushback` operation to maintain an average **O(1) Amortized** time complexity.

Review:
- **Amortized Analysis:** Even though resizing takes O(N) time, it happens so infrequently (only after doubling the number of elements) that spreading the cost over all pushbacks results in an average cost of O(1) per operation.
- **Lazy Deletion on Pop:** Your `popback` approach elegantly implements "lazy deletion" by simply decrementing `self.length` instead of physically clearing or shrinking the underlying array. This keeps the operation at strict O(1).
- **Pointer Invariant:** Tracking separate bounds for `self.length` (logical size) and `self.capacity` (physical container allocation size) is the foundational design invariant that governs all array boundary validations.
"""


class DynamicArray:
    def __init__(self, capacity: int):
        self.length = 0
        self.capacity = capacity
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity
